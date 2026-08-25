# Installation

This guide covers local (development) and production installation of the
SOC CMM Assessment System.

## Prerequisites

- Python **3.11** or newer
- `pip`
- Optional: Docker and Docker Compose (for the containerised flow)
- Optional: `git` (to clone the repository)

## 1. Get the source code

```bash
git clone https://github.com/fernando-karl/soc_cmm_system.git
cd soc_cmm_system
```

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

> **Tip:** use a virtual environment (`python -m venv .venv && source .venv/bin/activate`) to isolate dependencies.

## 3. Configure environment variables

Copy the example file and edit it:

```bash
cp .env.example .env
```

| Variable                      | Required | Description                                                                                                         |
| ----------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------- |
| `SECRET_KEY`                  | **Yes**  | Used to sign JWT tokens. The application **refuses to start** without it.                                           |
| `ADMIN_PASSWORD`              | **Yes**¹ | Password for the bootstrap `admin` user created by the migration script.                                             |
| `ALLOWED_ORIGINS`             | No       | Comma-separated list of CORS origins. Defaults to `http://localhost:8400`. Use `*` only on trusted networks.        |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | No       | JWT lifetime in minutes (default: `30`).                                                                             |
| `HOST`                        | No       | Network interface to bind to (default: `0.0.0.0`).                                                                   |
| `PORT`                        | No       | TCP port to listen on (default: `8400`).                                                                             |
| `ADMIN_EMAIL`                 | No       | Email for the bootstrap admin user (default: `admin@soc-cmm.local`).                                                 |

¹ Required only for the initial migration. After the first login, change
the password from the UI and unset the variable.

Generate a strong `SECRET_KEY` with:

```bash
python -c "import secrets; print(secrets.token_urlsafe(48))"
```

## 4. Bootstrap the database

The first run requires creating the authentication tables and the initial
admin user:

```bash
export ADMIN_PASSWORD="your-strong-password"
python scripts/migrate_to_auth.py
```

The script creates the required `users` tables, backs up any existing
database, and registers the `admin` account using the password supplied in
`$ADMIN_PASSWORD`.

> If you already have a populated database under a different filename,
> either rename it to `soc_cmm_translated.db` or edit the `db_path`
> variable inside `migrate_to_auth.py`.

## 5. Start the application

```bash
python main.py
```

Browse to <http://localhost:8400>. To change the port:

```bash
PORT=9000 python main.py
```

## Docker (alternative)

See [`docker.md`](./docker.md) for the containerised flow.

## Verification

- The home page loads at `http://localhost:${PORT:-8400}`.
- Interactive API docs are available at `/docs` (Swagger) and `/redoc`.
- Log in as `admin` with `$ADMIN_PASSWORD` and **change the password
  immediately**.

## Troubleshooting

See [`troubleshooting.md`](./troubleshooting.md) if you hit any errors
during installation or start-up.
