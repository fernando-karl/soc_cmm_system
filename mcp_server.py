#!/usr/bin/env python3
"""
SOC CMM Assessment MCP Server

Servidor MCP em Python para interação com a API do SOC CMM.
Permite a modelos de IA:
- Identificar clientes
- Obter avaliações em andamento
- Criar clientes
- Criar avaliações
- Solicitar próximas questões
- Registrar respostas
"""

import asyncio
import json
import logging
from typing import Any, Dict, List, Optional, Sequence
from urllib.parse import urljoin

import httpx
from mcp.server import Server
from mcp.server.models import InitializationOptions
from mcp.server.stdio import stdio_server
from mcp.types import (
    CallToolRequest,
    CallToolResult,
    ListToolsRequest,
    ListToolsResult,
    Tool,
    TextContent,
    ImageContent,
    EmbeddedResource,
)
from pydantic import BaseModel, Field

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration
API_BASE_URL = "http://localhost:8400"
TIMEOUT = 30.0

class ApiClient:
    """HTTP client for the SOC CMM Assessment API"""
    
    def __init__(self, base_url: str = API_BASE_URL):
        self.base_url = base_url
        self.client = httpx.AsyncClient(timeout=TIMEOUT)
    
    async def get(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        """Make GET request to API"""
        url = urljoin(self.base_url, endpoint)
        try:
            response = await self.client.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            logger.error(f"HTTP error calling {url}: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error calling {url}: {e}")
            raise
    
    async def post(self, endpoint: str, data: Dict) -> Dict:
        """Make POST request to API"""
        url = urljoin(self.base_url, endpoint)
        try:
            response = await self.client.post(url, json=data)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            logger.error(f"HTTP error calling {url}: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error calling {url}: {e}")
            raise
    
    async def put(self, endpoint: str, data: Optional[Dict] = None) -> Dict:
        """Make PUT request to API"""
        url = urljoin(self.base_url, endpoint)
        try:
            response = await self.client.put(url, json=data)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            logger.error(f"HTTP error calling {url}: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error calling {url}: {e}")
            raise
    
    async def close(self):
        """Close the HTTP client"""
        await self.client.aclose()

# Initialize API client
api_client = ApiClient()

# Initialize MCP server
server = Server("soc-cmm-assessment")

@server.list_tools()
async def handle_list_tools() -> ListToolsResult:
    """List available tools"""
    return ListToolsResult(
        tools=[
            Tool(
                name="identify_customer",
                description="Identify a customer by ID, name, or email",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "integer",
                            "description": "Customer ID to identify"
                        },
                        "name": {
                            "type": "string",
                            "description": "Customer name to search for"
                        },
                        "email": {
                            "type": "string",
                            "description": "Customer email to search for"
                        }
                    },
                    "oneOf": [
                        {"required": ["customer_id"]},
                        {"required": ["name"]},
                        {"required": ["email"]}
                    ]
                }
            ),
            Tool(
                name="get_assessments_in_progress",
                description="Get all assessments in progress for a customer",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "integer",
                            "description": "Customer ID to get assessments for"
                        }
                    },
                    "required": ["customer_id"]
                }
            ),
            Tool(
                name="create_customer",
                description="Create a new customer",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Customer name"
                        },
                        "email": {
                            "type": "string",
                            "description": "Customer email (optional)"
                        },
                        "organization": {
                            "type": "string",
                            "description": "Customer organization (optional)"
                        }
                    },
                    "required": ["name"]
                }
            ),
            Tool(
                name="create_assessment",
                description="Create a new assessment for a customer",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "integer",
                            "description": "Customer ID for the assessment"
                        },
                        "name": {
                            "type": "string",
                            "description": "Assessment name (optional)"
                        }
                    },
                    "required": ["customer_id"]
                }
            ),
            Tool(
                name="get_next_questions",
                description="Get next questions for an assessment based on domain and aspect",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "assessment_id": {
                            "type": "integer",
                            "description": "Assessment ID to get questions for"
                        },
                        "domain_id": {
                            "type": "integer",
                            "description": "Domain ID (optional - if not provided, returns all domains)"
                        },
                        "aspect_id": {
                            "type": "string",
                            "description": "Aspect ID (optional - if not provided, returns all aspects for domain)"
                        }
                    },
                    "required": ["assessment_id"]
                }
            ),
            Tool(
                name="register_answer",
                description="Register an answer for a question in an assessment",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "assessment_id": {
                            "type": "integer",
                            "description": "Assessment ID"
                        },
                        "question_id": {
                            "type": "integer",
                            "description": "Question ID"
                        },
                        "answer_option_id": {
                            "type": "integer",
                            "description": "Answer option ID for multiple choice questions"
                        },
                        "answer_text": {
                            "type": "string",
                            "description": "Answer text for open-ended questions"
                        }
                    },
                    "required": ["assessment_id", "question_id"]
                }
            ),
            Tool(
                name="get_assessment_progress",
                description="Get progress information for an assessment",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "assessment_id": {
                            "type": "integer",
                            "description": "Assessment ID to get progress for"
                        }
                    },
                    "required": ["assessment_id"]
                }
            ),
            Tool(
                name="complete_assessment",
                description="Mark an assessment as complete and calculate scores",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "assessment_id": {
                            "type": "integer",
                            "description": "Assessment ID to complete"
                        }
                    },
                    "required": ["assessment_id"]
                }
            ),
            Tool(
                name="get_assessment_results",
                description="Get detailed results and scores for a completed assessment",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "assessment_id": {
                            "type": "integer",
                            "description": "Assessment ID to get results for"
                        }
                    },
                    "required": ["assessment_id"]
                }
            )
        ]
    )

