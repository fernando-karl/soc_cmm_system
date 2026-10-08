"""Structural checks on the shipped SOC-CMM(R) questionnaire datasets.

The extractor once filed questions under the last section header it had passed
in the workbook's `_Output` sheet. Two quirks of that sheet broke it: some
headers carry a space between letter and number ("S 2 - ..."), and a block near
the end re-lists capability items from other aspects under "M5". The result was
that 270 of 622 questions (2.4.2) and 283 of 664 (2.3.3) sat under the wrong
aspect, and Security Incident Management and Forensics had no questions at all.

Every question id encodes its own aspect ("S 2.3.1" is Services aspect 2), so
these tests check the datasets against that, rather than against a count that
would have to be updated by hand on every SOC-CMM release.
"""
import json
import re
from collections import Counter
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
DATASETS = [
    REPO_ROOT / "dataset" / "soc_cmm_2.4.2_advanced.json",
    REPO_ROOT / "dataset" / "soc_cmm_2.3.3_basic.json",
]
TRANSLATIONS = sorted((REPO_ROOT / "dataset" / "translations").glob("*.json"))

# Domain order in the datasets -> the letter SOC-CMM uses in question ids.
# Process is "M" (management) in the workbook.
DOMAIN_LETTER = {"Business": "B", "People": "P", "Process": "M",
                 "Technology": "T", "Services": "S"}
CODE = re.compile(r"^([A-Z]{1,2})\s?(\d+)")


def _load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def _aspect_keys(data):
    """aspect id -> (domain letter, aspect number), e.g. ("S", 2)."""
    letters = {d["id"]: DOMAIN_LETTER[d["name"]] for d in data["domains"]}
    return {a["id"]: (letters[a["domain_id"]], a["order_index"])
            for a in data["aspects"]}


@pytest.mark.parametrize("path", DATASETS, ids=lambda p: p.name)
def test_every_question_sits_under_the_aspect_its_code_names(path):
    data = _load(path)
    keys = _aspect_keys(data)
    wrong = []
    for q in data["questions"]:
        m = CODE.match(q["code"])
        assert m, f"unrecognised question code {q['code']!r}"
        expected = (m.group(1), int(m.group(2)))
        if keys[q["aspect_id"]] != expected:
            wrong.append(q["code"])
    assert not wrong, (
        f"{len(wrong)} of {len(data['questions'])} questions are under the wrong "
        f"aspect, e.g. {wrong[:5]}")


@pytest.mark.parametrize("path", DATASETS, ids=lambda p: p.name)
def test_every_aspect_has_questions(path):
    data = _load(path)
    per_aspect = Counter(q["aspect_id"] for q in data["questions"])
    empty = [a["name"] for a in data["aspects"] if not per_aspect[a["id"]]]
    assert not empty, f"aspects with no questions: {empty}"


@pytest.mark.parametrize("path", DATASETS, ids=lambda p: p.name)
def test_question_codes_are_unique(path):
    data = _load(path)
    codes = Counter(q["code"] for q in data["questions"])
    dupes = [c for c, n in codes.items() if n > 1]
    assert not dupes, f"duplicate question codes: {dupes[:5]}"


@pytest.mark.parametrize("path", TRANSLATIONS, ids=lambda p: p.name)
def test_translation_files_have_no_gaps(path):
    """An empty string is shown to users as an untranslated English fallback."""
    strings = _load(path)["strings"]
    missing = [k for k, v in strings.items() if not v.get("text")]
    assert not missing, f"{len(missing)} untranslated strings, e.g. {missing[:3]}"


def test_shipped_dataset_matches_the_workbook():
    """The committed JSON must be what the extractor produces today.

    Catches a fix to the extractor that was never followed by a regeneration,
    which is exactly how a mis-filed dataset could survive a correct script.
    """
    pytest.importorskip("openpyxl")
    import sys
    sys.path.insert(0, str(REPO_ROOT / "scripts"))
    import extract_soc_cmm as extractor

    wb, workbook = extractor.load_workbook(None)
    fresh, _ = extractor.build(wb, workbook_name=workbook.name)
    shipped = _load(extractor.OUTPUT)
    assert fresh["questions"] == shipped["questions"], (
        "dataset/soc_cmm_2.4.2_advanced.json is out of date: "
        "run python scripts/extract_soc_cmm.py")
    assert fresh["aspects"] == shipped["aspects"]
    assert fresh["answer_options"] == shipped["answer_options"]
