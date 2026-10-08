# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Changed

- **Scoring now follows the official SOC-CMM® 2.4.2 (advanced) workbook**
  instead of taking a plain average, so a number from this tool is comparable
  with one from the spreadsheet. Per aspect, over the answered questions with
  answer `a` and importance factor `h`, the workbook's `_Output` sheet computes
  `100 × (SUM(a×h) − SUM(h)) / (SUM(5×h) − SUM(h))`, a factor-weighted mean of
  `(a − 1) / 4`. Maturity on the 0–5 scale is `5 × percentage / 100` and a
  domain is the plain mean of its aspects, both as the workbook's results sheet
  derives them (the domain step already matched)
- **The lowest answer now scores 0%, not 20%.** Subtracting `SUM(h)` normalises
  over the range of the scale rather than its top, so a SOC that has none of a
  capability reads zero. **Percentages from earlier releases will go down.**
  `scripts/init_db.py` recalculates stored scores from the stored answers and
  says so when it does; the raw answers are untouched

### Added

- **Per-question importance**, as the workbook uses it: `none`, `low`,
  `normal`, `high` or `critical`, mapping to a factor of 0, 0.5, 1, 2 or 4
  (`_Score matrix`). A question marked `none` drops out of the score entirely.
  `POST /api/answers` takes an optional `importance` and it is stored per
  answer, defaulting to `normal` — what every question ships as in the
  workbook, which leaves the weighting inert until an assessor sets it
- `sql/migrations/add_answer_importance.sql`, applied by the bootstrap
- Tests pinning the scoring to the workbook: each uniform answer level scores
  exactly `100 × (a − 1) / 4`, importance moves a mixed aspect by the weighted
  amount, `none` removes a question, an aspect of only `none` questions gets no
  score rather than a fabricated 0, and the domain score is the mean of its
  aspects

### Known gap

- The questionnaire interface has no control for importance yet, so it can only
  be set through the API. Until it is added, every answer saved from the web
  interface is `normal`, which matches a stock workbook

### Fixed

- **A fresh install served the questionnaire in English to Portuguese users.**
  `scripts/init_db.py` created the four translation tables but never loaded
  anything into them, so only the interface was translated and all 622
  questions, their guidance and all 3110 answer options appeared in English.
  The fix was a documented manual step (`scripts/translations.py import`) that
  the README never mentioned. The bootstrap now imports every
  `dataset/translations/*.json` itself, and reports the translated-question
  count per language when it finishes
- README and both installation guides claimed the dataset held "97 questions
  but answer options for only 11 of them". That has been wrong since 2.0.0
  regenerated the questionnaire: it is 622 questions and 3110 options, all
  scorable
- README, both overviews and both usage guides still described **six** domains
  including `Results`, the misrepresentation 2.0.0 set out to fix, and still
  listed aspects under their pre-2.0.0 guessed names. The docs now describe the
  five scored domains and their real aspects
- The docs described a 0–5 maturity scale ("0 — Non-existent"), but the shipped
  questionnaire offers levels 1–5 with no zero. They now describe what ships

### Added

- A **Scoring** section in the README and in `docs/pt-br/visao_geral.md`,
  stating plainly that the score is an unweighted average and how it differs
  from the official workbook: the workbook normalises per question as
  `100 × (answer − 1) / 4` so its lowest answer scores 0% where this tool's
  scores 20%, and it weights questions by an assessor-set importance
  (factor 0 / 0.5 / 1 / 2 / 4) where this tool treats all questions equally.
  The point is that nobody compares a number from here with a number from the
  workbook and concludes one of them is broken
- Tests that a fresh bootstrap actually produces a usable Portuguese
  questionnaire: the translation row counts match the content counts, the
  stored Portuguese is not just the English text copied across, and the
  language-aware queries the application uses return it

## [2.0.0] - 2026-10-08


### Upgrading from 1.x
The questionnaire has been replaced, so question and answer ids from 1.x do not
map onto this release. **There is no in-place migration.** Seeding never
overwrites existing content, so an existing database keeps its old questionnaire;
`scripts/init_db.py` now detects this and says so. To move to the corrected
questionnaire, export anything you need and rebuild with
`python scripts/init_db.py --recreate`.

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
- The session cookie's `Secure` flag is no longer hardcoded to `false`. It now
  follows `ALLOWED_ORIGINS` — on when every origin is `https://`, off otherwise
  — and `COOKIE_SECURE` forces it either way, which is what a deployment behind
  a TLS-terminating proxy needs. `SameSite` is configurable through
  `COOKIE_SAMESITE` (still `lax` by default)
- `ACCESS_TOKEN_EXPIRE_MINUTES` now actually controls the session. Login
  ignored it and issued a 24-hour token with a matching cookie; both now expire
  together after `ACCESS_TOKEN_EXPIRE_MINUTES`, whose default drops from 24
  hours to 8. `create_access_token` fell back to 15 minutes when given no
  explicit lifetime, a third value nothing could configure; it now uses the
  same setting
- `python-jose` 3.3.0 → 3.5.0, fixing CVE-2024-33663 (algorithm confusion with
  an OpenSSH ECDSA key) and CVE-2024-33664 (JWE decompression bomb)

### Changed

- `mcp` 1.0.0 → 1.30.0 (the 2.x line moved the decorator API off the lowlevel
  `Server` onto `FastMCP` and would need the server rewritten), and `httpx`
  0.27.0 → 0.28.1, which `mcp` 1.30 requires
- **The questionnaire is now generated from the official SOC-CMM® workbook and
  tracks v2.4.2 (advanced)**, replacing a hand-built extract that diverged from
  the framework. 5 scored domains (not 6 — `Results` is the workbook's output
  section, not a domain), 27 aspects under their official names, 622 questions
  and 3110 answer options, every one scorable. Each option is that question's
  own description of its maturity level, taken from the workbook's `_Guidance`
  sheet, and each question carries its NIST CSF 2.0 mapping
- Attribution throughout — the in-app footer and About page in both languages,
  `NOTICE`, and the docs — now names v2.4.2 (advanced)
- Screenshots and the PDF deck regenerated against the corrected data; the
  deck now states the five domains, the 622 questions and 3110 options, the
  bootstrap step, and that the Portuguese covers the questionnaire itself
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

- `ALLOWED_ORIGINS` defaulted to `http://localhost:8000` while the application
  serves on 8400, so the documented default rejected every browser request it
  was meant to allow. It now follows `PORT`
- The MCP server built its `InitializationOptions` by hand and passed
  `notification_options=None` into `get_capabilities`, which reads attributes
  off it. The pinned 1.0.0 tolerated that; on 1.30.0 it raises `AttributeError`
  before the server accepts a single request. It now uses
  `server.create_initialization_options()`, which derives the name, version and
  capabilities from the server instance
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

### Removed

- Tracked SQLite databases and backups (and purged from git history) to avoid
  shipping credentials or personal data
- Root draft/summary markdown files moved to `docs/archive/`

## [1.0.0] - 2025-07

### Added

- Initial SOC CMM Assessment System (FastAPI, SQLite, bilingual EN/PT-BR UI)
- Authentication, admin features, REST API, MCP server
- CC BY-SA 4.0 license and NOTICE with SOC-CMM® attribution