@server.call_tool()
async def handle_call_tool(name: str, arguments: Dict[str, Any]) -> CallToolResult:
    """Handle tool calls"""
    try:
        if name == "identify_customer":
            return await identify_customer(arguments)
        elif name == "get_assessments_in_progress":
            return await get_assessments_in_progress(arguments)
        elif name == "create_customer":
            return await create_customer(arguments)
        elif name == "create_assessment":
            return await create_assessment(arguments)
        elif name == "get_next_questions":
            return await get_next_questions(arguments)
        elif name == "register_answer":
            return await register_answer(arguments)
        elif name == "get_assessment_progress":
            return await get_assessment_progress(arguments)
        elif name == "complete_assessment":
            return await complete_assessment(arguments)
        elif name == "get_assessment_results":
            return await get_assessment_results(arguments)
        else:
            raise ValueError(f"Unknown tool: {name}")
    except Exception as e:
        logger.error(f"Error in tool {name}: {e}")
        return CallToolResult(
            content=[TextContent(type="text", text=f"Error: {str(e)}")]
        )

async def identify_customer(arguments: Dict[str, Any]) -> CallToolResult:
    """Identify a customer by ID, name, or email"""
    try:
        if "customer_id" in arguments:
            # Get customer by ID
            customer_data = await api_client.get(f"/api/customers/{arguments['customer_id']}")
            customer = customer_data.get("customer")
            if customer:
                return CallToolResult(
                    content=[TextContent(
                        type="text",
                        text=f"Customer found:\n{json.dumps(customer, indent=2)}"
                    )]
                )
            else:
                return CallToolResult(
                    content=[TextContent(type="text", text="Customer not found")]
                )
        else:
            # Search by name or email
            customers_data = await api_client.get("/api/customers")
            customers = customers_data.get("customers", [])
            
            search_term = arguments.get("name") or arguments.get("email")
            search_field = "name" if "name" in arguments else "email"
            
            if not search_term:
                return CallToolResult(
                    content=[TextContent(type="text", text="Search term is required")]
                )
            
            found_customers = []
            for customer in customers:
                customer_value = customer.get(search_field)
                if customer_value and search_term.lower() in customer_value.lower():
                    found_customers.append(customer)
            
            if found_customers:
                return CallToolResult(
                    content=[TextContent(
                        type="text",
                        text=f"Found {len(found_customers)} customer(s):\n{json.dumps(found_customers, indent=2)}"
                    )]
                )
            else:
                return CallToolResult(
                    content=[TextContent(type="text", text=f"No customers found matching {search_field}: {search_term}")]
                )
    except Exception as e:
        raise Exception(f"Failed to identify customer: {str(e)}")

async def get_assessments_in_progress(arguments: Dict[str, Any]) -> CallToolResult:
    """Get assessments in progress for a customer"""
    try:
        customer_id = arguments["customer_id"]
        assessments_data = await api_client.get(f"/api/customers/{customer_id}/assessments")
        assessments = assessments_data.get("assessments", [])
        
        # Filter for in-progress assessments
        in_progress = [a for a in assessments if a.get("status") == "in_progress"]
        
        return CallToolResult(
            content=[TextContent(
                type="text",
                text=f"Found {len(in_progress)} assessment(s) in progress:\n{json.dumps(in_progress, indent=2)}"
            )]
        )
    except Exception as e:
        raise Exception(f"Failed to get assessments in progress: {str(e)}")

