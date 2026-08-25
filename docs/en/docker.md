# Docker & deployment

The application ships with a `Dockerfile` based on `python:3.11-slim` and a
ready-to-use `docker-compose.yml`.

## Prerequisites

- Docker 20+
- Docker Compose v2 (`docker compose ...`)

## 1. Configure `.env`

Create `.env` from the example before starting the containers (the
application **refuses to start** without `SECRET_KEY`):

```bash
cp .env.example .env
# edit .env and set SECRET_KEY, ADMIN_PASSWORD, etc.
```

The `docker-compose.yml` automatically loads `.env` via `env_file`.

## 2. Bring the service up

```bash
docker compose up -d --build
```

The application is reachable at <http://localhost:8400> (or at the port you
set via `PORT`).

## 3. Bootstrap the database (first run)

With the container running, execute the migration to create the auth
tables and the admin user:

```bash
docker compose exec soc-cmm python scripts/migrate_to_auth.py
```

## Changing the port

The host-side port is controlled by the `PORT` variable in `.env`:

```bash
PORT=9000 docker compose up -d
```

The container's internal port stays at `8400`.

## Important environment variables

| Variable          | Purpose                                                                  |
| ----------------- | ------------------------------------------------------------------------ |
| `SECRET_KEY`      | JWT signing — required, no fallback.                                     |
| `ADMIN_PASSWORD`  | Bootstrap admin password — only needed for the initial migration.        |
| `ALLOWED_ORIGINS` | CSV list of allowed CORS origins. Default: `http://localhost:8400`.       |
| `PORT`, `HOST`    | Port/interface the application listens on. Default: `0.0.0.0:8400`.       |

See the full list in [`installation.md`](./installation.md) and in
`.env.example`.

## Data persistence

The service mounts `./data` to `/app/data` in the container. If you
customise database paths, point them under that directory.

> **Note:** the default SQLite database (`soc_cmm_translated.db`) lives in
> the application root inside the container. For real persistence in
> production, adjust `database.py` (the `db_path` variable) to point at
> `/app/data/soc_cmm_translated.db` or migrate to a managed database
> (PostgreSQL/MySQL).

## Healthcheck

The container exposes a `HEALTHCHECK` that hits `/` on the internal port.
Adjust the URL in environments fronted by a reverse proxy.

## Production recommendations

- Terminate TLS in a reverse proxy (nginx, Caddy, Traefik).
- Restrict `ALLOWED_ORIGINS` to your real domains (never `*`).
- Rotate `SECRET_KEY` periodically.
- Strong admin password, changed after the first login;
  `ADMIN_PASSWORD` removed from the environment after the migration.
- Regular backups of the data volume.
- Consider migrating from SQLite to PostgreSQL/MySQL for multi-user
  deployments.

To stop and remove the containers:

```bash
docker compose down
```

To also remove the volumes (deletes data):

```bash
docker compose down -v
```
