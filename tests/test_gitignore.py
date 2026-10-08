"""No database or database backup may ever be committable.

A `v2.0.0` tag was once pushed from a stale local branch and republished twelve
SQLite databases — including bcrypt password hashes — that had been purged from
history. The backup that was sitting untracked at the time,
`soc_cmm_bilingual.db.bak_<timestamp>`, was not matched by `.gitignore`: it has
a suffix after `.db`, so `*.db` misses it, and it ends in `.bak_<timestamp>`
rather than `.bak`, so that pattern misses it too.

These assert that every backup name the project's own scripts can write is
ignored, so `git add -A` cannot stage a live database.
"""
import subprocess
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]

# Each entry is a name some script in this repository actually writes.
#   scripts/migrate_to_auth.py                     <db>.backup_<timestamp>
#   scripts/run_admin_migration.py                 <db>.backup_admin_<timestamp>
#   scripts/migrate_bilingual.py                   <db>.bak_<timestamp>
#   scripts/legacy/create_translated_database_safe.py
#                                                  soc_cmm_backup_<timestamp>.db
MUST_BE_IGNORED = [
    "soc_cmm.db",
    "soc_cmm_bilingual.db",
    "soc_cmm_bilingual.db.bak_20260519_131025",
    "soc_cmm_bilingual.db.backup_20250711_204932",
    "soc_cmm_bilingual.db.backup_admin_20250803_104157",
    "soc_cmm_backup_20250711_204932.db",
    "soc_cmm_translated.db.backup_20250726_005820",
    "soc_cmm.db-journal",
    "soc_cmm.db-wal",
    "soc_cmm.db-shm",
    "data.sqlite",
    "data.sqlite3",
    "anything.bak",
    "anything.backup",
    ".env",
]

# Files the repository must keep tracking — a broad ignore rule that swallowed
# one of these would be worse than the hole it closed.
MUST_NOT_BE_IGNORED = [
    "README.md",
    "database.py",
    "dataset/soc_cmm_2.4.2_advanced.json",
    "dataset/soc-cmm-2.4.2-advanced.xlsx",
    "dataset/translations/pt_br.json",
    "sql/schema/database_schema.sql",
    "sql/migrations/add_answer_importance.sql",
    ".env.example",
]


def ignored(path):
    """True when git would refuse to stage `path`."""
    return subprocess.run(
        ["git", "check-ignore", "-q", path],
        cwd=REPO_ROOT, capture_output=True).returncode == 0


@pytest.mark.parametrize("path", MUST_BE_IGNORED)
def test_databases_and_backups_cannot_be_committed(path):
    assert ignored(path), (
        f"{path} is NOT ignored — `git add -A` would stage it. "
        "Every name the migration scripts write must be covered.")


@pytest.mark.parametrize("path", MUST_NOT_BE_IGNORED)
def test_the_rules_do_not_swallow_tracked_files(path):
    assert not ignored(path), f"{path} is ignored but the repository tracks it"


def test_no_tracked_file_is_ignored():
    """Catches an over-broad rule against the whole index, not just a sample."""
    tracked = subprocess.run(["git", "ls-files"], cwd=REPO_ROOT,
                             capture_output=True, text=True, check=True).stdout
    clash = subprocess.run(["git", "check-ignore", "--stdin"], cwd=REPO_ROOT,
                           input=tracked, capture_output=True, text=True)
    assert not clash.stdout.strip(), (
        "these tracked files are now ignored:\n" + clash.stdout)


def test_no_database_is_tracked():
    """The state the history purge established, asserted rather than assumed."""
    tracked = subprocess.run(["git", "ls-files"], cwd=REPO_ROOT,
                             capture_output=True, text=True, check=True).stdout
    offenders = [line for line in tracked.splitlines()
                 if (".db" in line or ".sqlite" in line)
                 and not line.endswith((".py", ".md", ".sql", ".json", ".yml"))]
    assert not offenders, f"database files are tracked: {offenders}"
