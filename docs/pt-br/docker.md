# Docker e Deploy

A aplicação inclui um `Dockerfile` baseado em `python:3.11-slim` e um
`docker-compose.yml` pronto para uso local.

## Pré-requisitos

- Docker 20+
- Docker Compose v2 (`docker compose ...`)

## 1. Configurar o `.env`

Antes de subir os containers, crie o arquivo `.env` baseado em
`.env.example` (a aplicação **não inicia** sem `SECRET_KEY`):

```bash
cp .env.example .env
# edite .env e defina SECRET_KEY, ADMIN_PASSWORD, etc.
```

O `docker-compose.yml` carrega o `.env` automaticamente via `env_file`.

## 2. Subir o serviço

```bash
docker compose up -d --build
```

A aplicação fica disponível em <http://localhost:8400> (ou na porta que você
definir em `PORT`).

## 3. Inicializar o banco (primeira execução)

Com o container rodando, execute a migração para criar as tabelas de
autenticação e o usuário admin:

```bash
docker compose exec soc-cmm python migrate_to_auth.py
```

## Trocar a porta

A porta exposta no host é controlada pela variável `PORT` no `.env`:

```bash
PORT=9000 docker compose up -d
```

A porta interna do container permanece `8400`.

## Variáveis de ambiente importantes

| Variável            | Função                                                                  |
| ------------------- | ----------------------------------------------------------------------- |
| `SECRET_KEY`        | Assinatura JWT — obrigatória, sem fallback.                             |
| `ADMIN_PASSWORD`    | Senha do admin inicial — apenas para a migração.                        |
| `ALLOWED_ORIGINS`   | Lista CSV de origens CORS. Padrão: `http://localhost:8400`.             |
| `PORT`, `HOST`      | Porta/interface escutada pela aplicação. Padrão: `0.0.0.0:8400`.        |

Veja a lista completa em [`instalacao.md`](./instalacao.md) e em
`.env.example`.

## Persistência de dados

O serviço monta `./data` no caminho `/app/data` do container. Aponte os
caminhos de banco/arquivos persistentes para esse diretório se você
customizar o ponto de montagem.

> **Atenção:** o banco SQLite padrão (`soc_cmm_translated.db`) está no
> diretório raiz da aplicação dentro do container. Para persistência real
> em produção, ajuste `database.py` (variável `db_path`) para apontar para
> `/app/data/soc_cmm_translated.db` ou migre para um banco gerenciado
> (PostgreSQL/MySQL).

## Checagem de saúde

O container expõe um `HEALTHCHECK` que faz um GET em `/` na porta interna.
Em ambientes com proxy reverso, ajuste a URL conforme necessário.

## Recomendações para produção

- TLS terminando em proxy reverso (nginx, Caddy, Traefik).
- `ALLOWED_ORIGINS` restrito a domínios reais (nunca `*`).
- `SECRET_KEY` rotacionado periodicamente.
- Usuário admin com senha forte trocada após o primeiro login;
  `ADMIN_PASSWORD` removida do ambiente após a migração.
- Backups regulares do volume de dados.
- Considere migrar SQLite para PostgreSQL/MySQL em deploys multi-usuário.

Para parar e remover os containers:

```bash
docker compose down
```

Para remover também os volumes (perde os dados):

```bash
docker compose down -v
```
