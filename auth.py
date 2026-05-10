"""
Módulo de Autenticação (JWT + Bcrypt)

- Registro, login e gerenciamento de usuários
- Geração/validação de tokens JWT
- Hash de senha com bcrypt
- Funções utilitárias para obter usuário atual e verificar permissões
"""
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
SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise RuntimeError(
        "SECRET_KEY environment variable is required. "
        "Generate one with: python -c \"import secrets; print(secrets.token_urlsafe(48))\" "
        "and export it before starting the application. See .env.example."
    )
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

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
    """Fornece operações de autenticação e gerenciamento de usuários."""
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
    
    def create_user(self, username: str, email: str, password: str, full_name: str = None, is_admin: bool = False) -> int:
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
            INSERT INTO users (username, email, hashed_password, full_name, is_admin)
            VALUES (?, ?, ?, ?, ?)
        """, (username, email, hashed_password, full_name, is_admin))
        
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

    def update_user(self, user_id: int, username: str, email: str, full_name: str = None, is_active: bool = True, is_admin: bool = False) -> bool:
        """Update user information"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                UPDATE users 
                SET username = ?, email = ?, full_name = ?, is_active = ?, is_admin = ?, updated_at = CURRENT_TIMESTAMP
                WHERE id = ?
            """, (username, email, full_name, is_active, is_admin, user_id))
            
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            conn.close()
            return False
    
    def update_user_password(self, user_id: int, new_password: str) -> bool:
        """Update user password"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            hashed_password = self.get_password_hash(new_password)
            cursor.execute("""
                UPDATE users 
                SET hashed_password = ?, updated_at = CURRENT_TIMESTAMP
                WHERE id = ?
            """, (hashed_password, user_id))
            
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            conn.close()
            return False
    
    def delete_user(self, user_id: int) -> bool:
        """Delete a user (admin only)"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            # First delete all related data
            cursor.execute("DELETE FROM assessment_answers WHERE assessment_id IN (SELECT id FROM assessments WHERE customer_id IN (SELECT id FROM customers WHERE user_id = ?))", (user_id,))
            cursor.execute("DELETE FROM assessment_scores WHERE assessment_id IN (SELECT id FROM assessments WHERE customer_id IN (SELECT id FROM customers WHERE user_id = ?))", (user_id,))
            cursor.execute("DELETE FROM assessments WHERE customer_id IN (SELECT id FROM customers WHERE user_id = ?)", (user_id,))
            cursor.execute("DELETE FROM customers WHERE user_id = ?", (user_id,))
            cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
            
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            conn.close()
            return False

# Global auth manager instance
auth_manager = AuthManager()

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Cria um token JWT de acesso com expiração."""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)) -> dict:
    """Valida o token JWT e retorna os dados do usuário."""
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
    """Retorna o usuário autenticado atual."""
    return verify_token(token)

def get_current_active_user(current_user: dict = Depends(get_current_user)) -> dict:
    """Garante que o usuário atual está ativo."""
    if not current_user.get("is_active"):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

def get_current_admin_user(current_user: dict = Depends(get_current_active_user)) -> dict:
    """Garante que o usuário atual é administrador."""
    if not current_user.get("is_admin"):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acesso negado. Apenas administradores podem acessar esta funcionalidade."
        )
    return current_user

router = APIRouter()

class PasswordChangeRequest(BaseModel):
    current_password: str
    new_password: str
    confirm_password: str


def include_auth_routes(app: FastAPI):
    app.include_router(router)