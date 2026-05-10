# SOC CMM Assessment MCP Server

A Python Model Context Protocol (MCP) server that provides AI models with tools to interact with the SOC CMM Assessment System API.

## Overview

This MCP server enables AI models to:
- ✅ **Identify customers** by ID, name, or email
- ✅ **Get assessments in progress** for any customer
- ✅ **Create new customers** with contact information
- ✅ **Create assessments** for existing customers
- ✅ **Request next questions** from the assessment questionnaire
- ✅ **Register answers** to assessment questions
- ✅ **Track assessment progress** and completion status
- ✅ **Complete assessments** and calculate maturity scores
- ✅ **Retrieve assessment results** and analytics

## Architecture

```
AI Model/Client
       ↓
   MCP Server (mcp_server.py)
       ↓
   SOC CMM API (main.py)
       ↓
   SQLite Database (soc_cmm_translated.db)
```

## Installation

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure the environment** (the API refuses to start without
   `SECRET_KEY`):
   ```bash
   cp .env.example .env
   # edit .env: set SECRET_KEY and ADMIN_PASSWORD
   ```

3. **Run the bootstrap migration** (first time only):
   ```bash
   export ADMIN_PASSWORD="strong-password"
   python migrate_to_auth.py
   ```

4. **Start the API server**:
   ```bash
   python main.py
   # default port: 8400 — override with PORT=9000 python main.py
   ```
   The API will be available at `http://localhost:8400` (or your custom port).

5. **Test the setup**:
   ```bash
   python test_mcp_server.py
   ```

## Usage

### Running the MCP Server

```bash
python mcp_server.py
```

### Configuration

The MCP server can be configured via environment variables:
- `API_BASE_URL`: Base URL of the SOC CMM API (default: `http://localhost:8400`).
  If you changed the API's `PORT`, update `API_BASE_URL` accordingly.

> **Note on authentication:** the SOC CMM API requires user authentication
> (JWT). The MCP server currently targets a locally trusted deployment and
> does not negotiate JWTs on behalf of the AI model. For multi-user
> deployments, run the API behind an authenticated proxy or extend the MCP
> server to forward an `Authorization: Bearer <token>` header.

### MCP Client Configuration

Use the provided `mcp_config.json` file to configure your MCP client:

```json
{
  "mcpServers": {
    "soc-cmm-assessment": {
      "command": "python",
      "args": ["mcp_server.py"],
      "env": {
        "API_BASE_URL": "http://localhost:8400"
      }
    }
  }
}
```

## Available Tools

### 1. identify_customer
Identify a customer by ID, name, or email address.

**Parameters:**
- `customer_id` (int): Customer ID to identify
- `name` (str): Customer name to search for
- `email` (str): Customer email to search for

**Example:**
```json
{
  "name": "identify_customer",
  "arguments": {
    "customer_id": 1
  }
}
```

### 2. get_assessments_in_progress
Get all assessments currently in progress for a customer.

**Parameters:**
- `customer_id` (int): Customer ID to get assessments for

**Example:**
```json
{
  "name": "get_assessments_in_progress",
  "arguments": {
    "customer_id": 1
  }
}
```

### 3. create_customer
Create a new customer record.

**Parameters:**
- `name` (str): Customer name (required)
- `email` (str): Customer email (optional)
- `organization` (str): Customer organization (optional)

**Example:**
```json
{
  "name": "create_customer",
  "arguments": {
    "name": "John Doe",
    "email": "john@example.com",
    "organization": "Example Corp"
  }
}
```

### 4. create_assessment
Create a new assessment for an existing customer.

**Parameters:**
- `customer_id` (int): Customer ID for the assessment
- `name` (str): Assessment name (optional)

**Example:**
```json
{
  "name": "create_assessment",
  "arguments": {
    "customer_id": 1,
    "name": "Q1 2024 Assessment"
  }
}
```

### 5. get_next_questions
Get the next questions for an assessment, optionally filtered by domain or aspect.

**Parameters:**
- `assessment_id` (int): Assessment ID to get questions for
- `domain_id` (int): Domain ID (optional)
- `aspect_id` (str): Aspect ID (optional)

**Example:**
```json
{
  "name": "get_next_questions",
  "arguments": {
    "assessment_id": 1,
    "domain_id": 1
  }
}
```

### 6. register_answer
Register an answer for a specific question in an assessment.

**Parameters:**
- `assessment_id` (int): Assessment ID
- `question_id` (int): Question ID
- `answer_option_id` (int): Answer option ID for multiple choice questions
- `answer_text` (str): Answer text for open-ended questions

