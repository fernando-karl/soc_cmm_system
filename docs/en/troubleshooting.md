# Troubleshooting

## Application refuses to start (`SECRET_KEY environment variable is required`)

`SECRET_KEY` must be set in the environment. Set it before starting:

```bash
export SECRET_KEY="$(python -c 'import secrets; print(secrets.token_urlsafe(48))')"
python main.py
```

For Docker, define it in the `.env` file loaded by `docker-compose.yml`.

## Migration fails with `ADMIN_PASSWORD environment variable is required`

The bootstrap admin requires `ADMIN_PASSWORD`:

```bash
export ADMIN_PASSWORD="strong-password"
python scripts/migrate_to_auth.py
```

## Port conflict

The default port is `8400`. To change it:

```bash
PORT=9000 python main.py
```

For Docker: `PORT=9000 docker compose up -d`.

## Database errors

- Make sure `soc_cmm_translated.db` exists and is writable.
- Confirm the `users` table exists (run `migrate_to_auth.py`).
- For local testing only, you may delete the `.db` file and re-run the
  population scripts (`scripts/legacy/run_populate_database_fixed.py`).

## Authentication issues

- Clear browser cookies (the token may be expired or stale).
- Confirm the `SECRET_KEY` is the same one used to issue the token; after
  rotating it, every user must log in again.
- Inspect the server logs for JWT errors.

## CORS errors in the browser

The origin issuing the request must appear in `ALLOWED_ORIGINS`:

```bash
export ALLOWED_ORIGINS="https://app.example.com,https://admin.example.com"
```

Use `*` only on trusted networks; credentials are automatically disabled
when `*` is the only configured origin.

## Dependencies

```bash
pip install -r requirements.txt
```

If you see a version error, ensure Python 3.11+ (`python --version`).

## Logs

- Server console (uvicorn) — shows requests, errors and stack traces.
- Browser DevTools — shows JS and CORS errors.
- For Docker: `docker compose logs -f soc-cmm`.
