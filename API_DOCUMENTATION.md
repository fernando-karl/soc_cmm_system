# API Documentation - SOC CMM Assessment System

## 📋 Visão Geral

O **SOC CMM Assessment System** é uma API desenvolvida com FastAPI que permite realizar avaliações de maturidade de Security Operations Center (SOC) baseadas no modelo CMM (Capability Maturity Model).

### 🔧 Tecnologias Utilizadas

- **FastAPI** 0.115.14 - Framework web moderno e de alta performance
- **SQLite** - Banco de dados
- **Pydantic** 2.11.7 - Validação de dados
- **Uvicorn** 0.35.0 - Servidor ASGI

### 🌐 Configuração

- **URL Base**: `http://localhost:8400`
- **Porta**: 8400
- **CORS**: Habilitado para todas as origens

---

## 📊 Modelos de Dados

### CustomerCreate
```python
{
    "name": str,           # Nome do cliente (obrigatório)
    "email": str,          # Email do cliente (opcional)
    "organization": str    # Organização do cliente (opcional)
}
```

### AssessmentCreate
```python
{
    "customer_id": int,    # ID do cliente (obrigatório)
    "name": str           # Nome da avaliação (opcional)
}
```

### AnswerSubmit
```python
{
    "assessment_id": int,     # ID da avaliação (obrigatório)
    "question_id": int,       # ID da questão (obrigatório)
    "answer_option_id": int,  # ID da opção de resposta (opcional)
    "answer_text": str        # Texto da resposta (opcional)
}
```

---

## 🌐 Rotas Web (Interface)

### 🏠 Página Principal
```
GET /
```
**Descrição**: Página inicial do sistema
**Retorno**: HTML da página principal

### 👥 Página de Clientes
```
GET /customers
```
**Descrição**: Página de gerenciamento de clientes
**Retorno**: HTML da página de clientes

### 📝 Página de Avaliação
```
GET /assessment/{assessment_id}
```
**Descrição**: Página do questionário de avaliação
**Parâmetros**:
- `assessment_id` (int): ID da avaliação
**Retorno**: HTML da página de avaliação

### 📊 Página de Resultados
```
GET /results/{assessment_id}
```
**Descrição**: Página de resultados da avaliação
**Parâmetros**:
- `assessment_id` (int): ID da avaliação
**Retorno**: HTML da página de resultados

---

## 🔌 API Endpoints

### 👥 Gerenciamento de Clientes

#### Criar Cliente
```
POST /api/customers
```
**Descrição**: Cria um novo cliente
**Body**:
```json
{
    "name": "João Silva",
    "email": "joao@empresa.com",
    "organization": "Empresa ABC"
}
```
**Resposta**:
```json
{
    "id": 1,
    "message": "Customer created successfully"
}
```

#### Listar Clientes
```
GET /api/customers
```
**Descrição**: Retorna lista de todos os clientes
**Resposta**:
```json
{
    "customers": [
        {
            "id": 1,
            "name": "João Silva",
            "email": "joao@empresa.com",
            "organization": "Empresa ABC",
            "created_at": "2024-01-01T10:00:00"
        }
    ]
}
```

#### Buscar Cliente
```
GET /api/customers/{customer_id}
```
**Descrição**: Retorna detalhes de um cliente específico
**Parâmetros**:
- `customer_id` (int): ID do cliente
**Resposta**:
```json
{
    "customer": {
        "id": 1,
        "name": "João Silva",
        "email": "joao@empresa.com",
        "organization": "Empresa ABC",
        "created_at": "2024-01-01T10:00:00"
    }
}
```

---

### 📋 Gerenciamento de Avaliações

#### Criar Avaliação
```
POST /api/assessments
```
**Descrição**: Cria uma nova avaliação para um cliente
**Body**:
```json
{
    "customer_id": 1,
    "name": "Avaliação SOC Q1 2024"
}
```
**Resposta**:
```json
{
    "id": 1,
    "message": "Assessment created successfully"
}
```

