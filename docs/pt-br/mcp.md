# MCP (Model Context Protocol)

Servidor MCP em Python que permite que modelos de IA interajam com a API do SOC CMM.

## Como usar
1. Instale dependências: `pip install -r requirements.txt`
2. Inicie a API: `python main.py`
3. Rode o servidor MCP: `python mcp_server.py`

Configuração via `mcp_config.json` (variável `API_BASE_URL`).

## Ferramentas Disponíveis
1. `identify_customer` — Identifica cliente por ID/nome/email
2. `get_assessments_in_progress` — Avaliações em andamento de um cliente
3. `create_customer` — Cria cliente
4. `create_assessment` — Cria avaliação
5. `get_next_questions` — Próximas questões (por domínio/aspecto)
6. `register_answer` — Registra resposta
7. `get_assessment_progress` — Progresso da avaliação
8. `complete_assessment` — Conclui avaliação e calcula pontuações
9. `get_assessment_results` — Resultados e análises

Erros são tratados com mensagens descritivas e logs.

Consulte `MCP_README.md` e `MCP_IMPLEMENTATION_SUMMARY.md` para detalhes.