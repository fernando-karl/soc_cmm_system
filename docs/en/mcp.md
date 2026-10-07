# MCP (Model Context Protocol)

A Python MCP server that lets AI models drive the SOC CMM API.

## How to use
1. Install dependencies: `pip install -r requirements.txt`
2. Start the API: `python main.py`
3. Run the MCP server: `python mcp_server.py`

Configuration lives in `mcp_config.json` (`API_BASE_URL`).

## Available tools
1. `identify_customer` — identify a customer by ID, name or email
2. `get_assessments_in_progress` — return in-progress assessments for a customer
3. `create_customer` — create a customer
4. `create_assessment` — create an assessment
5. `get_next_questions` — return upcoming questions (per domain/aspect)
6. `register_answer` — store an answer
7. `get_assessment_progress` — assessment progress
8. `complete_assessment` — finalise an assessment and compute scores
9. `get_assessment_results` — results and analytics

Errors are returned with descriptive messages and logged.

See `MCP_README.md` and `MCP_IMPLEMENTATION_SUMMARY.md` at the repository
root for the full reference.

## Authentication

The customer and assessment endpoints require authentication, so the MCP
server needs a bearer token. Obtain one from `POST /api/auth/login` and pass
it as `API_TOKEN`:

```bash
export API_TOKEN='<token from /api/auth/login>'
export API_BASE_URL='http://localhost:8400'   # optional, this is the default
python mcp_server.py
```

Without `API_TOKEN` the server starts but logs a warning, and every customer or
assessment call fails with 401. The token carries the permissions of the user it
was issued to, so the MCP server only ever sees that user's data.
