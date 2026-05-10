# Development

## Project layout (summary)

- `main.py` — FastAPI app, web and API routes
- `database.py` — SQLite data access
- `auth.py` — authentication and JWT
- `mcp_server.py` — MCP server
- `templates/` — Jinja2 pages (EN/PT-BR)
- `static/` — CSS/JS/icons
- `tests/` — automated tests (`test_*.py` files)

## Running locally

```bash
pip install -r requirements.txt
cp .env.example .env       # set SECRET_KEY at minimum
python main.py
```

## Code conventions
- Python 3.11+, type hints where they add value
- Short, useful docstrings; no narration of obvious behaviour
- Descriptive function names
- Avoid deep nesting; use early returns

## Testing
- Run tests with `pytest` (when available)

## Contributing
This project is licensed under **CC BY-SA 4.0** — contributions are
accepted under the same terms. By contributing, you agree to license your
work under CC BY-SA 4.0 (see `LICENSE`).
