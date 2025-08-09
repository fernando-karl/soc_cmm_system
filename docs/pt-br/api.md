# API (Referência Rápida)

Base URL: `http://localhost:8400`

## Modelos
- CustomerCreate: `{ name: str, email?: str, organization?: str }`
- AssessmentCreate: `{ customer_id: int, name?: str }`
- AnswerSubmit: `{ assessment_id: int, question_id: int, answer_option_id?: int, answer_text?: str }`

## Web
- GET `/` — Home
- GET `/customers` — Página de clientes
- GET `/assessment/{assessment_id}` — Questionário
- GET `/results/{assessment_id}` — Resultados

## API
- POST `/api/customers` — Criar cliente
- GET `/api/customers` — Listar clientes
- GET `/api/customers/{customer_id}` — Detalhar cliente
- POST `/api/assessments` — Criar avaliação
- GET `/api/customers/{customer_id}/assessments` — Avaliações do cliente
- GET `/api/assessments/{assessment_id}` — Detalhar avaliação
- PUT `/api/assessments/{assessment_id}/complete` — Concluir avaliação
- GET `/api/domains` — Domínios SOC CMM
- GET `/api/domains/{domain_id}/aspects` — Aspectos do domínio
- GET `/api/aspects/{aspect_id}/questions` — Questões do aspecto
- POST `/api/answers` — Submeter resposta
- GET `/api/assessments/{assessment_id}/answers` — Respostas da avaliação
- GET `/api/assessments/{assessment_id}/scores` — Pontuações
- GET `/api/assessments/{assessment_id}/radar-data` — Dados para gráfico
- GET `/api/customers/{customer_id}/progress` — Progresso por cliente

Códigos: 200/201 sucesso; 400/404/422/500 erros.

Para detalhes completos, consulte `API_DOCUMENTATION.md` no repositório.