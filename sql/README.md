# SQL

| Directory | Contents |
| --- | --- |
| `schema/` | Table definitions. `schema/database_schema.sql` is what `DatabaseManager.init_database()` reads; `schema/bilingual_schema.sql` adds the translation tables `database.py` queries for non-default languages. |
| `seed/` | `INSERT` statements for the questionnaire, generated from `dataset/`. These contain **no** `CREATE TABLE` — they assume the schema already exists. |
| `migrations/` | Incremental schema changes and data fixes. |

Migrations are **not** tracked by a migration framework and are not
automatically ordered. Read a file before running it, and back up your
database first.

## Known gaps

- `DatabaseManager.__init__` has its `init_database()` and
  `populate_initial_data()` calls commented out (`database.py`), so nothing
  creates or seeds the database automatically. A fresh clone therefore has no
  working database, and `scripts/migrate_to_auth.py` exits with
  "No database file found!".
- `schema/database_schema.sql` does not define the `users.is_admin` column,
  but `database.py` selects it. That column is added by
  `migrations/add_admin_field.sql`, so the base schema alone is not sufficient
  for the application to run.
- A complete schema therefore needs all three of `schema/database_schema.sql`,
  `schema/bilingual_schema.sql` and `migrations/add_admin_field.sql`. See
  `tests/conftest.py`, which builds exactly that for the test suite.
