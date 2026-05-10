# API (quick reference)

Base URL: `http://localhost:8400` (override the port via `PORT`).

## Models
- `CustomerCreate`: `{ name: str, email?: str, organization?: str }`
- `AssessmentCreate`: `{ customer_id: int, name?: str }`
- `AnswerSubmit`: `{ assessment_id: int, question_id: int, answer_option_id?: int, answer_text?: str }`

## Web pages
- `GET /` — Home
- `GET /customers` — Customers page
- `GET /assessment/{assessment_id}` — Questionnaire
- `GET /results/{assessment_id}` — Results

## REST API
- `POST /api/customers` — Create a customer
- `GET  /api/customers` — List customers
- `GET  /api/customers/{customer_id}` — Customer details
- `POST /api/assessments` — Create an assessment
- `GET  /api/customers/{customer_id}/assessments` — Customer's assessments
- `GET  /api/assessments/{assessment_id}` — Assessment details
- `PUT  /api/assessments/{assessment_id}/complete` — Complete assessment
- `GET  /api/domains` — SOC-CMM domains
- `GET  /api/domains/{domain_id}/aspects` — Domain's aspects
- `GET  /api/aspects/{aspect_id}/questions` — Aspect's questions
- `POST /api/answers` — Submit an answer
- `GET  /api/assessments/{assessment_id}/answers` — Assessment answers
- `GET  /api/assessments/{assessment_id}/scores` — Scores
- `GET  /api/assessments/{assessment_id}/radar-data` — Radar chart data
- `GET  /api/customers/{customer_id}/progress` — Customer progress

Status codes: 200/201 success; 400/404/422/500 errors.

For complete details, see `API_DOCUMENTATION.md` at the repository root or
the live Swagger UI at `/docs`.
