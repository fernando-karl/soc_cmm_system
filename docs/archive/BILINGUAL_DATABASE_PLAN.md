## SOC CMM Bilingual Database Plan (EN + PT-BR)

### Objective
- Use the English database as the canonical baseline
- Maintain both English and Portuguese content concurrently
- Serve DB-backed texts in the user’s chosen language without duplicating operational data

### Recommendation
- Use a single database with translation tables instead of separate English and Portuguese databases.
- Keep base tables in English as the fallback/default.
- Add four translation tables to store localized strings.

### Why not two databases?
- Separate DBs duplicate users/customers/assessments and analytics, causing divergence and operational complexity.
- A single DB keeps one source of truth for IDs and metrics while allowing multiple languages.

### Schema additions (minimal, additive)
Add translation tables to your existing schema. Keep base columns in English; translations live in side tables.

```sql
-- Domain translations
CREATE TABLE IF NOT EXISTS domain_translations (
  domain_id INTEGER NOT NULL,
  language TEXT NOT NULL,      -- 'en' | 'pt_br'
  name TEXT NOT NULL,
  description TEXT,
  PRIMARY KEY (domain_id, language),
  FOREIGN KEY (domain_id) REFERENCES domains(id)
);

-- Aspect translations
CREATE TABLE IF NOT EXISTS aspect_translations (
  aspect_id INTEGER NOT NULL,
  language TEXT NOT NULL,
  name TEXT NOT NULL,
  description TEXT,
  PRIMARY KEY (aspect_id, language),
  FOREIGN KEY (aspect_id) REFERENCES aspects(id)
);

-- Question translations
CREATE TABLE IF NOT EXISTS question_translations (
  question_id INTEGER NOT NULL,
  language TEXT NOT NULL,
  question_text TEXT NOT NULL,
  guidance TEXT,
  PRIMARY KEY (question_id, language),
  FOREIGN KEY (question_id) REFERENCES questions(id)
);

-- Answer option translations
CREATE TABLE IF NOT EXISTS answer_option_translations (
  answer_option_id INTEGER NOT NULL,
  language TEXT NOT NULL,
  option_text TEXT NOT NULL,
  PRIMARY KEY (answer_option_id, language),
  FOREIGN KEY (answer_option_id) REFERENCES answer_options(id)
);
```

### Step-by-step execution

1) Create the English baseline database
- Create schema using `database_schema.sql`.
- Populate with English content using the fixed SQL generator and populator already in the repo.
  - Generate (if needed): `generate_complete_sql_fixed.py` reads `soc_cmm_questions.json` and writes `complete_populate_database_fixed.sql`.
  - Populate: load the English SQL into the new DB (ensure it matches the fixed file; alternatively, execute the file directly).

2) Add the translation tables
- Run the SQL above to create `_translations` tables in the same DB.

3) Seed English translations (optional but consistent)
- Option A (skip): rely on base text as fallback when `language='en'`.
- Option B (seed): insert English rows into each `_translations` table with `language='en'` by selecting from base tables. This simplifies querying with a uniform JOIN pattern.

4) Seed Portuguese translations
- Source A (recommended): existing Portuguese DB `soc_cmm_translated.db` has IDs aligned; copy strings into `_translations` with `language='pt_br'`:
  - For each entity type, iterate IDs and insert translated text into the corresponding `_translations` table.
  - Example mapping: `domains.id -> domain_translations(domain_id)`, `aspects.id -> aspect_translations(aspect_id)`, `questions.id -> question_translations(question_id)`, `answer_options.id -> answer_option_translations(answer_option_id)`.
- Source B (alternative): use `soc_cmm_questions-port.json` / `traduzido.json` to map IDs to Portuguese strings and insert.

5) Update application data access
- In `database.py`, update read methods to return translated strings:
  - `get_domains(language)` – left join `domain_translations` on requested language; fallback to base if missing.
  - `get_domain_aspects(language)` – left join `aspect_translations`.
  - `get_aspect_questions(language)` – join `question_translations` and `answer_option_translations` for options.
- Use `COALESCE(translation, base)` in SQL or Python fallback if no translation found.
- Pass `language = get_language_from_request(request)` (already implemented in `main.py`) into these DB methods.

6) Point the app to the new bilingual DB
- Update `DatabaseManager` initialization in `main.py` (and config if present) to use the new DB path (e.g., `soc_cmm_bilingual.db`).
- Archive `soc_cmm_translated.db` as a backup; do not use it at runtime.

7) Validation
- Switch language selector (see `LANGUAGE_SYSTEM_SUMMARY.md`) and verify domains/aspects/questions/options change language while IDs and scoring remain stable.
- Complete an assessment in both languages and ensure results pages read data correctly.

8) Optional quick alternative (not recommended)
- Maintain two DBs (`soc_cmm_en.db` and `soc_cmm_translated.db`) and swap `db_path` based on cookie `language`.
- This splits users/customers/assessments and complicates operations/reporting.

9) Rollback and safety
- Keep backups before migration.
- Migration scripts should be idempotent; use `INSERT OR REPLACE` for translations and `IF NOT EXISTS` on DDL.

### Assets already in the repo
- English dataset and generators:
  - `soc_cmm_questions.json`
  - `generate_complete_sql_fixed.py`
  - `complete_populate_database_fixed.sql`
  - `run_populate_database_fixed.py`
- Portuguese sources:
  - `soc_cmm_translated.db` (current default in `database.py`)
  - `soc_cmm_questions-port.json`, `traduzido.json`
- Language selection already implemented in `main.py` and templates (see `LANGUAGE_SYSTEM_SUMMARY.md`).

### Effort overview
- DB work: 1–2 hours (create translation tables, seed PT-BR from translated DB/JSON).
- Code changes: 1–2 hours (joins/fallbacks in `database.py`, plumb `language` param).
- Testing: 0.5–1 hour.

### Next actions
- Create bilingual DB from English baseline
- Add/seed translation tables
- Update `database.py` queries to use translations
- Switch application to new DB and validate end-to-end