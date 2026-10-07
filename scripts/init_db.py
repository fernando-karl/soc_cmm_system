#!/usr/bin/env python3
"""Create a ready-to-use SOC CMM database from scratch.

This is the one command a fresh clone needs before `python main.py`:

    python scripts/init_db.py

It is idempotent — running it again on an existing database adds whatever is
missing and leaves existing data alone.

Steps:

  1. base schema          sql/schema/database_schema.sql
  2. translation tables   sql/schema/bilingual_schema.sql
  3. migrations           sql/migrations/add_admin_field.sql
  4. questionnaire data   dataset/soc_cmm_complete_data.json
  5. admin user           only when ADMIN_PASSWORD is set

The database location follows the same rule as the application: `DB_PATH` if
set, otherwise `soc_cmm_bilingual.db` next to the application code.
"""
import argparse
import os
import sqlite3
import sys
from pathlib import Path

# This script lives outside the repository root; make the app modules importable.
REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from database import DatabaseManager, DEFAULT_DB_PATH, DATA_FILE, SCHEMA_FILE

BILINGUAL_SCHEMA = REPO_ROOT / "sql" / "schema" / "bilingual_schema.sql"
MIGRATIONS = [REPO_ROOT / "sql" / "migrations" / "add_admin_field.sql"]


def log(message: str) -> None:
    print(f"[init-db] {message}", flush=True)


def load_dataset():
    import json
    with open(DATA_FILE, "r", encoding="utf-8") as handle:
        return json.load(handle)


def apply_migration(db: DatabaseManager, path: Path) -> None:
    """Apply one migration, treating an already-applied one as success.

    SQLite has no `ADD COLUMN IF NOT EXISTS`, so re-running a migration that
    adds a column raises "duplicate column name". That means the migration is
    already in place, which is exactly the state we want.
    """
    try:
        db.apply_sql_file(path)
        log(f"applied migration {path.name}")
    except sqlite3.OperationalError as exc:
        if "duplicate column name" in str(exc).lower():
            log(f"migration {path.name} already applied")
        else:
            raise


def create_admin(db: DatabaseManager) -> None:
    """Create the initial admin user when ADMIN_PASSWORD is set."""
    password = os.environ.get("ADMIN_PASSWORD")
    if not password:
        log("ADMIN_PASSWORD not set — no admin user created")
        log("  set it and re-run, or register a user in the web interface")
        return

    # Imported here so the script still works for schema-only runs on a machine
    # without the auth dependencies installed.
    from auth import auth_manager

    username = os.environ.get("ADMIN_USERNAME", "admin")
    if auth_manager.get_user_by_username(username):
        log(f"user {username!r} already exists — leaving it untouched")
        return

    auth_manager.create_user(
        username=username,
        email=os.environ.get("ADMIN_EMAIL", "admin@soc-cmm.local"),
        password=password,
        full_name="Administrator",
        is_admin=True,
    )
    log(f"created admin user {username!r} — change the password after first login")


def summarise(db: DatabaseManager) -> None:
    conn = db.get_connection()
    try:
        counts = {}
        for table in ("domains", "aspects", "questions", "answer_options", "users"):
            try:
                counts[table] = conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
            except sqlite3.Error:
                counts[table] = "?"
        answerable = conn.execute(
            "SELECT COUNT(DISTINCT question_id) FROM answer_options"
        ).fetchone()[0]
    finally:
        conn.close()
    log("contents: " + ", ".join(f"{k}={v}" for k, v in counts.items()))

    total = counts.get("questions")
    if isinstance(total, int) and total and answerable < total:
        log("")
        log(f"WARNING: only {answerable} of {total} questions have answer options, so the")
        log("  rest cannot be scored yet. This is a gap in the shipped dataset")
        log(f"  ({DATA_FILE.name}), not a problem with this database. A fuller set of")
        log("  options exists in sql/seed/ but was generated for an older schema and")
        log("  does not load as is. See sql/README.md.")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create or update the SOC CMM database.",
        epilog="Set DB_PATH to choose where the database file lives.",
    )
    parser.add_argument(
        "--recreate",
        action="store_true",
        help="DELETE the existing database file first and build it from scratch. "
             "This destroys all users, customers and assessments.",
    )
    args = parser.parse_args()

    db_path = Path(DEFAULT_DB_PATH)
    log(f"database: {db_path}")

    for required in (SCHEMA_FILE, BILINGUAL_SCHEMA, DATA_FILE, *MIGRATIONS):
        if not Path(required).exists():
            log(f"ERROR: required file is missing: {required}")
            return 1

    if args.recreate and db_path.exists():
        confirm = os.environ.get("INIT_DB_ASSUME_YES") or input(
            f"Delete {db_path} and everything in it? Type 'yes' to confirm: "
        )
        if confirm.strip().lower() not in ("y", "yes"):
            log("aborted — nothing was changed")
            return 1
        db_path.unlink()
        log("deleted the existing database")

    existed = db_path.exists()
    db = DatabaseManager()

    db.init_database()
    log("base schema ready")

    db.apply_sql_file(BILINGUAL_SCHEMA)
    log("translation tables ready")

    for migration in MIGRATIONS:
        apply_migration(db, migration)

    conn = db.get_connection()
    try:
        existing = [r[0] for r in conn.execute("SELECT name FROM domains ORDER BY id")]
    finally:
        conn.close()

    if not existing:
        db.populate_initial_data()
        log("seeded the questionnaire from the SOC-CMM dataset")
    else:
        log(f"questionnaire already seeded ({len(existing)} domains) — left as is")
        expected = [d["name"] for d in load_dataset()["domains"]]
        if existing != expected:
            log("")
            log("WARNING: this database holds a different questionnaire than the one")
            log(f"  this version ships. Found {len(existing)} domains "
                f"({', '.join(existing)});")
            log(f"  expected {len(expected)} ({', '.join(expected)}).")
            log("  Seeding never overwrites existing content, so it has been left")
            log("  alone — but assessments scored against it do not match the")
            log("  current SOC-CMM release.")
            log("")
            log("  Versions before 2.0.0 shipped a questionnaire that diverged from")
            log("  the framework: aspects were misnamed (\"Cost\" for \"Customers\")")
            log("  and Results was scored as a sixth domain. To move to the correct")
            log("  questionnaire, export anything you need and rebuild:")
            log("      python scripts/init_db.py --recreate")
            log("  There is no in-place migration: question ids are not comparable")
            log("  between the two, so old answers cannot be carried across.")

    create_admin(db)
    summarise(db)

    log("done — start the application with: python main.py"
        if not existed else "done — existing database updated in place")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
