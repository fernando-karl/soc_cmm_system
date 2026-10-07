-- Translation tables for the bilingual (EN / PT-BR) content.
--
-- `database.py` queries these whenever a language other than the stored
-- default is requested, so they are part of the schema the application needs,
-- not an optional extra. They were previously defined only as a Python string
-- inside `scripts/migrate_bilingual.py`; that script applies this same DDL.

CREATE TABLE IF NOT EXISTS domain_translations (
  domain_id INTEGER NOT NULL,
  language TEXT NOT NULL,
  name TEXT NOT NULL,
  description TEXT,
  PRIMARY KEY (domain_id, language),
  FOREIGN KEY (domain_id) REFERENCES domains(id)
);

CREATE TABLE IF NOT EXISTS aspect_translations (
  aspect_id TEXT NOT NULL,
  language TEXT NOT NULL,
  name TEXT NOT NULL,
  description TEXT,
  PRIMARY KEY (aspect_id, language),
  FOREIGN KEY (aspect_id) REFERENCES aspects(id)
);

CREATE TABLE IF NOT EXISTS question_translations (
  question_id INTEGER NOT NULL,
  language TEXT NOT NULL,
  question_text TEXT NOT NULL,
  guidance TEXT,
  PRIMARY KEY (question_id, language),
  FOREIGN KEY (question_id) REFERENCES questions(id)
);

CREATE TABLE IF NOT EXISTS answer_option_translations (
  answer_option_id INTEGER NOT NULL,
  language TEXT NOT NULL,
  option_text TEXT NOT NULL,
  PRIMARY KEY (answer_option_id, language),
  FOREIGN KEY (answer_option_id) REFERENCES answer_options(id)
);
