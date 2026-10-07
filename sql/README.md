# SQL

| Directory | Contents |
| --- | --- |
| `schema/` | Table definitions. `schema/database_schema.sql` is what `DatabaseManager.init_database()` reads; `schema/bilingual_schema.sql` adds the translation tables `database.py` queries for non-default languages. |
| `seed/` | `INSERT` statements for the questionnaire, generated from `dataset/`. These contain **no** `CREATE TABLE` — they assume the schema already exists. |
| `migrations/` | Incremental schema changes and data fixes. |

Migrations are **not** tracked by a migration framework and are not
automatically ordered. Read a file before running it, and back up your
database first.

## Bootstrapping

`python scripts/init_db.py` applies all of these in the right order —
`schema/database_schema.sql`, then `schema/bilingual_schema.sql`, then the
migrations — and seeds the questionnaire from `dataset/`. It is idempotent.
Both schema files use `IF NOT EXISTS` throughout, so they are safe to re-apply.

Note that the base schema alone is **not** enough to run the application: it
does not define `users.is_admin`, which `database.py` selects, and it does not
create the translation tables. `migrations/add_admin_field.sql` and
`schema/bilingual_schema.sql` supply those.

## Known gaps

- `seed/complete_populate_database.sql` holds a much larger questionnaire
  (565 questions, 1269 answer options) than the JSON dataset the bootstrap
  uses (97 questions, 12 options). It **cannot be loaded as is**: it was
  generated for an older schema and conflicts with the current one — it omits
  the `Results` domain, inserts `aspects` rows without the `code` column the
  schema requires, and uses `field_type` where the schema has `question_type`.
  Regenerating it against the current schema would make far more of the
  questionnaire scorable, and is the single most valuable data contribution
  this project could receive.
- `seed/` files contain `INSERT` statements only — they assume the schema
  already exists.
