"""The database bootstrap must work on a fresh clone, and be safe to re-run.

These run `scripts/init_db.py` as a subprocess against a throwaway DB_PATH,
which is exactly how a new contributor runs it.
"""
import json
import sqlite3
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
INIT_DB = REPO_ROOT / "scripts" / "init_db.py"


def run_init_db(db_path, **extra_env):
    env = {
        "PATH": "/usr/bin:/bin:/usr/local/bin",
        "DB_PATH": str(db_path),
        "SECRET_KEY": "test-only-secret-key-not-for-production",
        **extra_env,
    }
    return subprocess.run(
        [sys.executable, str(INIT_DB)],
        cwd=REPO_ROOT, env=env, capture_output=True, text=True, timeout=300,
    )


def tables(db_path):
    conn = sqlite3.connect(db_path)
    try:
        return {r[0] for r in conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table'")}
    finally:
        conn.close()


def count(db_path, table):
    conn = sqlite3.connect(db_path)
    try:
        return conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
    finally:
        conn.close()


@pytest.fixture(scope="module")
def built(tmp_path_factory):
    """A database built by the bootstrap exactly as a fresh clone would."""
    db_path = tmp_path_factory.mktemp("init-db") / "bootstrap.db"
    result = run_init_db(db_path)
    assert result.returncode == 0, f"init_db.py failed:\n{result.stdout}\n{result.stderr}"
    assert db_path.exists(), "init_db.py reported success but created no database"
    return db_path


def test_creates_every_table_the_application_queries(built):
    """Including the bits the base schema alone does not provide."""
    present = tables(built)
    for table in ("users", "customers", "domains", "aspects", "questions",
                  "answer_options", "assessments", "assessment_answers",
                  "assessment_scores"):
        assert table in present, f"missing application table: {table}"
    for table in ("domain_translations", "aspect_translations",
                  "question_translations", "answer_option_translations"):
        assert table in present, f"missing translation table: {table}"


def test_applies_the_is_admin_migration(built):
    """database.py selects users.is_admin; the base schema does not define it."""
    conn = sqlite3.connect(built)
    try:
        columns = {r[1] for r in conn.execute("PRAGMA table_info(users)")}
    finally:
        conn.close()
    assert "is_admin" in columns


def test_seeds_the_questionnaire(built):
    """SOC-CMM has five scored domains; Results is output, not a sixth domain."""
    assert count(built, "domains") == 5
    assert count(built, "aspects") == 27
    assert count(built, "questions") == 649


def test_every_question_is_scorable(built):
    """A question with no answer options cannot be completed or scored."""
    conn = sqlite3.connect(built)
    try:
        total = conn.execute("SELECT COUNT(*) FROM questions").fetchone()[0]
        answerable = conn.execute(
            "SELECT COUNT(DISTINCT question_id) FROM answer_options").fetchone()[0]
    finally:
        conn.close()
    assert answerable == total, f"only {answerable} of {total} questions are scorable"


def test_aspects_use_the_official_names(built):
    """Guard against the names being reconstructed from the sheet codes again."""
    conn = sqlite3.connect(built)
    try:
        names = {r[0] for r in conn.execute("SELECT name FROM aspects")}
        domains = {r[0] for r in conn.execute("SELECT name FROM domains")}
    finally:
        conn.close()
    assert domains == {"Business", "People", "Process", "Technology", "Services"}
    for official in ("Customers / Stakeholders", "Roles and Hierarchy",
                     "People Management", "Operations and Facilities",
                     "Detection Engineering & Validation", "Security Monitoring",
                     "Security Incident Management", "Threat Intelligence"):
        assert official in names, f"missing official aspect name: {official}"
    for wrong in ("Cost", "Retention & Hiring", "Performance Management",
                  "Operations & Functions", "Data & Technology Exchange",
                  "Service Catalog Management", "Threat Hunting & Research"):
        assert wrong not in names, f"guessed-from-code aspect name is back: {wrong}"


def test_a_fully_mature_assessment_scores_full_marks(built):
    """The option scale must match the scoring divisor, or a perfect SOC is capped."""
    conn = sqlite3.connect(built)
    try:
        levels = {r[0] for r in conn.execute(
            "SELECT DISTINCT maturity_level FROM answer_options")}
    finally:
        conn.close()
    assert max(levels) == 5, f"top maturity level is {max(levels)}, expected 5"


def test_loads_the_shipped_translations(built):
    """A fresh install must serve Portuguese to Portuguese users.

    The questionnaire is seeded in English and the translated text lives in
    separate tables, so a bootstrap that skips the import leaves a PT-BR user
    reading 649 English questions with only the interface translated.
    """
    conn = sqlite3.connect(built)
    try:
        counts = {
            table: conn.execute(
                f"SELECT COUNT(*) FROM {table} WHERE language = 'pt_br'").fetchone()[0]
            for table in ("domain_translations", "aspect_translations",
                          "question_translations", "answer_option_translations")
        }
    finally:
        conn.close()
    assert counts["domain_translations"] == count(built, "domains")
    assert counts["aspect_translations"] == count(built, "aspects")
    assert counts["question_translations"] == count(built, "questions")
    assert counts["answer_option_translations"] == count(built, "answer_options")


def test_translated_questions_are_actually_in_portuguese(built):
    """Guard against the import writing the English text into the pt_br rows,
    which would satisfy a row count but change nothing a user sees."""
    conn = sqlite3.connect(built)
    try:
        same = conn.execute(
            "SELECT COUNT(*) FROM questions q "
            "JOIN question_translations t ON t.question_id = q.id "
            "WHERE t.language = 'pt_br' AND t.question_text = q.question_text"
        ).fetchone()[0]
        total = conn.execute(
            "SELECT COUNT(*) FROM question_translations WHERE language = 'pt_br'"
        ).fetchone()[0]
    finally:
        conn.close()
    # A handful of identical strings is plausible (acronyms, product names);
    # a large overlap means the import copied the English across.
    assert same < total * 0.1, (
        f"{same} of {total} pt_br questions are byte-identical to the English")


LANGUAGE_PROBE = """
import json, sys
sys.path.insert(0, ".")
from database import DatabaseManager
db = DatabaseManager()
out = {}
for lang in ("en", "pt_br"):
    domains = db.get_domains(lang)
    aspects = db.get_domain_aspects(domains[0]["id"], lang)
    questions = db.get_aspect_questions(aspects[0]["id"], lang)
    out[lang] = {"domains": [d["name"] for d in domains],
                 "aspect": aspects[0]["name"],
                 "question": questions[0]["question_text"]}
print(json.dumps(out))
"""


def test_the_language_aware_queries_return_the_translations(built):
    """The rows exist; this is the path the application actually reads them by."""
    result = subprocess.run(
        [sys.executable, "-c", LANGUAGE_PROBE],
        cwd=REPO_ROOT,
        env={"PATH": "/usr/bin:/bin:/usr/local/bin", "DB_PATH": str(built),
             "SECRET_KEY": "test-only-secret-key-not-for-production"},
        capture_output=True, text=True, timeout=120,
    )
    assert result.returncode == 0, result.stderr
    out = json.loads(result.stdout.strip().splitlines()[-1])
    assert out["en"]["domains"] == ["Business", "People", "Process",
                                   "Technology", "Services"]
    assert out["pt_br"]["domains"] == ["Neg\u00f3cio", "Pessoas", "Processo",
                                       "Tecnologia", "Servi\u00e7os"]
    for field in ("aspect", "question"):
        assert out["pt_br"][field] != out["en"][field], (
            f"pt_br {field} is still the English text: {out['pt_br'][field]!r}")


def test_is_idempotent(built):
    """Re-running must not fail, duplicate the seed, or wipe anything."""
    before = {t: count(built, t) for t in ("domains", "aspects", "questions")}
    result = run_init_db(built)
    assert result.returncode == 0, f"second run failed:\n{result.stdout}\n{result.stderr}"
    after = {t: count(built, t) for t in ("domains", "aspects", "questions")}
    assert after == before, f"re-running changed the seed: {before} -> {after}"


def test_creates_the_admin_user_only_when_a_password_is_given(tmp_path):
    no_password = tmp_path / "no-admin.db"
    result = run_init_db(no_password)
    assert result.returncode == 0, result.stderr
    assert count(no_password, "users") == 0

    with_password = tmp_path / "with-admin.db"
    result = run_init_db(with_password, ADMIN_PASSWORD="BootstrapPw!2026")
    assert result.returncode == 0, result.stderr
    assert count(with_password, "users") == 1

    conn = sqlite3.connect(with_password)
    try:
        username, is_admin = conn.execute(
            "SELECT username, is_admin FROM users").fetchone()
    finally:
        conn.close()
    assert username == "admin"
    assert is_admin


def test_warns_when_the_dataset_cannot_score_every_question(built):
    """The shipped dataset covers only some questions; say so rather than imply
    a complete questionnaire."""
    result = run_init_db(built)
    answerable = count(built, "answer_options")
    total = count(built, "questions")
    if answerable and total > answerable:
        assert "WARNING" in result.stdout
        assert "answer options" in result.stdout


def test_warns_when_the_database_holds_a_different_questionnaire(tmp_path):
    """Upgrading from a release whose questionnaire diverged must not be silent.

    Seeding never overwrites existing content, so a pre-2.0.0 database keeps its
    wrong questionnaire. Saying so is the difference between a confusing upgrade
    and a correct one.
    """
    db_path = tmp_path / "stale.db"
    result = run_init_db(db_path)
    assert result.returncode == 0, result.stderr

    conn = sqlite3.connect(db_path)
    try:
        conn.execute(
            "INSERT INTO domains (id, name, description, order_index) "
            "VALUES (99, 'Results', 'a domain this release does not ship', 99)")
        conn.commit()
    finally:
        conn.close()

    result = run_init_db(db_path)
    assert result.returncode == 0, result.stderr
    assert "WARNING" in result.stdout
    assert "--recreate" in result.stdout
