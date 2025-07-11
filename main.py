from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import uvicorn
import os

from database import DatabaseManager

app = FastAPI(title="SOC CMM Assessment System", version="1.0.0")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database
db = DatabaseManager()

# Setup templates and static files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Pydantic models
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

# API Routes

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Home page"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/customers", response_class=HTMLResponse)
async def customers_page(request: Request):
    """Customers management page"""
    customers = db.get_customers()
    return templates.TemplateResponse("customers.html", {
        "request": request, 
        "customers": customers
    })

@app.get("/assessment/{assessment_id}", response_class=HTMLResponse)
async def assessment_page(request: Request, assessment_id: int):
    """Assessment questionnaire page"""
    assessment = db.get_assessment(assessment_id)
    if not assessment:
        raise HTTPException(status_code=404, detail="Assessment not found")
    
    customer = db.get_customer(assessment['customer_id'])
    domains = db.get_domains()
    
    return templates.TemplateResponse("assessment.html", {
        "request": request,
        "assessment": assessment,
        "customer": customer,
        "domains": domains
    })

@app.get("/results/{assessment_id}", response_class=HTMLResponse)
async def results_page(request: Request, assessment_id: int):
    """Assessment results page"""
    assessment = db.get_assessment(assessment_id)
    if not assessment:
        raise HTTPException(status_code=404, detail="Assessment not found")
    
    customer = db.get_customer(assessment['customer_id'])
    scores = db.get_assessment_scores(assessment_id)
    radar_data = db.get_radar_chart_data(assessment_id)
    
    return templates.TemplateResponse("results.html", {
        "request": request,
        "assessment": assessment,
        "customer": customer,
        "scores": scores,
        "radar_data": radar_data
    })

# API Endpoints

@app.post("/api/customers")
async def create_customer(customer: CustomerCreate):
    """Create a new customer"""
    customer_id = db.create_customer(
        name=customer.name,
        email=customer.email,
        organization=customer.organization
    )
    return {"id": customer_id, "message": "Customer created successfully"}

@app.get("/api/customers")
async def get_customers():
    """Get all customers"""
    customers = db.get_customers()
    return {"customers": customers}

@app.get("/api/customers/{customer_id}")
async def get_customer(customer_id: int):
    """Get customer details"""
    customer = db.get_customer(customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return {"customer": customer}

@app.post("/api/assessments")
async def create_assessment(assessment: AssessmentCreate):
    """Create a new assessment"""
    assessment_id = db.create_assessment(
        customer_id=assessment.customer_id,
        name=assessment.name
    )
    return {"id": assessment_id, "message": "Assessment created successfully"}

@app.get("/api/customers/{customer_id}/assessments")
async def get_customer_assessments(customer_id: int):
    """Get all assessments for a customer"""
    assessments = db.get_customer_assessments(customer_id)
    return {"assessments": assessments}

@app.get("/api/assessments/{assessment_id}")
async def get_assessment(assessment_id: int):
    """Get assessment details"""
    assessment = db.get_assessment(assessment_id)
    if not assessment:
        raise HTTPException(status_code=404, detail="Assessment not found")
    return {"assessment": assessment}

@app.put("/api/assessments/{assessment_id}/complete")
async def complete_assessment(assessment_id: int):
    """Mark assessment as complete"""
    assessment = db.get_assessment(assessment_id)
    if not assessment:
        raise HTTPException(status_code=404, detail="Assessment not found")
    
    # Calculate scores before completing
    db.calculate_assessment_scores(assessment_id)
    db.complete_assessment(assessment_id)
    
    return {"message": "Assessment completed successfully"}

@app.get("/api/domains")
async def get_domains():
    """Get all domains"""
    domains = db.get_domains()
    return {"domains": domains}

@app.get("/api/domains/{domain_id}/aspects")
async def get_domain_aspects(domain_id: int):
    """Get aspects for a domain"""
    aspects = db.get_domain_aspects(domain_id)
    return {"aspects": aspects}

@app.get("/api/aspects/{aspect_id}/questions")
async def get_aspect_questions(aspect_id: str):
    """Get questions for an aspect"""
    questions = db.get_aspect_questions(aspect_id)
    return {"questions": questions}

@app.get("/api/assessments/{assessment_id}/answers")
async def get_assessment_answers(assessment_id: int):
    """Get all answers for an assessment"""
    assessment = db.get_assessment(assessment_id)
    if not assessment:
        raise HTTPException(status_code=404, detail="Assessment not found")
    
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
    return {"message": "Answer saved successfully"}

@app.get("/api/assessments/{assessment_id}/scores")
async def get_assessment_scores(assessment_id: int):
    """Get assessment scores"""
    assessment = db.get_assessment(assessment_id)
    if not assessment:
        raise HTTPException(status_code=404, detail="Assessment not found")
    
    scores = db.get_assessment_scores(assessment_id)
    return {"scores": scores}

@app.get("/api/assessments/{assessment_id}/radar-data")
async def get_radar_chart_data(assessment_id: int):
    """Get radar chart data for assessment"""
    assessment = db.get_assessment(assessment_id)
    if not assessment:
        raise HTTPException(status_code=404, detail="Assessment not found")
    
    radar_data = db.get_radar_chart_data(assessment_id)
    return {"radar_data": radar_data}

@app.get("/api/customers/{customer_id}/progress")
async def get_customer_progress(customer_id: int):
    """Get progress over time for a customer"""
    assessments = db.get_customer_assessments(customer_id)
    
    progress_data = []
    for assessment in assessments:
        if assessment['status'] == 'completed':
            radar_data = db.get_radar_chart_data(assessment['id'])
            progress_data.append({
                'assessment_id': assessment['id'],
                'name': assessment['name'],
                'completed_at': assessment['completed_at'],
                'radar_data': radar_data
            })
    
    return {"progress": progress_data}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8400)

