# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added

- Open-source readiness: `SECURITY.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`,
  GitHub issue/PR templates, and minimal CI
- Maintainer contact on privacy/terms pages and README Support section
- Documentation alignment with SOC-CMM® maturity scale (0–5) and non-affiliation notice

### Changed

- Repository reorganised for public release: the project root now holds only
  the application entrypoints and project metadata. Supporting files moved to
  `dataset/` (SOC-CMM® source data), `sql/{schema,seed,migrations}/`,
  `scripts/` (operational tooling) with `scripts/legacy/` for historical
  one-offs, and `tests/`
- `main.py` and `database.py` now resolve templates, static assets, the SQL
  schema and the seed dataset relative to the module location instead of the
  current working directory, so the app runs from any directory
- Renamed `soc cmm port.txt` to `dataset/soc_cmm_port.txt` (removed spaces)
- Added `README.md` files to `dataset/`, `sql/`, `scripts/`, `scripts/legacy/`
  and `tests/` describing contents and safe usage
- Documented the layout in a "Project Structure" section of the README

### Added

- An automated `pytest` suite in `tests/`, wired into CI. It builds its own
  throwaway database and covers the access-control rules above: every
  customer- and assessment-scoped endpoint is asserted against an anonymous
  caller, a second authenticated tenant, and the owner. Verified to fail
  against the pre-fix code
- `sql/schema/bilingual_schema.sql` — the translation tables `database.py`
  queries existed only as a Python string inside `scripts/migrate_bilingual.py`
  and were missing from the schema
- `requirements-dev.txt` for test and development dependencies

### Fixed

- `POST /api/answers` passed `answer_text` to `DatabaseManager.save_answer()`,
  which did not accept it, so the endpoint returned 500 on every call. The
  method now stores `answer_text` (the column already existed), treats
  `answer_option_id` as optional, and raises on an unknown option id, which the
  route maps to a 400 instead of a 500

- `start_mcp_server.sh` still invoked `test_mcp_server.py` at the old root path
  after the reorganisation, so the script aborted and never started the MCP
  server
- The SQLite path stayed relative to the current directory while templates and
  static files became module-relative, so running from another directory booted
  the app against an empty auto-created database instead of failing loudly.
  The path is now module-relative and overridable via `DB_PATH`, shared by
  `database.py` and `auth.py` so the two cannot drift
- `docker-compose.yml` now sets `DB_PATH` inside the mounted volume; previously
  the database was written to the image layer and lost on every rebuild
- `scripts/legacy/extract_questions_from_excel.py` wrote its output to the
  repository root instead of `dataset/`
- Stale `migrate_to_auth.py` paths in `CONTRIBUTING.md` and several active docs
  pages, which disagreed with their own translations after the move
- The manual check scripts raised `SystemExit` at import time, which aborted
  `pytest` collection with an internal error. The credential lookup is now
  lazy, and the scripts are named `check_*.py` under `tests/manual/` so
  `pytest` does not collect scripts that are not tests
- Corrected the new per-directory READMEs, which claimed behaviour the code
  does not have: `init_database()` and `populate_initial_data()` are commented
  out in `DatabaseManager.__init__`, the seed SQL contains no `CREATE TABLE`,
  `run_populate_database.py` splits SQL line-by-line and cannot work, and the
  base schema lacks the `users.is_admin` column the application selects. These
  gaps are now documented rather than papered over

### Security

- **Fixed an access-control flaw (IDOR) in the assessment API.** Seven
  endpoints took no authenticated user and performed no ownership check:
  `GET /api/assessments/{id}`, `PUT /api/assessments/{id}/complete`,
  `GET /api/assessments/{id}/answers`, `POST /api/answers`,
  `GET /api/assessments/{id}/scores`, `GET /api/assessments/{id}/radar-data`
  and `GET /api/customers/{id}/progress`. Since customer and assessment ids
  are sequential integers, any unauthenticated caller who could reach the
  server was able to enumerate and read every tenant's assessment results, and
  `POST /api/answers` allowed writing answers into any assessment. All seven
  now require authentication and verify ownership through new
  `assert_customer_owner` / `assert_assessment_owner` helpers
- The MCP server sent no credentials and worked only because of the flaw above.
  It now sends a bearer token from `API_TOKEN`, and warns at startup when it is
  unset
- Pinned `bcrypt>=4.0.1,<4.1`. `passlib` 1.7.4 probes bcrypt with a 72+ byte
  password, which bcrypt 4.1+ rejects outright, so a fresh install resolved to
  bcrypt 5.x and **no password could be hashed or verified at all**

- Removed hard-coded credentials from the integration scripts in `tests/`;
  they now read `ADMIN_PASSWORD` / `TEST_USER_PASSWORD` from the environment
  and refuse to run when the admin password is unset

### Removed

- Tracked SQLite databases and backups (and purged from git history) to avoid
  shipping credentials or personal data
- Root draft/summary markdown files moved to `docs/archive/`

## [1.0.0] - 2025-07

### Added

- Initial SOC CMM Assessment System (FastAPI, SQLite, bilingual EN/PT-BR UI)
- Authentication, admin features, REST API, MCP server
- CC BY-SA 4.0 license and NOTICE with SOC-CMM® attribution
