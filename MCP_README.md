# MCP Server — SOC CMM Assessment System

> **Canonical docs:** [`docs/en/mcp.md`](docs/en/mcp.md) (English) ·
> [`docs/pt-br/mcp.md`](docs/pt-br/mcp.md) (Português).
> This file is a short overview for MCP clients.

Model Context Protocol (MCP) integration so AI assistants can drive
customers, assessments, and questionnaire workflows against the SOC CMM
Assessment System API.

## What it can do

- Identify customers by ID, name, or email
- List in-progress assessments
- Create customers and assessments
- Fetch next questions and register answers
- Track progress, complete assessments, and retrieve scores

## Quick start

```bash
pip install -r requirements.txt
cp .env.example .env   # set SECRET_KEY
./start_mcp_server.sh
```

Full tool list, auth, and configuration: see the canonical MCP docs linked above.

## License

CC BY-SA 4.0 — derivative of SOC-CMM® by Rob van Os. This project is not
affiliated with soc-cmm.com. See `LICENSE` and `NOTICE`.