async def create_customer(arguments: Dict[str, Any]) -> CallToolResult:
    """Create a new customer"""
    try:
        customer_data = {
            "name": arguments["name"],
            "email": arguments.get("email"),
            "organization": arguments.get("organization")
        }
        
        result = await api_client.post("/api/customers", customer_data)
        
        return CallToolResult(
            content=[TextContent(
                type="text",
                text=f"Customer created successfully:\n{json.dumps(result, indent=2)}"
            )]
        )
    except Exception as e:
        raise Exception(f"Failed to create customer: {str(e)}")

async def create_assessment(arguments: Dict[str, Any]) -> CallToolResult:
    """Create a new assessment"""
    try:
        assessment_data = {
            "customer_id": arguments["customer_id"],
            "name": arguments.get("name")
        }
        
        result = await api_client.post("/api/assessments", assessment_data)
        
        return CallToolResult(
            content=[TextContent(
                type="text",
                text=f"Assessment created successfully:\n{json.dumps(result, indent=2)}"
            )]
        )
    except Exception as e:
        raise Exception(f"Failed to create assessment: {str(e)}")

async def get_next_questions(arguments: Dict[str, Any]) -> CallToolResult:
    """Get next questions for an assessment"""
    try:
        assessment_id = arguments["assessment_id"]
        
        # First verify the assessment exists
        assessment_data = await api_client.get(f"/api/assessments/{assessment_id}")
        assessment = assessment_data.get("assessment")
        
        if not assessment:
            return CallToolResult(
                content=[TextContent(type="text", text="Assessment not found")]
            )
        
        # Get existing answers to determine what's already answered
        answers_data = await api_client.get(f"/api/assessments/{assessment_id}/answers")
        answered_question_ids = set(answer["question_id"] for answer in answers_data.get("answers", []))
        
        if "aspect_id" in arguments:
            # Get questions for specific aspect
            aspect_id = arguments["aspect_id"]
            questions_data = await api_client.get(f"/api/aspects/{aspect_id}/questions")
            questions = questions_data.get("questions", [])
            
            # Filter out already answered questions
            unanswered_questions = [q for q in questions if q["id"] not in answered_question_ids]
            
            return CallToolResult(
                content=[TextContent(
                    type="text",
                    text=f"Found {len(unanswered_questions)} unanswered question(s) for aspect {aspect_id}:\n{json.dumps(unanswered_questions, indent=2)}"
                )]
            )
        elif "domain_id" in arguments:
            # Get aspects for domain, then questions
            domain_id = arguments["domain_id"]
            aspects_data = await api_client.get(f"/api/domains/{domain_id}/aspects")
            aspects = aspects_data.get("aspects", [])
            
            all_questions = []
            for aspect in aspects:
                questions_data = await api_client.get(f"/api/aspects/{aspect['id']}/questions")
                questions = questions_data.get("questions", [])
                all_questions.extend(questions)
            
            # Filter out already answered questions
            unanswered_questions = [q for q in all_questions if q["id"] not in answered_question_ids]
            
            return CallToolResult(
                content=[TextContent(
                    type="text",
                    text=f"Found {len(unanswered_questions)} unanswered question(s) for domain {domain_id}:\n{json.dumps(unanswered_questions, indent=2)}"
                )]
            )
        else:
            # Get all domains and their questions
            domains_data = await api_client.get("/api/domains")
            domains = domains_data.get("domains", [])
            
            all_questions = []
            for domain in domains:
                aspects_data = await api_client.get(f"/api/domains/{domain['id']}/aspects")
                aspects = aspects_data.get("aspects", [])
                
                for aspect in aspects:
                    questions_data = await api_client.get(f"/api/aspects/{aspect['id']}/questions")
                    questions = questions_data.get("questions", [])
                    all_questions.extend(questions)
            
            # Filter out already answered questions
            unanswered_questions = [q for q in all_questions if q["id"] not in answered_question_ids]
            
            return CallToolResult(
                content=[TextContent(
                    type="text",
                    text=f"Found {len(unanswered_questions)} unanswered question(s) total:\n{json.dumps(unanswered_questions, indent=2)}"
                )]
            )
    except Exception as e:
        raise Exception(f"Failed to get next questions: {str(e)}")

