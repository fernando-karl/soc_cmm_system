# Desenvolvimento

## Estrutura do Projeto (resumo)
- `main.py` — app FastAPI, rotas web e API
- `database.py` — acesso ao SQLite
- `auth.py` — autenticação e JWT
- `mcp_server.py` — servidor MCP
- `templates/` — páginas Jinja2 (EN/PT-BR)
- `static/` — CSS/JS/ícones
- `tests/` — testes automatizados (arquivos `test_*.py`)

## Executando
```bash
pip install -r requirements.txt
python main.py
```

## Padrões de Código
- Python 3.11+, tipagem onde fizer sentido
- Docstrings e comentários curtos explicativos
- Funções com nomes descritivos
- Evite aninhamentos profundos; use retornos antecipados

## Testes
- Execute testes com `pytest` (se disponível)