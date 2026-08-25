"""
Aplicação FastAPI do SOC CMM Assessment System.

- Rotas web (templates Jinja2) e rotas de API REST
- Autenticação via JWT e cookies (isolamento por usuário)
- Suporte a idiomas (EN/PT-BR) com seletor e cookie de preferência
- Integração com SQLite via `database.py`
"""
from fastapi import FastAPI, HTTPException, Request, Form, Depends, status
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from typing import Optional, List
import uvicorn
import os
from datetime import timedelta

from pathlib import Path

from database import DatabaseManager
from auth import auth_manager, create_access_token, get_current_active_user, get_current_admin_user, UserCreate, UserLogin, Token, include_auth_routes

app = FastAPI(title="SOC CMM Assessment System", version="1.0.0")
include_auth_routes(app)

# CORS: lista de origens vem de ALLOWED_ORIGINS (CSV). Default seguro = localhost.
# Para liberar tudo em redes confiáveis, defina ALLOWED_ORIGINS=*
_allowed_origins_env = os.getenv("ALLOWED_ORIGINS", "http://localhost:8000")
allowed_origins = [o.strip() for o in _allowed_origins_env.split(",") if o.strip()]
# allow_credentials só é compatível com lista explícita — desliga se for wildcard
allow_credentials = allowed_origins != ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=allow_credentials,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database
db = DatabaseManager()

# Configura templates e arquivos estáticos
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

# Modelos Pydantic (validação de payloads da API)
class CustomerCreate(BaseModel):
    name: str
    email: Optional[str] = None
    organization: Optional[str] = None

class AssessmentCreate(BaseModel):
    customer_id: int
    name: Optional[str] = None

class AnswerSubmit(BaseModel):
    assessment_id: int
    question_id: int
    answer_option_id: Optional[int] = None
    answer_text: Optional[str] = None