#### Listar Avaliações do Cliente
```
GET /api/customers/{customer_id}/assessments
```
**Descrição**: Retorna todas as avaliações de um cliente
**Parâmetros**:
- `customer_id` (int): ID do cliente
**Resposta**:
```json
{
    "assessments": [
        {
            "id": 1,
            "customer_id": 1,
            "name": "Avaliação SOC Q1 2024",
            "status": "in_progress",
            "started_at": "2024-01-01T10:00:00",
            "completed_at": null
        }
    ]
}
```

#### Buscar Avaliação
```
GET /api/assessments/{assessment_id}
```
**Descrição**: Retorna detalhes de uma avaliação específica
**Parâmetros**:
- `assessment_id` (int): ID da avaliação
**Resposta**:
```json
{
    "assessment": {
        "id": 1,
        "customer_id": 1,
        "name": "Avaliação SOC Q1 2024",
        "status": "in_progress",
        "started_at": "2024-01-01T10:00:00",
        "completed_at": null
    }
}
```

#### Completar Avaliação
```
PUT /api/assessments/{assessment_id}/complete
```
**Descrição**: Marca uma avaliação como concluída e calcula as pontuações
**Parâmetros**:
- `assessment_id` (int): ID da avaliação
**Resposta**:
```json
{
    "message": "Assessment completed successfully"
}
```

---

### 📚 Estrutura de Dados SOC CMM

#### Listar Domínios
```
GET /api/domains
```
**Descrição**: Retorna todos os domínios do modelo SOC CMM
**Resposta**:
```json
{
    "domains": [
        {
            "id": 1,
            "name": "Governance",
            "description": "Descrição do domínio de governança",
            "order_index": 1
        }
    ]
}
```

#### Listar Aspectos do Domínio
```
GET /api/domains/{domain_id}/aspects
```
**Descrição**: Retorna aspectos de um domínio específico
**Parâmetros**:
- `domain_id` (int): ID do domínio
**Resposta**:
```json
{
    "aspects": [
        {
            "id": "GOV-1",
            "domain_id": 1,
            "name": "Estrutura Organizacional",
            "code": "GOV-1",
            "description": "Descrição do aspecto",
            "order_index": 1
        }
    ]
}
```

#### Listar Questões do Aspecto
```
GET /api/aspects/{aspect_id}/questions
```
**Descrição**: Retorna questões de um aspecto específico
**Parâmetros**:
- `aspect_id` (str): ID do aspecto
**Resposta**:
```json
{
    "questions": [
        {
            "id": 1,
            "aspect_id": "GOV-1",
            "question_text": "Sua organização possui estrutura organizacional definida?",
            "question_type": "multiple_choice",
            "order_index": 1,
            "aspect_name": "Estrutura Organizacional",
            "domain_name": "Governance",
            "options": [
                {
                    "id": 1,
                    "question_id": 1,
                    "option_text": "Não existe",
                    "maturity_level": 1,
                    "order_index": 1
                },
                {
                    "id": 2,
                    "question_id": 1,
                    "option_text": "Existe informalmente",
                    "maturity_level": 2,
                    "order_index": 2
                }
            ]
        }
    ]
}
```

---

### 📝 Respostas e Pontuações

#### Submeter Resposta
```
POST /api/answers
```
**Descrição**: Submete uma resposta para uma questão
**Body**:
```json
{
    "assessment_id": 1,
    "question_id": 1,
    "answer_option_id": 3,
    "answer_text": null
}
```
**Resposta**:
```json
{
    "message": "Answer saved successfully"
}
```

#### Listar Respostas da Avaliação
```
GET /api/assessments/{assessment_id}/answers
```
**Descrição**: Retorna todas as respostas de uma avaliação
**Parâmetros**:
- `assessment_id` (int): ID da avaliação
**Resposta**:
```json
{
    "answers": [
        {
            "question_id": 1,
            "answer_option_id": 3,
            "answer_text": null,
            "maturity_score": 3
        }
    ]
}
```

