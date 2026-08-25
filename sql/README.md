# SQL

| Directory | Contents |
| --- | --- |
| `schema/` | Table definitions. `schema/database_schema.sql` is the one read by `database.py`. |
| `seed/` | Questionnaire seed data generated from `dataset/`. |
| `migrations/` | Incremental schema changes and data fixes, applied by the scripts in `scripts/`. |

Migrations are **not** tracked by a migration framework and are not
automatically ordered. Read a file before running it, and back up your
database first.