class UserUpdate(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None
    is_active: bool = True
    is_admin: bool = False

class UserPasswordUpdate(BaseModel):
    current_password: str
    new_password: str
    confirm_password: str

# Dependência de segurança (Bearer opcional; também suporta cookie)
security = HTTPBearer(auto_error=False)

# Função auxiliar de autenticação
async def get_current_user_from_request(request: Request):
    """Obtém o usuário atual pelos cookies (ou headers)."""
    token = request.cookies.get("access_token")
    if not token:
        return None
    
    try:
        # Decode JWT token to get username
        from jose import jwt
        payload = jwt.decode(token, auth_manager.SECRET_KEY, algorithms=["HS256"])
        username = payload.get("sub")
        if username:
            user = auth_manager.get_user_by_username(username)
            return user
    except Exception as e:
        print(f"Erro ao decodificar o token: {e}")
        return None
    
    return None

# Função auxiliar de idioma
def get_language_from_request(request: Request) -> str:
    """Obtém o idioma pelos parâmetros de query ou cookies (padrão: en)."""
    # First check query parameter
    lang = request.query_params.get("lang")
    if lang in ["en", "pt_br"]:
        return lang
    
    # Then check cookie
    lang = request.cookies.get("language")
    if lang in ["en", "pt_br"]:
        return lang
    
    # Default to English
    return "en"

def get_template_name(base_name: str, language: str) -> str:
    """Retorna o nome do template conforme o idioma."""
    if language == "pt_br":
        return f"{base_name}_pt_br.html"
    return f"{base_name}.html"

# New authentication dependency that supports both cookies and Bearer tokens
async def get_current_user_flexible(request: Request, credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Get current user from either cookies or Bearer token"""
    # First try to get from cookies
    user = await get_current_user_from_request(request)
    if user:
        return user
    
    # If no user from cookies, try Bearer token
    if credentials:
        try:
            # Verify Bearer token directly
            from jose import jwt, JWTError
            payload = jwt.decode(credentials.credentials, auth_manager.SECRET_KEY, algorithms=["HS256"])
            username: str = payload.get("sub")
            if username:
                user = auth_manager.get_user_by_username(username)
                if user:
                    return user
        except Exception as e:
            print(f"Erro na verificação do token Bearer: {e}")
            pass
    
    # If neither works, raise authentication error
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Não autenticado",
        headers={"WWW-Authenticate": "Bearer"},
    )

async def get_current_active_user_flexible(current_user: dict = Depends(get_current_user_flexible)) -> dict:
    """Get current active user with flexible authentication"""
    if not current_user.get("is_active"):
        raise HTTPException(status_code=400, detail="Usuário inativo")
    return current_user

async def get_current_admin_user_flexible(current_user: dict = Depends(get_current_active_user_flexible)) -> dict:
    """Get current admin user with flexible authentication"""
    if not current_user.get("is_admin"):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acesso negado. Apenas administradores podem acessar esta funcionalidade."
        )
    return current_user

# API Routes

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Home page"""
    user = await get_current_user_from_request(request)
    language = get_language_from_request(request)
    template_name = get_template_name("index", language)
    
    response = templates.TemplateResponse(template_name, {
        "request": request, 
        "user": user,
        "language": language
    })
    
    # Set language cookie if not already set
    if not request.cookies.get("language"):
        response.set_cookie("language", language, max_age=31536000)  # 1 year
    
    return response

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    """Login page"""
    language = get_language_from_request(request)
    template_name = get_template_name("login", language)
    
    response = templates.TemplateResponse(template_name, {
        "request": request,
        "language": language
    })
    
    if not request.cookies.get("language"):
        response.set_cookie("language", language, max_age=31536000)
    
    return response

@app.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    """Register page"""
    language = get_language_from_request(request)
    template_name = get_template_name("register", language)
    
    response = templates.TemplateResponse(template_name, {
        "request": request,
        "language": language
    })
    
    if not request.cookies.get("language"):
        response.set_cookie("language", language, max_age=31536000)
    
    return response

@app.get("/terms", response_class=HTMLResponse)
async def terms_page(request: Request):
    """Terms and conditions page"""
    user = await get_current_user_from_request(request)
    language = get_language_from_request(request)
    template_name = get_template_name("terms", language)
    
    response = templates.TemplateResponse(template_name, {
        "request": request, 
        "user": user,
        "language": language
    })
    
    if not request.cookies.get("language"):
        response.set_cookie("language", language, max_age=31536000)
    
    return response

@app.get("/help", response_class=HTMLResponse)
async def help_page(request: Request):
    """Help page"""
    user = await get_current_user_from_request(request)
    language = get_language_from_request(request)
    template_name = get_template_name("help", language)
    
    response = templates.TemplateResponse(template_name, {
        "request": request, 
        "user": user,
        "language": language
    })
    
    if not request.cookies.get("language"):
        response.set_cookie("language", language, max_age=31536000)
    
    return response

@app.get("/privacy-policy", response_class=HTMLResponse)
async def privacy_policy_page(request: Request):
    """Privacy Policy page"""
    user = await get_current_user_from_request(request)
    language = get_language_from_request(request)
    template_name = get_template_name("privacy_policy", language)
    
    response = templates.TemplateResponse(template_name, {
        "request": request, 
        "user": user,
        "language": language
    })
    
    if not request.cookies.get("language"):
        response.set_cookie("language", language, max_age=31536000)
    
    return response

@app.get("/faq", response_class=HTMLResponse)
async def faq_page(request: Request):
    """FAQ page"""
    user = await get_current_user_from_request(request)
    language = get_language_from_request(request)
    template_name = get_template_name("faq", language)
    
    response = templates.TemplateResponse(template_name, {
        "request": request, 
        "user": user,
        "language": language
    })
    
    if not request.cookies.get("language"):
        response.set_cookie("language", language, max_age=31536000)
    
    return response

@app.get("/about", response_class=HTMLResponse)
async def about_page(request: Request):
    """About Us page"""
    user = await get_current_user_from_request(request)
    language = get_language_from_request(request)
    template_name = get_template_name("about", language)

    response = templates.TemplateResponse(template_name, {
        "request": request,
        "user": user,
        "language": language
    })

    if not request.cookies.get("language"):
        response.set_cookie("language", language, max_age=31536000)

    return response

@app.get("/change-language/{language}")
async def change_language(request: Request, language: str):
    """Change language and redirect back to previous page"""
    if language not in ["en", "pt_br"]:
        language = "en"
    
    # Get the referer URL or default to home
    referer = request.headers.get("referer", "/")
    
    # Create response that redirects back
    response = RedirectResponse(url=referer, status_code=302)
    
    # Set the language cookie
    response.set_cookie("language", language, max_age=31536000)  # 1 year
    
    return response

@app.post("/api/auth/register")
async def register(user: UserCreate):
    """Register a new user"""
    try:
        user_id = auth_manager.create_user(
            username=user.username,
            email=user.email,
            password=user.password,
            full_name=user.full_name
        )
        return {"message": "Usuário registrado com sucesso", "user_id": user_id}
    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content={"detail": e.detail})

@app.post("/api/auth/login")
async def login(user_credentials: UserLogin):
    """Login user"""
    user = auth_manager.authenticate_user(user_credentials.username, user_credentials.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(hours=24)  # Aumentado para 24 horas
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    
    response = JSONResponse(content={
        "access_token": access_token, 
        "token_type": "bearer", 
        "user": user
    })
    
    # Set cookie
    response.set_cookie(
        key="access_token",
        value=access_token,
        max_age=86400,  # 24 hours (24 * 60 * 60)
        httponly=True,
        secure=False,  # Set to True in production with HTTPS
        samesite="lax"
    )
    
    return response

@app.post("/api/auth/logout")
async def logout():
    """Logout user"""
    response = JSONResponse(content={"message": "Deslogado com sucesso"})
    response.delete_cookie(
        key="access_token",
        httponly=True,
        secure=False,
        samesite="lax"
    )
    return response

@app.post("/api/auth/change-password")
async def change_password(password_update: UserPasswordUpdate, request: Request):
    """Change user password"""
    user = await get_current_user_from_request(request)
    if not user:
        raise HTTPException(status_code=401, detail="Não autorizado")
    
    # Verify current password
    if not auth_manager.verify_password(password_update.current_password, user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Senha atual incorreta")
    
    # Verify new password confirmation
    if password_update.new_password != password_update.confirm_password:
        raise HTTPException(status_code=400, detail="As senhas não coincidem")
    
    # Verify new password length
    if len(password_update.new_password) < 8:
        raise HTTPException(status_code=400, detail="A senha deve ter pelo menos 8 caracteres")
    
    user_id = user["id"]
    success = auth_manager.update_user_password(user_id, password_update.new_password)
    if not success:
        raise HTTPException(status_code=400, detail="Falha ao atualizar a senha")
    return {"message": "Senha atualizada com sucesso"}

@app.get("/customers", response_class=HTMLResponse)
async def customers_page(request: Request):
    """Customers management page"""
    user = await get_current_user_from_request(request)
    if not user:
        return RedirectResponse(url="/login", status_code=302)
    
    language = get_language_from_request(request)
    template_name = get_template_name("customers", language)
    customers = db.get_customers(user_id=user["id"])
    
    response = templates.TemplateResponse(template_name, {
        "request": request, 
        "customers": customers,
        "user": user,
        "language": language
    })
    
    if not request.cookies.get("language"):
        response.set_cookie("language", language, max_age=31536000)
    
    return response

@app.get("/assessment/{assessment_id}", response_class=HTMLResponse)
async def assessment_page(request: Request, assessment_id: int):
    """Assessment questionnaire page"""
    user = await get_current_user_from_request(request)
    if not user:
        return RedirectResponse(url="/login", status_code=302)
    
    assessment = db.get_assessment(assessment_id)
    if not assessment:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")
    
    customer = db.get_customer(assessment['customer_id'])
    # Check if customer belongs to current user
    if customer['user_id'] != user['id']:
        raise HTTPException(status_code=403, detail="Acesso negado")
    
    language = get_language_from_request(request)
    template_name = get_template_name("assessment", language)
    domains = db.get_domains(language)
    
    response = templates.TemplateResponse(template_name, {
        "request": request,
        "assessment": assessment,
        "customer": customer,
        "domains": domains,
        "user": user,
        "language": language
    })
    
    if not request.cookies.get("language"):
        response.set_cookie("language", language, max_age=31536000)
    
    return response

@app.get("/results/{assessment_id}", response_class=HTMLResponse)
async def results_page(request: Request, assessment_id: int):
    """Assessment results page"""
    user = await get_current_user_from_request(request)
    if not user:
        return RedirectResponse(url="/login", status_code=302)
    
    assessment = db.get_assessment(assessment_id)
    if not assessment:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")
    
    customer = db.get_customer(assessment['customer_id'])
    # Check if customer belongs to current user
    if customer['user_id'] != user['id']:
        raise HTTPException(status_code=403, detail="Acesso negado")
    
    language = get_language_from_request(request)
    template_name = get_template_name("results", language)
    scores = db.get_assessment_scores(assessment_id, language)
    radar_data = db.get_radar_chart_data(assessment_id, language)
    
    response = templates.TemplateResponse(template_name, {
        "request": request,
        "assessment": assessment,
        "customer": customer,
        "scores": scores,
        "radar_data": radar_data,
        "user": user,
        "language": language
    })
    
    if not request.cookies.get("language"):
        response.set_cookie("language", language, max_age=31536000)
    
    return response

@app.get("/change-password", response_class=HTMLResponse)
async def change_password_page(request: Request):
    user = await get_current_user_from_request(request)
    if not user:
        return RedirectResponse(url="/login", status_code=302)
    
    language = get_language_from_request(request)
    template_name = get_template_name("change_password", language)
    
    response = templates.TemplateResponse(template_name, {
        "request": request, 
        "user": user,
        "language": language
    })
    
    if not request.cookies.get("language"):
        response.set_cookie("language", language, max_age=31536000)
    
    return response

@app.get("/admin", response_class=HTMLResponse)
async def admin_dashboard(request: Request):
    """Admin dashboard page"""
    user = await get_current_user_from_request(request)
    if not user:
        return RedirectResponse(url="/login", status_code=302)
    
    # Check if user is admin
    if not user.get("is_admin"):
        return RedirectResponse(url="/", status_code=302)
    
    stats = db.get_dashboard_stats()
    return templates.TemplateResponse("admin_dashboard.html", {
        "request": request, 
        "user": user,
        "stats": stats
    })

@app.get("/admin/users", response_class=HTMLResponse)
async def admin_users_page(request: Request):
    """Admin users management page"""
    user = await get_current_user_from_request(request)
    if not user:
        return RedirectResponse(url="/login", status_code=302)
    
    # Check if user is admin
    if not user.get("is_admin"):
        return RedirectResponse(url="/", status_code=302)
    
    users = db.get_all_users()
    return templates.TemplateResponse("admin_users.html", {
        "request": request, 
        "users": users,
        "user": user
    })

@app.get("/admin/users/{user_id}/edit", response_class=HTMLResponse)
async def admin_edit_user_page(request: Request, user_id: int):
    """Admin edit user page"""
    user = await get_current_user_from_request(request)
    if not user:
        return RedirectResponse(url="/login", status_code=302)
    
    # Check if user is admin
    if not user.get("is_admin"):
        return RedirectResponse(url="/", status_code=302)
    
    target_user = db.get_user_by_id(user_id)
    if not target_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    return templates.TemplateResponse("admin_edit_user.html", {
        "request": request, 
        "user": user,
        "target_user": target_user
    })

@app.get("/admin/users/new", response_class=HTMLResponse)
async def admin_new_user_page(request: Request):
    """Admin create new user page"""
    user = await get_current_user_from_request(request)
    if not user:
        return RedirectResponse(url="/login", status_code=302)
    
    # Check if user is admin
    if not user.get("is_admin"):
        return RedirectResponse(url="/", status_code=302)
    
    return templates.TemplateResponse("admin_new_user.html", {
        "request": request, 
        "user": user
    })

# API Endpoints

@app.post("/api/customers")
async def create_customer(customer: CustomerCreate, current_user: dict = Depends(get_current_active_user_flexible)):
    """Create a new customer"""
    customer_id = db.create_customer(
        user_id=current_user["id"],
        name=customer.name,
        email=customer.email,
        organization=customer.organization
    )
    return {"id": customer_id, "message": "Cliente criado com sucesso"}

@app.get("/api/customers")
async def get_customers(current_user: dict = Depends(get_current_active_user_flexible)):
    """Get all customers for the current user"""
    customers = db.get_customers(user_id=current_user["id"])
    return {"customers": customers}

@app.get("/api/customers/{customer_id}")
async def get_customer(customer_id: int, current_user: dict = Depends(get_current_active_user_flexible)):
    """Get customer details"""
    customer = db.get_customer(customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    
    # Check if customer belongs to current user
    if customer['user_id'] != current_user['id']:
        raise HTTPException(status_code=403, detail="Acesso negado")
    
    return {"customer": customer}

@app.post("/api/assessments")
async def create_assessment(assessment: AssessmentCreate, current_user: dict = Depends(get_current_active_user_flexible)):
    """Create a new assessment"""
    # Verify customer belongs to current user
    customer = db.get_customer(assessment.customer_id)
    if not customer or customer['user_id'] != current_user['id']:
        raise HTTPException(status_code=403, detail="Acesso negado")
    
    assessment_id = db.create_assessment(
        customer_id=assessment.customer_id,
        name=assessment.name
    )
    return {"id": assessment_id, "message": "Avaliação criada com sucesso"}

@app.get("/api/customers/{customer_id}/assessments")
async def get_customer_assessments(customer_id: int, current_user: dict = Depends(get_current_active_user_flexible)):
    """Get all assessments for a customer"""
    # Verify customer belongs to current user
    customer = db.get_customer(customer_id)
    if not customer or customer['user_id'] != current_user['id']:
        raise HTTPException(status_code=403, detail="Acesso negado")
    
    assessments = db.get_customer_assessments(customer_id)
    return {"assessments": assessments}

@app.get("/api/assessments/{assessment_id}")
async def get_assessment(assessment_id: int):
    """Get assessment details"""
    assessment = db.get_assessment(assessment_id)
    if not assessment:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")
    return {"assessment": assessment}

@app.put("/api/assessments/{assessment_id}/complete")
async def complete_assessment(assessment_id: int):
    """Mark assessment as complete"""
    assessment = db.get_assessment(assessment_id)
    if not assessment:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")
    
    # Calculate scores before completing
    db.calculate_assessment_scores(assessment_id)
    db.complete_assessment(assessment_id)
    
    return {"message": "Avaliação concluída com sucesso"}

@app.get("/api/domains")
async def get_domains(request: Request):
    """Get all domains"""
    language = get_language_from_request(request)
    domains = db.get_domains(language)
    return {"domains": domains}

@app.get("/api/domains/{domain_id}/aspects")
async def get_domain_aspects(domain_id: int, request: Request):
    """Get aspects for a domain"""
    language = get_language_from_request(request)
    aspects = db.get_domain_aspects(domain_id, language)
    return {"aspects": aspects}

@app.get("/api/aspects/{aspect_id}/questions")
async def get_aspect_questions(aspect_id: str, request: Request):
    """Get questions for an aspect"""
    language = get_language_from_request(request)
    questions = db.get_aspect_questions(aspect_id, language)
    return {"questions": questions}

@app.get("/api/assessments/{assessment_id}/answers")
async def get_assessment_answers(assessment_id: int):
    """Get all answers for an assessment"""
    assessment = db.get_assessment(assessment_id)
    if not assessment:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")
    
    answers = db.get_assessment_answers(assessment_id)
    return {"answers": answers}

@app.post("/api/answers")
async def submit_answer(answer: AnswerSubmit):
    """Submit an answer"""
    db.save_answer(
        assessment_id=answer.assessment_id,
        question_id=answer.question_id,
        answer_option_id=answer.answer_option_id,
        answer_text=answer.answer_text
    )
    return {"message": "Resposta salva com sucesso"}

@app.get("/api/assessments/{assessment_id}/scores")
async def get_assessment_scores(assessment_id: int, request: Request):
    """Get assessment scores"""
    assessment = db.get_assessment(assessment_id)
    if not assessment:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")

    language = get_language_from_request(request)
    scores = db.get_assessment_scores(assessment_id, language)
    return {"scores": scores}

@app.get("/api/assessments/{assessment_id}/radar-data")
async def get_radar_chart_data(assessment_id: int, request: Request):
    """Get radar chart data for assessment"""
    assessment = db.get_assessment(assessment_id)
    if not assessment:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")

    language = get_language_from_request(request)
    radar_data = db.get_radar_chart_data(assessment_id, language)
    return {"radar_data": radar_data}

# Admin API Endpoints

@app.get("/api/admin/dashboard")
async def get_admin_dashboard(current_user: dict = Depends(get_current_admin_user_flexible)):
    """Get admin dashboard statistics"""
    stats = db.get_dashboard_stats()
    return {"stats": stats}

@app.get("/api/admin/users")
async def get_all_users(current_user: dict = Depends(get_current_admin_user_flexible)):
    """Get all users for admin management"""
    users = db.get_all_users()
    return {"users": users}

@app.get("/api/admin/users/{user_id}")
async def get_user_by_id(user_id: int, current_user: dict = Depends(get_current_admin_user_flexible)):
    """Get user by ID for admin management"""
    user = db.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return {"user": user}

@app.put("/api/admin/users/{user_id}")
async def update_user(user_id: int, user_update: UserUpdate, current_user: dict = Depends(get_current_admin_user_flexible)):
    """Update user information"""
    success = auth_manager.update_user(
        user_id=user_id,
        username=user_update.username,
        email=user_update.email,
        full_name=user_update.full_name,
        is_active=user_update.is_active,
        is_admin=user_update.is_admin
    )
    
    if not success:
        raise HTTPException(status_code=400, detail="Falha ao atualizar o usuário")
    
    return {"message": "Usuário atualizado com sucesso"}

@app.put("/api/admin/users/{user_id}/password")
async def update_user_password(user_id: int, password_update: UserPasswordUpdate, current_user: dict = Depends(get_current_admin_user_flexible)):
    """Update user password"""
    if password_update.new_password != password_update.confirm_password:
        raise HTTPException(status_code=400, detail="As senhas não coincidem")
    
    if len(password_update.new_password) < 8:
        raise HTTPException(status_code=400, detail="A senha deve ter pelo menos 8 caracteres")
    
    success = auth_manager.update_user_password(user_id, password_update.new_password)
    
    if not success:
        raise HTTPException(status_code=400, detail="Falha ao atualizar a senha")
    
    return {"message": "Senha atualizada com sucesso"}

@app.delete("/api/admin/users/{user_id}")
async def delete_user(user_id: int, current_user: dict = Depends(get_current_admin_user_flexible)):
    """Delete a user"""
    if user_id == current_user["id"]:
        raise HTTPException(status_code=400, detail="Não é possível deletar sua própria conta")
    
    success = auth_manager.delete_user(user_id)
    
    return {"message": "Usuário deletado com sucesso"}

@app.get("/api/customers/{customer_id}/progress")
async def get_customer_progress(customer_id: int, request: Request):
    """Get progress over time for a customer"""
    language = get_language_from_request(request)
    assessments = db.get_customer_assessments(customer_id)

    progress_data = []
    for assessment in assessments:
        if assessment['status'] == 'completed':
            radar_data = db.get_radar_chart_data(assessment['id'], language)
            progress_data.append({
                'assessment_id': assessment['id'],
                'name': assessment['name'],
                'completed_at': assessment['completed_at'],
                'radar_data': radar_data
            })
    
    return {"progress": progress_data}

if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8400"))
    uvicorn.run(app, host=host, port=port)

