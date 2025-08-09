# Docker e Deploy

## Local (Docker Compose)
```bash
docker-compose up -d
```

## Dockerfile (resumo)
- Base: `python:3.11-slim`
- Instala `requirements.txt`
- Expõe porta `8400`
- Comando: `python main.py`

## Produção (dicas)
- Use `SECRET_KEY` forte
- HTTPS e cookies seguros
- Banco de dados gerenciado (ex.: Postgres)
- Logs e backups regulares