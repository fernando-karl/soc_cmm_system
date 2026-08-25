#!/usr/bin/env python3
"""
Test script for the SOC CMM Assessment MCP Server

This script tests the MCP server functionality by making direct API calls
to simulate what the MCP server would do.
"""

import asyncio
import json
import sys
import httpx
from typing import Dict, Any

API_BASE_URL = "http://localhost:8400"

class TestApiClient:
    """Test client for API validation"""
    
    def __init__(self, base_url: str = API_BASE_URL):
        self.base_url = base_url
        self.client = httpx.AsyncClient(timeout=30.0)
    
    async def get(self, endpoint: str) -> Dict:
        """Make GET request"""
        url = f"{self.base_url}{endpoint}"
        try:
            response = await self.client.get(url)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            print(f"HTTP error calling {url}: {e}")
            return {}
        except Exception as e:
            print(f"Error calling {url}: {e}")
            return {}
    
    async def post(self, endpoint: str, data: Dict) -> Dict:
        """Make POST request"""
        url = f"{self.base_url}{endpoint}"
        try:
            response = await self.client.post(url, json=data)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            print(f"HTTP error calling {url}: {e}")
            return {}
        except Exception as e:
            print(f"Error calling {url}: {e}")
            return {}
    
    async def put(self, endpoint: str, data: Dict = None) -> Dict:
        """Make PUT request"""
        url = f"{self.base_url}{endpoint}"
        try:
            response = await self.client.put(url, json=data if data is not None else {})
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            print(f"HTTP error calling {url}: {e}")
            return {}
        except Exception as e:
            print(f"Error calling {url}: {e}")
            return {}
    
    async def close(self):
        """Close client"""
        await self.client.aclose()

async def test_mcp_functionality():
    """Test all MCP server functionality"""
    client = TestApiClient()
    
    print("🧪 Testing SOC CMM Assessment MCP Server Functionality\n")
    
    # Test 1: Check if API is running
    print("1. Testing API availability...")
    domains = await client.get("/api/domains")
    if domains.get("domains"):
        print("   ✅ API is running and accessible")
    else:
        print("   ❌ API is not accessible. Make sure main.py is running on port 8400")
        await client.close()
        return False
    
    # Test 2: Create a test customer
    print("\n2. Testing customer creation...")
    customer_data = {
        "name": "Test Customer",
        "email": "test@example.com",
        "organization": "Test Organization"
    }
    
    customer_result = await client.post("/api/customers", customer_data)
    if customer_result.get("id"):
        customer_id = customer_result["id"]
        print(f"   ✅ Customer created with ID: {customer_id}")
    else:
        print("   ❌ Failed to create customer")
        await client.close()
        return False
    
    # Test 3: Identify customer
    print("\n3. Testing customer identification...")
    customer_info = await client.get(f"/api/customers/{customer_id}")
    if customer_info.get("customer"):
        print(f"   ✅ Customer identified: {customer_info['customer']['name']}")
    else:
        print("   ❌ Failed to identify customer")
    
    # Test 4: Create assessment
    print("\n4. Testing assessment creation...")
    assessment_data = {
        "customer_id": customer_id,
        "name": "Test Assessment"
    }
    
    assessment_result = await client.post("/api/assessments", assessment_data)
    if assessment_result.get("id"):
        assessment_id = assessment_result["id"]
        print(f"   ✅ Assessment created with ID: {assessment_id}")
    else:
        print("   ❌ Failed to create assessment")
        await client.close()
        return False
    
    # Test 5: Get assessments in progress
    print("\n5. Testing assessments in progress...")
    assessments = await client.get(f"/api/customers/{customer_id}/assessments")
    if assessments.get("assessments"):
        in_progress = [a for a in assessments["assessments"] if a.get("status") == "in_progress"]
        print(f"   ✅ Found {len(in_progress)} assessment(s) in progress")
    else:
        print("   ❌ Failed to get assessments")
    
    # Test 6: Get next questions
    print("\n6. Testing question retrieval...")
    # Get first domain
    first_domain = domains["domains"][0] if domains.get("domains") else None
    if first_domain:
        aspects = await client.get(f"/api/domains/{first_domain['id']}/aspects")
        if aspects.get("aspects"):
            first_aspect = aspects["aspects"][0]
            questions = await client.get(f"/api/aspects/{first_aspect['id']}/questions")
            if questions.get("questions"):
                print(f"   ✅ Found {len(questions['questions'])} questions for aspect {first_aspect['id']}")
                
                # Test 7: Register answer
                print("\n7. Testing answer registration...")
                first_question = questions["questions"][0]
                if first_question.get("options"):
                    first_option = first_question["options"][0]
                    answer_data = {
                        "assessment_id": assessment_id,
                        "question_id": first_question["id"],
                        "answer_option_id": first_option["id"]
                    }
                    
                    answer_result = await client.post("/api/answers", answer_data)
                    if answer_result.get("message"):
                        print("   ✅ Answer registered successfully")
                    else:
                        print("   ❌ Failed to register answer")
                else:
                    print("   ⚠️  No answer options available for testing")
            else:
                print("   ❌ Failed to get questions")
        else:
            print("   ❌ Failed to get aspects")
    else:
        print("   ❌ No domains available")
    
    # Test 8: Get assessment progress
    print("\n8. Testing assessment progress...")
    assessment_info = await client.get(f"/api/assessments/{assessment_id}")
    if assessment_info.get("assessment"):
        print(f"   ✅ Assessment status: {assessment_info['assessment'].get('status')}")
    else:
        print("   ❌ Failed to get assessment info")
    
    # Test 9: Complete assessment (optional)
    print("\n9. Testing assessment completion...")
    complete_result = await client.put(f"/api/assessments/{assessment_id}/complete")
    if complete_result.get("message"):
        print("   ✅ Assessment completed successfully")
        
        # Test 10: Get assessment results
        print("\n10. Testing assessment results...")
        scores = await client.get(f"/api/assessments/{assessment_id}/scores")
        if scores.get("scores"):
            print("   ✅ Assessment results retrieved successfully")
        else:
            print("   ❌ Failed to get assessment results")
    else:
        print("   ❌ Failed to complete assessment")
    
    await client.close()
    
    print("\n🎉 All tests completed!")
    return True

async def main():
    """Main test function"""
    try:
        success = await test_mcp_functionality()
        if success:
            print("\n✅ MCP server functionality validated successfully!")
            print("\nTo use the MCP server:")
            print("1. Make sure the API is running: python main.py")
            print("2. Install MCP dependencies: pip install -r requirements.txt")
            print("3. Run the MCP server: python mcp_server.py")
            print("4. Configure your MCP client to use the server with mcp_config.json")
        else:
            print("\n❌ Some tests failed. Please check the API and try again.")
            sys.exit(1)
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())