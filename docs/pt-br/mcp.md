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

## Autenticação

Os endpoints de clientes e avaliações exigem autenticação, então o servidor MCP
precisa de um token bearer. Obtenha um em `POST /api/auth/login` e informe-o
como `API_TOKEN`:

```bash
export API_TOKEN='<token de /api/auth/login>'
export API_BASE_URL='http://localhost:8400'   # opcional, este é o padrão
python mcp_server.py
```

Sem `API_TOKEN` o servidor inicia mas registra um aviso, e toda chamada a
clientes ou avaliações falha com 401. O token carrega as permissões do usuário
que o emitiu, portanto o servidor MCP só vê os dados desse usuário.
