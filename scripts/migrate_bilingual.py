"""
Migra para o banco bilíngue `soc_cmm_bilingual.db` conforme BILINGUAL_DATABASE_PLAN.md.

- Conteúdo estático (domains/aspects/questions/answer_options) vem de soc_cmm.db (EN canônico)
- Dados de usuário (users/customers/assessments/assessment_answers/assessment_scores)
  vêm de soc_cmm_translated.db (BD ativo até agora)
- Tabelas *_translations criadas e semeadas:
    language='en'    → a partir das colunas base
    language='pt_br' → a partir de soc_cmm_translated.db (IDs alinham)
- Aspects 4.20–4.23 existentes só em soc_cmm_translated.db são ignorados
  (vazios: 0 questions/scores/answers)

Idempotente: re-rodar regrava translations sem duplicar (INSERT OR REPLACE).
Cria backup do alvo antes de sobrescrever.
"""
import os
import shutil
import sqlite3
import sys
from datetime import datetime

EN_DB = "soc_cmm.db"
PT_DB = "soc_cmm_translated.db"
OUT_DB = "soc_cmm_bilingual.db"

USER_DATA_TABLES = [
    "users",
    "customers",
    "assessments",
    "assessment_answers",
    "assessment_scores",
]

TRANSLATION_SCHEMA = """
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
"""


def log(msg):
    print(f"[migrate] {msg}", flush=True)


def must_exist(path):
    if not os.path.exists(path):
        sys.exit(f"FATAL: missing source DB: {path}")


def copy_table(src_conn, dst_conn, table):
    """Copia todas as linhas de src.table para dst.table (apaga dst.table antes)."""
    rows = src_conn.execute(f"SELECT * FROM {table}").fetchall()
    if not rows:
        log(f"  {table}: 0 rows in source, skipping")
        return 0
    cols = [d[0] for d in src_conn.execute(f"SELECT * FROM {table} LIMIT 0").description]
    placeholders = ",".join("?" * len(cols))
    col_list = ",".join(cols)
    dst_conn.execute(f"DELETE FROM {table}")
    dst_conn.executemany(
        f"INSERT INTO {table} ({col_list}) VALUES ({placeholders})",
        [tuple(r) for r in rows],
    )
    return len(rows)


def ensure_users_table(conn):
    """soc_cmm.db não tem a tabela users; criar conforme database_schema.sql se faltar."""
    cur = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='users'"
    )
    if cur.fetchone():
        return
    log("  creating users table (missing in EN baseline)")
    conn.executescript(
        """
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(50) UNIQUE NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL,
            hashed_password VARCHAR(255) NOT NULL,
            full_name VARCHAR(255),
            is_active BOOLEAN DEFAULT 1,
            is_admin BOOLEAN DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        CREATE INDEX IF NOT EXISTS idx_users_username ON users(username);
        CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
        """
    )


def ensure_user_table_columns(dst_conn, src_conn, table):
    """Garante que dst.table tenha pelo menos as mesmas colunas que src.table.

    Cenário: soc_cmm.db (EN) pode ter colunas a menos em customers/etc do que
    soc_cmm_translated.db, o que faria o INSERT falhar.
    """
    # PRAGMA table_info -> (cid, name, type, notnull, dflt_value, pk)
    src_cols = {
        d[1]: d[2]
        for d in src_conn.execute(f"PRAGMA table_info({table})").fetchall()
    }
    dst_cols = {
        d[1]: d[2]
        for d in dst_conn.execute(f"PRAGMA table_info({table})").fetchall()
    }
    for col, typ in src_cols.items():
        if col not in dst_cols:
            log(f"  ALTER {table} ADD COLUMN {col} {typ or ''}")
            dst_conn.execute(f"ALTER TABLE {table} ADD COLUMN {col} {typ or ''}")