async def register_answer(arguments: Dict[str, Any]) -> CallToolResult:
    """Register an answer for a question"""
    try:
        answer_data = {
            "assessment_id": arguments["assessment_id"],
            "question_id": arguments["question_id"],
            "answer_option_id": arguments.get("answer_option_id"),
            "answer_text": arguments.get("answer_text")
        }
        
        result = await api_client.post("/api/answers", answer_data)
        
        return CallToolResult(
            content=[TextContent(
                type="text",
                text=f"Answer registered successfully:\n{json.dumps(result, indent=2)}"
            )]
        )
    except Exception as e:
        raise Exception(f"Failed to register answer: {str(e)}")

async def get_assessment_progress(arguments: Dict[str, Any]) -> CallToolResult:
    """Get progress information for an assessment"""
    try:
        assessment_id = arguments["assessment_id"]
        
        # Get assessment details
        assessment_data = await api_client.get(f"/api/assessments/{assessment_id}")
        assessment = assessment_data.get("assessment")
        
        if not assessment:
            return CallToolResult(
                content=[TextContent(type="text", text="Assessment not found")]
            )
        
        # Get answers
        answers_data = await api_client.get(f"/api/assessments/{assessment_id}/answers")
        answers = answers_data.get("answers", [])
        
        # Get total questions count
        domains_data = await api_client.get("/api/domains")
        domains = domains_data.get("domains", [])
        
        total_questions = 0
        for domain in domains:
            aspects_data = await api_client.get(f"/api/domains/{domain['id']}/aspects")
            aspects = aspects_data.get("aspects", [])
            
            for aspect in aspects:
                questions_data = await api_client.get(f"/api/aspects/{aspect['id']}/questions")
                questions = questions_data.get("questions", [])
                total_questions += len(questions)
        
        answered_questions = len(answers)
        progress_percentage = (answered_questions / total_questions * 100) if total_questions > 0 else 0
        
        progress_info = {
            "assessment": assessment,
            "answered_questions": answered_questions,
            "total_questions": total_questions,
            "progress_percentage": round(progress_percentage, 2),
            "status": assessment.get("status")
        }
        
        return CallToolResult(
            content=[TextContent(
                type="text",
                text=f"Assessment progress:\n{json.dumps(progress_info, indent=2)}"
            )]
        )
    except Exception as e:
        raise Exception(f"Failed to get assessment progress: {str(e)}")

async def complete_assessment(arguments: Dict[str, Any]) -> CallToolResult:
    """Complete an assessment and calculate scores"""
    try:
        assessment_id = arguments["assessment_id"]
        
        result = await api_client.put(f"/api/assessments/{assessment_id}/complete")
        
        return CallToolResult(
            content=[TextContent(
                type="text",
                text=f"Assessment completed successfully:\n{json.dumps(result, indent=2)}"
            )]
        )
    except Exception as e:
        raise Exception(f"Failed to complete assessment: {str(e)}")

async def get_assessment_results(arguments: Dict[str, Any]) -> CallToolResult:
    """Get detailed results for a completed assessment"""
    try:
        assessment_id = arguments["assessment_id"]
        
        # Get assessment details
        assessment_data = await api_client.get(f"/api/assessments/{assessment_id}")
        assessment = assessment_data.get("assessment")
        
        if not assessment:
            return CallToolResult(
                content=[TextContent(type="text", text="Assessment not found")]
            )
        
        # Get scores
        scores_data = await api_client.get(f"/api/assessments/{assessment_id}/scores")
        scores = scores_data.get("scores", {})
        
        # Get radar chart data
        radar_data = await api_client.get(f"/api/assessments/{assessment_id}/radar-data")
        
        results = {
            "assessment": assessment,
            "scores": scores,
            "radar_data": radar_data.get("radar_data", {})
        }
        
        return CallToolResult(
            content=[TextContent(
                type="text",
                text=f"Assessment results:\n{json.dumps(results, indent=2)}"
            )]
        )
    except Exception as e:
        raise Exception(f"Failed to get assessment results: {str(e)}")

async def main():
    """Main function to run the MCP server"""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="soc-cmm-assessment",
                server_version="1.0.0",
                capabilities=server.get_capabilities(
                    notification_options=None,
                    experimental_capabilities=None,
                ),
            ),
        )

if __name__ == "__main__":
    asyncio.run(main())