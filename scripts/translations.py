#!/usr/bin/env python3
"""Export and import questionnaire translations.

The questionnaire content is generated from the English SOC-CMM® workbook, so
every translation lives outside it, in `dataset/translations/<language>.json`.

    # write/refresh the file to translate
    python scripts/translations.py export --language pt_br

    # load it into a database
    python scripts/translations.py import --language pt_br

Export deduplicates: the 3110 answer options across the questionnaire are only
792 distinct strings, so a translator sees each phrase once. Import expands a
translated string back to every row that uses it.

Strings already translated keep their text on re-export, so running `export`
after a SOC-CMM release adds only what is new.
"""
import argparse
import json
import os
import re
import sqlite3
import sys
from collections import OrderedDict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from database import DatabaseManager, DEFAULT_DB_PATH, DATA_FILE

TRANSLATIONS_DIR = REPO_ROOT / "dataset" / "translations"

# Kinds map to the table that stores them and the column holding the text.
KINDS = {
    "domain": ("domain_translations", "domain_id", ("name",)),
    "aspect": ("aspect_translations", "aspect_id", ("name",)),
    "question": ("question_translations", "question_id", ("question_text",)),
    "option": ("answer_option_translations", "answer_option_id", ("option_text",)),
}


def log(message: str) -> None:
    print(f"[translations] {message}", flush=True)


def norm(text) -> str:
    return re.sub(r"\s+", " ", (text or "").strip())


def dataset():
    with open(DATA_FILE, "r", encoding="utf-8") as handle:
        return json.load(handle)


def source_strings(data):
    """Every distinct translatable string, with the kind it belongs to."""
    entries = OrderedDict()

    def add(kind, text):
        text = norm(text)
        if text and text not in entries:
            entries[text] = kind

    for domain in data["domains"]:
        add("domain", domain["name"])
    for aspect in data["aspects"]:
        add("aspect", aspect["name"])
    for question in data["questions"]:
        add("question", question["question_text"])
        add("guidance", question.get("guidance"))
    for option in data["answer_options"]:
        add("option", option["option_text"])
    return entries


def legacy_pt_pairs():
    """English -> Portuguese recovered from the pre-2.4.2 translation files.

    They are not aligned flat (741 English strings against 469 Portuguese), but
    walking both trees in parallel pairs what does line up. Treated as a
    starting point a human still reviews, never as authoritative.
    """
    en_file = REPO_ROOT / "dataset" / "soc_cmm_questions.json"
    pt_file = REPO_ROOT / "dataset" / "soc_cmm_questions-port.json"
    if not (en_file.exists() and pt_file.exists()):
        return {}
    english = json.loads(en_file.read_text(encoding="utf-8"))
    portuguese = json.loads(pt_file.read_text(encoding="utf-8"))

    pairs = {}

    def walk(a, b):
        if isinstance(a, dict) and isinstance(b, dict):
            for x, y in zip(list(a.keys()), list(b.keys())):
                walk(a[x], b[y])
        elif isinstance(a, list) and isinstance(b, list):
            for x, y in zip(a, b):
                walk(x, y)
        elif isinstance(a, str) and isinstance(b, str):
            if len(a) > 18 and len(b) > 8:
                pairs[norm(a)] = norm(b)

    walk(english, portuguese)
    return pairs


def do_export(language: str, path: Path) -> int:
    data = dataset()
    entries = source_strings(data)

    existing = {}
    if path.exists():
        previous = json.loads(path.read_text(encoding="utf-8"))
        existing = previous.get("strings", {})

    legacy = legacy_pt_pairs() if language == "pt_br" else {}

    strings = OrderedDict()
    kept = recovered = todo = 0
    for text, kind in entries.items():
        before = existing.get(text) or {}
        translated = norm(before.get("text"))
        origin = before.get("origin", "")
        if translated:
            kept += 1
        elif legacy.get(text):
            translated, origin = legacy[text], "legacy"
            recovered += 1
        else:
            todo += 1
        strings[text] = {
            "kind": kind,
            "text": translated,
            "origin": origin or ("" if translated else "untranslated"),
        }

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({
        "language": language,
        "source_version": data["source"]["version"],
        "note": ("Values are translations of the key. An empty 'text' is "
                 "untranslated. 'origin' records where a translation came from: "
                 "'legacy' is carried over from the pre-2.4.2 files and is "
                 "unreviewed, 'machine' is machine-translated, 'human' is "
                 "reviewed. Regenerate with scripts/translations.py export."),
        "strings": strings,
    }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    done = kept + recovered
    log(f"wrote {path}")
    log(f"  {len(strings)} distinct strings — {done} translated "
        f"({kept} kept, {recovered} recovered from the old files), {todo} to go")
    return 0


def do_import(language: str, path: Path, db_path: str) -> int:
    if not path.exists():
        log(f"ERROR: no translation file at {path} — run 'export' first")
        return 1
    payload = json.loads(path.read_text(encoding="utf-8"))
    strings = payload.get("strings", {})

    data = dataset()
    db = DatabaseManager(db_path) if db_path else DatabaseManager()
    conn = db.get_connection()
    cursor = conn.cursor()

    def translated(text):
        entry = strings.get(norm(text)) or {}
        return norm(entry.get("text"))

    written = {k: 0 for k in KINDS}

    for domain in data["domains"]:
        value = translated(domain["name"])
        if value:
            cursor.execute(
                "INSERT OR REPLACE INTO domain_translations "
                "(domain_id, language, name, description) VALUES (?,?,?,?)",
                (domain["id"], language, value, None))
            written["domain"] += 1

    for aspect in data["aspects"]:
        value = translated(aspect["name"])
        if value:
            cursor.execute(
                "INSERT OR REPLACE INTO aspect_translations "
                "(aspect_id, language, name, description) VALUES (?,?,?,?)",
                (aspect["id"], language, value, None))
            written["aspect"] += 1

    for question in data["questions"]:
        value = translated(question["question_text"])
        guidance = translated(question.get("guidance"))
        if value or guidance:
            cursor.execute(
                "INSERT OR REPLACE INTO question_translations "
                "(question_id, language, question_text, guidance) VALUES (?,?,?,?)",
                (question["id"], language, value or question["question_text"],
                 guidance or None))
            written["question"] += 1

    for option in data["answer_options"]:
        value = translated(option["option_text"])
        if value:
            cursor.execute(
                "INSERT OR REPLACE INTO answer_option_translations "
                "(answer_option_id, language, option_text) VALUES (?,?,?)",
                (option["id"], language, value))
            written["option"] += 1

    conn.commit()
    conn.close()
    log(f"imported into {db.db_path} for language {language!r}")
    for kind, count in written.items():
        log(f"  {kind}s: {count} rows")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("action", choices=("export", "import"))
    parser.add_argument("--language", default="pt_br",
                        help="language code as the application uses it (default: pt_br)")
    parser.add_argument("--file", default=None, help="translation file path")
    parser.add_argument("--db", default=None,
                        help=f"database to import into (default: {DEFAULT_DB_PATH})")
    args = parser.parse_args()

    path = Path(args.file) if args.file else TRANSLATIONS_DIR / f"{args.language}.json"
    if args.action == "export":
        return do_export(args.language, path)
    return do_import(args.language, path, args.db)


if __name__ == "__main__":
    raise SystemExit(main())
