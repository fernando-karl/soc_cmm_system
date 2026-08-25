# Scripts

Operational helper scripts. Run them **from the repository root**:

```bash
python scripts/migrate_to_auth.py
```

| Script | Purpose |
| --- | --- |
| `migrate_to_auth.py` | Adds the authentication tables and creates the initial `admin` user. Requires `ADMIN_PASSWORD` in the environment. |
| `run_admin_migration.py` | Adds the `is_admin` column to an existing user table. |
| `migrate_bilingual.py` | Merges the English and Portuguese databases into the bilingual `soc_cmm_bilingual.db`. |
| `run_populate_database.py` | Populates a fresh database from the SQL seed files in `sql/seed/`. |

## `legacy/`

One-off tooling kept for historical reference — see
[`legacy/README.md`](legacy/README.md). These scripts are **not** part of the
supported workflow.

## Safety

These scripts write directly to SQLite databases. **Back up your database
before running any of them.** None of them should ever be exposed to
untrusted input or run against a production database without review.
