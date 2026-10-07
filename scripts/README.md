# Scripts

Helper scripts. Run them **from the repository root**:

```bash
python scripts/migrate_to_auth.py
```

| Script | Purpose |
| --- | --- |
| `init_db.py` | **Start here.** Creates a working database from nothing: schema, translation tables, migrations, questionnaire data, and the admin user when `ADMIN_PASSWORD` is set. Idempotent — safe to re-run. `--recreate` deletes the database first (destructive, asks for confirmation). |
| `migrate_to_auth.py` | Adds the authentication tables and creates the initial `admin` user in an **existing** database. Requires `ADMIN_PASSWORD`. Exits if no database file is found. |
| `run_admin_migration.py` | Adds the `is_admin` column to an existing user table. |
| `migrate_bilingual.py` | Merges a `soc_cmm.db` and `soc_cmm_translated.db` into the bilingual `soc_cmm_bilingual.db`. |
| `run_populate_database.py` | Applies `sql/seed/complete_populate_database.sql` to `soc_cmm.db`. **Known broken:** it splits the SQL one line at a time, so every multi-statement or multi-line `INSERT` fails; it also targets `soc_cmm.db` rather than the application database. Kept for reference. |

`init_db.py` is the only one you need on a fresh clone; the others handle
upgrades of databases that predate a given change.

## `legacy/`

One-off tooling kept for historical reference — see
[`legacy/README.md`](legacy/README.md). Not part of any supported workflow.

## Safety

These scripts write directly to SQLite databases. **Back up your database
before running any of them.** None should be exposed to untrusted input or run
against production data without review.