**Example:**
```json
{
  "name": "register_answer",
  "arguments": {
    "assessment_id": 1,
    "question_id": 15,
    "answer_option_id": 3
  }
}
```

### 7. get_assessment_progress
Get detailed progress information for an assessment.

**Parameters:**
- `assessment_id` (int): Assessment ID to get progress for

**Example:**
```json
{
  "name": "get_assessment_progress",
  "arguments": {
    "assessment_id": 1
  }
}
```

### 8. complete_assessment
Mark an assessment as complete and calculate maturity scores.

**Parameters:**
- `assessment_id` (int): Assessment ID to complete

**Example:**
```json
{
  "name": "complete_assessment",
  "arguments": {
    "assessment_id": 1
  }
}
```

### 9. get_assessment_results
Get detailed results and scores for a completed assessment.

**Parameters:**
- `assessment_id` (int): Assessment ID to get results for

**Example:**
```json
{
  "name": "get_assessment_results",
  "arguments": {
    "assessment_id": 1
  }
}
```

## SOC CMM Assessment Model

The system implements the **SOC-CMM®** framework by Rob van Os
(<https://www.soc-cmm.com>):

### Maturity Levels
1. **Level 1 — Initial**: Ad-hoc, unstructured processes
2. **Level 2 — Developing**: Basic documented processes
3. **Level 3 — Defined**: Standardised processes across the organisation
4. **Level 4 — Managed**: Metrics-driven processes
5. **Level 5 — Optimised**: Continuous improvement processes

### Domains
The assessment covers the six SOC-CMM® domains:
- **Business** — strategy, governance, cost management, privacy
- **People** — employment, training, performance, knowledge management
- **Process** — management, operations, reporting, use case management
- **Technology** — security information management, detection, analytics
- **Services** — service catalogue, threat hunting, vulnerability management
- **Results** — overview, critical success factors, sharing

### Assessment Flow
1. **Customer Registration**: Create customer profile
2. **Assessment Creation**: Initialize new assessment
3. **Question Answering**: Progressive questionnaire completion
4. **Progress Tracking**: Monitor completion status
5. **Results Generation**: Calculate maturity scores
6. **Analytics**: Radar charts and trend analysis

## Error Handling

The MCP server includes comprehensive error handling:
- **HTTP errors**: Network and API communication issues
- **Validation errors**: Invalid input parameters
- **Database errors**: Data persistence issues
- **Authentication errors**: API access problems

All errors are logged and returned as descriptive error messages to the client.

## Testing

Run the test suite to validate functionality:

```bash
python test_mcp_server.py
```

The test script validates:
- ✅ API connectivity
- ✅ Customer creation and identification
- ✅ Assessment creation and management
- ✅ Question retrieval and answering
- ✅ Progress tracking and completion
- ✅ Results generation and analytics

## Security Considerations

- **API Access**: Server runs on localhost by default
- **Input Validation**: All parameters are validated
- **Error Isolation**: Errors don't expose sensitive information
- **Database Security**: SQLite database with proper permissions

## Troubleshooting

### Common Issues

1. **API Connection Failed**
   - Ensure `main.py` is running on port 8400
   - Check `API_BASE_URL` environment variable

2. **Import Errors**
   - Install all dependencies: `pip install -r requirements.txt`
   - Verify Python version compatibility

3. **Database Errors**
   - Ensure `soc_cmm_translated.db` exists and is accessible
   - Re-run `python migrate_to_auth.py` if the `users` table is missing
   - Check database permissions

4. **MCP Client Issues**
   - Verify `mcp_config.json` configuration
   - Check MCP client compatibility

### Debug Mode

Enable debug logging by setting the log level:

```python
logging.basicConfig(level=logging.DEBUG)
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Implement changes with tests
4. Submit a pull request

## License

This project is distributed under the **Creative Commons
Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)** license — the
same license used by the SOC-CMM® framework on which it is based. See
[`LICENSE`](LICENSE) and [`NOTICE`](NOTICE) at the repository root for the
full attribution text.

> "SOC-CMM" is a trademark of Rob van Os. This project is **not affiliated
> with or endorsed by** Rob van Os or soc-cmm.com.

## Support

For issues and questions:
- Check the API documentation: [`API_DOCUMENTATION.md`](API_DOCUMENTATION.md)
- Run the test suite: `python test_mcp_server.py`
- Review the main README: [`README.md`](README.md)
- Bilingual user docs: [`docs/en/`](docs/en/README.md) /
  [`docs/pt-br/`](docs/pt-br/README.md)