from datetime import datetime, timedelta
from typing import Optional
from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
import sqlite3
import os
from fastapi import FastAPI

# Security configuration
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here-change-in-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT token security
security = HTTPBearer()

# Pydantic models
class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    full_name: Optional[str] = None

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class User(BaseModel):
    id: int
    username: str
    email: str
    full_name: Optional[str] = None
    is_active: bool

class AuthManager:
    def __init__(self, db_path: str = "soc_cmm_translated.db"):
        self.db_path = db_path
        self.SECRET_KEY = SECRET_KEY
    
    def get_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn
    
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Verify a password against its hash"""
        return pwd_context.verify(plain_password, hashed_password)
    
    def get_password_hash(self, password: str) -> str:
        """Hash a password"""
        return pwd_context.hash(password)
    
    def create_user(self, username: str, email: str, password: str, full_name: str = None) -> int:
        """Create a new user"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Check if user already exists
        cursor.execute("SELECT id FROM users WHERE username = ? OR email = ?", (username, email))
        if cursor.fetchone():
            conn.close()
            raise HTTPException(
                status_code=400,
                detail="Username or email already registered"
            )
        
        # Hash password and create user
        hashed_password = self.get_password_hash(password)
        
        cursor.execute("""
            INSERT INTO users (username, email, hashed_password, full_name)
            VALUES (?, ?, ?, ?)
        """, (username, email, hashed_password, full_name))
        
        user_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return user_id
    
    def authenticate_user(self, username: str, password: str) -> Optional[dict]:
        """Authenticate a user"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()
        
        if not user:
            return None
        
        if not self.verify_password(password, user['hashed_password']):
            return None
        
        return dict(user)
    
    def get_user(self, user_id: int) -> Optional[dict]:
        """Get user by ID"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        user = cursor.fetchone()
        conn.close()
        
        return dict(user) if user else None
    
    def get_user_by_username(self, username: str) -> Optional[dict]:
        """Get user by username"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()
        
        return dict(user) if user else None

# Global auth manager instance
auth_manager = AuthManager()

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Create a JWT access token"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)) -> dict:
    """Verify JWT token and return user data"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    
    user = auth_manager.get_user_by_username(username=token_data.username)
    if user is None:
        raise credentials_exception
    
    return user

def get_current_user(token: str = Depends(security)) -> dict:
    """Get current authenticated user"""
    return verify_token(token)

def get_current_active_user(current_user: dict = Depends(get_current_user)) -> dict:
    """Get current active user"""
    if not current_user.get("is_active"):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

router = APIRouter()

class PasswordChangeRequest(BaseModel):
    current_password: str
    new_password: str
    confirm_password: str

@router.post("/api/auth/change-password")
def change_password(request: PasswordChangeRequest, current_user: dict = Depends(get_current_active_user)):
    """Change the password for the current user"""
    if request.new_password != request.confirm_password:
        raise HTTPException(status_code=400, detail="New passwords do not match")
    if len(request.new_password) < 8:
        raise HTTPException(status_code=400, detail="Password must be at least 8 characters long")
    if not auth_manager.verify_password(request.current_password, current_user['hashed_password']):
        raise HTTPException(status_code=400, detail="Current password is incorrect")
    
    # Update password
    hashed_password = auth_manager.get_password_hash(request.new_password)
    conn = auth_manager.get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET hashed_password = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?", (hashed_password, current_user['id']))
    conn.commit()
    conn.close()
    return {"message": "Password changed successfully"}

def include_auth_routes(app: FastAPI):
    app.include_router(router)