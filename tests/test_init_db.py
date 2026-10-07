"""The database bootstrap must work on a fresh clone, and be safe to re-run.

These run `scripts/init_db.py` as a subprocess against a throwaway DB_PATH,
which is exactly how a new contributor runs it.
"""
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
    assert count(built, "domains") == 6
    assert count(built, "aspects") == 30
    assert count(built, "questions") == 97


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