#### Obter Pontuações da Avaliação
```
GET /api/assessments/{assessment_id}/scores
```
**Descrição**: Retorna pontuações calculadas da avaliação
**Parâmetros**:
- `assessment_id` (int): ID da avaliação
**Resposta**:
```json
{
    "scores": {
        "domain_scores": [
            {
                "name": "Governance",
                "score": 3.5,
                "percentage": 70.0
            }
        ],
        "aspect_scores": [
            {
                "domain_name": "Governance",
                "aspect_name": "Estrutura Organizacional",
                "score": 3.5,
                "percentage": 70.0
            }
        ]
    }
}
```

---

### 📊 Visualização de Dados

#### Dados para Gráfico Radar
```
GET /api/assessments/{assessment_id}/radar-data
```
**Descrição**: Retorna dados formatados para gráfico radar
**Parâmetros**:
- `assessment_id` (int): ID da avaliação
**Resposta**:
```json
{
    "radar_data": {
        "labels": ["Governance", "Operations", "Technology"],
        "datasets": [
            {
                "label": "SOC Maturity Level",
                "data": [70.0, 65.0, 80.0],
                "backgroundColor": "rgba(54, 162, 235, 0.2)",
                "borderColor": "rgba(54, 162, 235, 1)",
                "borderWidth": 2
            }
        ]
    }
}
```

#### Progresso do Cliente
```
GET /api/customers/{customer_id}/progress
```
**Descrição**: Retorna progresso ao longo do tempo para um cliente
**Parâmetros**:
- `customer_id` (int): ID do cliente
**Resposta**:
```json
{
    "progress": [
        {
            "assessment_id": 1,
            "name": "Avaliação SOC Q1 2024",
            "completed_at": "2024-01-01T15:00:00",
            "radar_data": {
                "labels": ["Governance", "Operations", "Technology"],
                "datasets": [
                    {
                        "label": "SOC Maturity Level",
                        "data": [70.0, 65.0, 80.0],
                        "backgroundColor": "rgba(54, 162, 235, 0.2)",
                        "borderColor": "rgba(54, 162, 235, 1)",
                        "borderWidth": 2
                    }
                ]
            }
        }
    ]
}
```

---

## 🚨 Códigos de Status HTTP

### Códigos de Sucesso
- **200 OK**: Requisição bem-sucedida
- **201 Created**: Recurso criado com sucesso

### Códigos de Erro
- **400 Bad Request**: Dados inválidos na requisição
- **404 Not Found**: Recurso não encontrado
- **422 Unprocessable Entity**: Erro de validação dos dados
- **500 Internal Server Error**: Erro interno do servidor

---

## 🔧 Configuração e Execução

### Requisitos
```bash
pip install -r requirements.txt
```

### Execução Local
```bash
python main.py
```

### Execução com Docker
```bash
docker-compose up -d
```

### Acesso à Documentação Interativa
- **Swagger UI**: `http://localhost:8400/docs`
- **ReDoc**: `http://localhost:8400/redoc`

---

## 📋 Estrutura do Banco de Dados

### Principais Tabelas
- **customers**: Informações dos clientes
- **assessments**: Avaliações realizadas
- **domains**: Domínios do modelo SOC CMM
- **aspects**: Aspectos dentro de cada domínio
- **questions**: Questões de cada aspecto
- **answer_options**: Opções de resposta para cada questão
- **assessment_answers**: Respostas dos usuários
- **assessment_scores**: Pontuações calculadas

### Relacionamentos
- Customer 1:N Assessment
- Assessment 1:N AssessmentAnswer
- Domain 1:N Aspect
- Aspect 1:N Question
- Question 1:N AnswerOption

---

## 📝 Notas Importantes

1. **Níveis de Maturidade**: O sistema utiliza escala de 1 a 5 para avaliar maturidade
2. **Cálculo de Pontuações**: Pontuações são calculadas automaticamente ao completar avaliação
3. **Persistência**: Todas as respostas são salvas automaticamente
4. **Versionamento**: Sistema permite múltiplas avaliações por cliente para acompanhar evolução
5. **Visualização**: Dados são apresentados em gráficos radar para facilitar análise

---

## 🤝 Suporte

Para dúvidas ou problemas com a API, consulte:
- Documentação interativa: `http://localhost:8400/docs`
- Logs da aplicação
- Arquivo README.md do projeto