def main():
    must_exist(EN_DB)
    must_exist(PT_DB)

    if os.path.exists(OUT_DB):
        backup = f"{OUT_DB}.bak_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        log(f"backup existing {OUT_DB} -> {backup}")
        shutil.copy2(OUT_DB, backup)
        os.remove(OUT_DB)

    log(f"copy {EN_DB} -> {OUT_DB} (EN baseline)")
    shutil.copy2(EN_DB, OUT_DB)

    out = sqlite3.connect(OUT_DB)
    pt = sqlite3.connect(PT_DB)
    out.execute("PRAGMA foreign_keys = OFF")
    out.row_factory = sqlite3.Row
    pt.row_factory = sqlite3.Row

    # --- 1) Copy user data from PT into bilingual ---
    log("copying user data tables from PT-BR DB")
    ensure_users_table(out)
    for t in USER_DATA_TABLES:
        # Tabela pode existir em PT mas não em EN baseline (ex: users)
        out_exists = out.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name=?", (t,)
        ).fetchone()
        if not out_exists:
            log(f"  {t}: missing in bilingual; will create from PT schema")
            ddl = pt.execute(
                "SELECT sql FROM sqlite_master WHERE type='table' AND name=?", (t,)
            ).fetchone()
            if ddl and ddl[0]:
                out.executescript(ddl[0] + ";")
        ensure_user_table_columns(out, pt, t)
        n = copy_table(pt, out, t)
        log(f"  {t}: copied {n} rows")

    # --- 2) Create translation tables ---
    log("creating *_translations tables")
    out.executescript(TRANSLATION_SCHEMA)

    # --- 3) Seed EN translations from base columns ---
    log("seeding EN translations from base columns")
    out.execute(
        "INSERT OR REPLACE INTO domain_translations(domain_id, language, name, description) "
        "SELECT id, 'en', name, description FROM domains"
    )
    out.execute(
        "INSERT OR REPLACE INTO aspect_translations(aspect_id, language, name, description) "
        "SELECT id, 'en', name, description FROM aspects"
    )
    out.execute(
        "INSERT OR REPLACE INTO question_translations(question_id, language, question_text, guidance) "
        "SELECT id, 'en', question_text, guidance FROM questions"
    )
    out.execute(
        "INSERT OR REPLACE INTO answer_option_translations(answer_option_id, language, option_text) "
        "SELECT id, 'en', option_text FROM answer_options"
    )

    # --- 4) Seed PT-BR translations from PT DB ---
    log("seeding PT-BR translations from PT DB")
    en_aspect_ids = {r[0] for r in out.execute("SELECT id FROM aspects").fetchall()}

    # Domains
    n = 0
    for r in pt.execute("SELECT id, name, description FROM domains"):
        out.execute(
            "INSERT OR REPLACE INTO domain_translations(domain_id, language, name, description) "
            "VALUES (?, 'pt_br', ?, ?)",
            (r["id"], r["name"], r["description"]),
        )
        n += 1
    log(f"  domain_translations(pt_br): {n}")

    # Aspects — só os que existem no EN baseline (ignora 4.20-4.23 órfãos)
    n = skipped = 0
    for r in pt.execute("SELECT id, name, description FROM aspects"):
        if r["id"] not in en_aspect_ids:
            skipped += 1
            continue
        out.execute(
            "INSERT OR REPLACE INTO aspect_translations(aspect_id, language, name, description) "
            "VALUES (?, 'pt_br', ?, ?)",
            (r["id"], r["name"], r["description"]),
        )
        n += 1
    log(f"  aspect_translations(pt_br): {n} (skipped {skipped} PT-only)")

    # Questions
    n = 0
    for r in pt.execute("SELECT id, question_text, guidance FROM questions"):
        out.execute(
            "INSERT OR REPLACE INTO question_translations(question_id, language, question_text, guidance) "
            "VALUES (?, 'pt_br', ?, ?)",
            (r["id"], r["question_text"], r["guidance"]),
        )
        n += 1
    log(f"  question_translations(pt_br): {n}")

    # Answer options
    n = 0
    for r in pt.execute("SELECT id, option_text FROM answer_options"):
        out.execute(
            "INSERT OR REPLACE INTO answer_option_translations(answer_option_id, language, option_text) "
            "VALUES (?, 'pt_br', ?)",
            (r["id"], r["option_text"]),
        )
        n += 1
    log(f"  answer_option_translations(pt_br): {n}")

    out.commit()

    # --- 5) Validation ---
    log("validating")
    checks = [
        ("domains", 5),
        ("aspects", 33),
        ("questions", 565),
        ("answer_options", 1329),
    ]
    for table, expected in checks:
        got = out.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
        status = "OK" if got == expected else "WARN"
        log(f"  [{status}] {table}: {got} (expected {expected})")

    for tt, expected_per_lang in [
        ("domain_translations", 5),
        ("aspect_translations", 33),
        ("question_translations", 565),
        ("answer_option_translations", 1329),
    ]:
        for lang in ("en", "pt_br"):
            got = out.execute(
                f"SELECT COUNT(*) FROM {tt} WHERE language=?", (lang,)
            ).fetchone()[0]
            status = "OK" if got == expected_per_lang else "WARN"
            log(f"  [{status}] {tt}({lang}): {got} (expected {expected_per_lang})")

    # Spot-check: Business in EN, Negócio in PT
    en_name = out.execute(
        "SELECT name FROM domain_translations WHERE domain_id=1 AND language='en'"
    ).fetchone()
    pt_name = out.execute(
        "SELECT name FROM domain_translations WHERE domain_id=1 AND language='pt_br'"
    ).fetchone()
    log(f"  domain 1: EN={en_name[0]!r}  PT={pt_name[0]!r}")

    users = out.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    customers = out.execute("SELECT COUNT(*) FROM customers").fetchone()[0]
    assessments = out.execute("SELECT COUNT(*) FROM assessments").fetchone()[0]
    log(f"  user data: {users} users, {customers} customers, {assessments} assessments")

    out.close()
    pt.close()
    log(f"done: {OUT_DB}")


if __name__ == "__main__":
    main()
