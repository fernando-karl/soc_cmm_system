# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Changed

- **The questionnaire is now generated from the official SOC-CMM® workbook and
  tracks v2.4.2 (advanced)**, replacing a hand-built extract that diverged from
  the framework. 5 scored domains (not 6 — `Results` is the workbook's output
  section, not a domain), 27 aspects under their official names, 622 questions
  and 3110 answer options, every one scorable. Each option is that question's
  own description of its maturity level, taken from the workbook's `_Guidance`
  sheet, and each question carries its NIST CSF 2.0 mapping
- Attribution throughout — the in-app footer and About page in both languages,
  `NOTICE`, and the docs — now names v2.4.2 (advanced)
- Screenshots and the PDF deck regenerated against the corrected data

### Added

- `scripts/init_db.py` — a one-command database bootstrap. It applies the base
  schema, the translation tables and the migrations, seeds the questionnaire,
  and creates the admin user when `ADMIN_PASSWORD` is set. It is idempotent, so
  it also brings an existing database up to date, and `--recreate` rebuilds from
  scratch after confirmation. A fresh clone can now be run by following the
  README, which it previously could not
- Tests covering the bootstrap: every table the application queries is created,
  the `is_admin` migration is applied, the questionnaire is seeded, re-running
  changes nothing, and the admin user appears only when a password is given


- **Visible SOC-CMM® attribution in the application itself**, as the CC BY-SA 4.0
  license requires. Previously the credit existed only in `LICENSE`, `NOTICE`
  and the README, so users of the running tool never saw it. Now: a notice in
  the footer of every page that extends the base template, a compact notice on
  the standalone sign-in, registration and change-password pages, and a full
  "Attribution & License" section on the About page — in both English and
  Portuguese, covering the credit to Rob van Os, the CC BY-SA 4.0 link, the
  trademark reservation and the non-affiliation statement
- `docs/screenshots/` — a captured gallery of the English and Portuguese
  interfaces and the mobile layout, linked from the README
- `docs/presentation/` — a 13-slide project overview as a 16:9 PDF, also
  linked from the README


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

- The progress-over-time chart plotted assessments newest-first, so a client
  whose maturity improved was drawn as declining. The series is now ordered
  chronologically

- `DatabaseManager.init_database()` split the schema file on `;`, which breaks
  on semicolons inside string literals; it now uses `executescript`. The schema
  also used plain `CREATE TABLE` / `CREATE INDEX`, so it could not be re-applied
  — both now use `IF NOT EXISTS`

- Every `*_pt_br.html` page extended the **English** `base.html`, so the
  Portuguese interface rendered an English navigation bar and footer and
  `base_pt_br.html` was dead code. They now extend `base_pt_br.html`
- The English `base.html` carried a Portuguese footer tagline
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
