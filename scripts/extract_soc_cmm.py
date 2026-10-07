#!/usr/bin/env python3
"""Generate the questionnaire dataset from the official SOC-CMM(R) spreadsheet.

    python scripts/extract_soc_cmm.py

Reads `dataset/soc-cmm2.3.3-basic.xlsx` and writes
`dataset/soc_cmm_2.3.3_basic.json`, which `scripts/init_db.py` seeds from.

Why this exists
---------------
The questionnaire that previously shipped had been reconstructed by hand and
diverged badly from the framework: aspect names were evidently guessed from the
sheet codes ("CST" became "Cost" rather than "Customers", "DTE" became "Data &
Technology Exchange" rather than "Detection Engineering"), and `Results` was
scored as a sixth domain although the spreadsheet uses it only for output.
Generating from the workbook removes the guesswork and makes a future SOC-CMM
release a re-run rather than a re-transcription.

Where each piece comes from
---------------------------
`_Output`    the canonical spine: the five scored domains, their sections
             (aspect code + official name), every question id, its type
             (M = maturity, C = completeness) and its NIST CSF mapping.
`<Domain> - <CODE>` sheets
             question text (column C) and the per-question remarks the
             spreadsheet shows beside it (column P).
`_Guidance`  for each question, what maturity levels 1-5 mean in that
             question's own words. These become the answer options.
`_Input`     the generic answer scales, used for questions that have no
             per-question guidance of their own.

`General` (Profile, Scope) and `Results` (Results, NIST CSF Scoring, Results
Sharing) are deliberately not emitted: neither holds scored questions.
"""
import argparse
import json
import re
import sys
from collections import OrderedDict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

WORKBOOK = REPO_ROOT / "dataset" / "soc-cmm2.3.3-basic.xlsx"
OUTPUT = REPO_ROOT / "dataset" / "soc_cmm_2.3.3_basic.json"

SOURCE_VERSION = "2.3.3 (basic)"

# The spreadsheet keys questions by a domain letter that is not always the
# domain's initial: the Process domain uses "M" (management).
DOMAIN_LETTER = {
    "Business": "B",
    "People": "P",
    "Process": "M",
    "Technology": "T",
    "Services": "S",
}
SCORED_DOMAINS = list(DOMAIN_LETTER)

# Generic scales from the `_Input` sheet, for questions with no per-question
# guidance. "Not required" is an opt-out rather than a maturity level and is
# not emitted as a scored option.
GENERIC_SCALES = {
    "C": [
        (1, "Incomplete"),
        (2, "Partially complete"),
        (3, "Averagely complete"),
        (4, "Mostly complete"),
        (5, "Fully complete"),
    ],
    "M": [
        (1, "No"),
        (2, "Partially"),
        (3, "Averagely"),
        (4, "Mostly"),
        (5, "Fully"),
    ],
}

QUESTION_ID = re.compile(r"^([A-Z]{1,2})\s?(\d+(?:\.\d+)*)$")
SECTION = re.compile(r"^([A-Z]{1,2})(\d+)\s+-\s+(.+)$")


def log(message: str) -> None:
    print(f"[extract] {message}", flush=True)


def load_workbook():
    try:
        import openpyxl
    except ImportError:
        raise SystemExit(
            "openpyxl is required: pip install -r requirements-dev.txt"
        )
    if not WORKBOOK.exists():
        raise SystemExit(f"workbook not found: {WORKBOOK}")
    import warnings
    with warnings.catch_warnings():
        # The workbook uses Excel extensions openpyxl drops on read; none of
        # them carry content this script needs.
        warnings.simplefilter("ignore")
        return openpyxl.load_workbook(WORKBOOK, data_only=True)


def normalise_id(raw: str) -> str:
    """'B 1.1' and 'B1.1' both key the same question."""
    m = QUESTION_ID.match(str(raw).strip())
    return f"{m.group(1)} {m.group(2)}" if m else ""


def read_output_spine(wb):
    """The five scored domains, their sections, and each question's metadata."""
    ws = wb["_Output"]
    domain = None
    section = None
    sections = OrderedDict()   # (letter, number) -> {name, domain}
    questions = OrderedDict()  # qid -> {type, nist, section}
    for row in ws.iter_rows(min_row=2, max_col=9, values_only=True):
        cells = list(row) + [None] * 9
        label = str(cells[0]).strip() if cells[0] else ""
        if not label:
            continue
        if label.startswith("SOC-CMM -"):
            name = label.replace("SOC-CMM -", "").replace("Domain", "").strip()
            domain = name if name in DOMAIN_LETTER else None
            continue
        m = SECTION.match(label)
        if m:
            key = (m.group(1), int(m.group(2)))
            # A section can be listed under more than one domain block; the
            # first listing wins, which is the domain it belongs to.
            if key not in sections:
                owner = next((d for d, l in DOMAIN_LETTER.items() if l == key[0]), domain)
                sections[key] = {"name": m.group(3).strip(), "domain": owner}
            section = key
            continue
        qid = normalise_id(label)
        if qid and section and qid not in questions:
            qtype = str(cells[2]).strip() if cells[2] else ""
            nist = [str(c).strip() for c in (cells[5], cells[7]) if c and str(c).strip()]
            questions[qid] = {"type": qtype, "nist": nist, "section": section}
    return sections, questions


def read_guidance(wb):
    """Per-question descriptions of maturity levels 1-5."""
    ws = wb["_Guidance"]
    guidance = {}
    current = None
    for row in ws.iter_rows(min_row=2, max_col=3, values_only=True):
        label, level, text = (list(row) + [None] * 3)[:3]
        if label:
            candidate = normalise_id(label)
            if candidate:
                current = candidate
        if not current or level is None or not text:
            continue
        try:
            level = int(level)
        except (TypeError, ValueError):
            continue
        if 1 <= level <= 5:
            guidance.setdefault(current, {})[level] = str(text).strip()
    return guidance


def read_sheet_questions(wb):
    """Question text and remarks, keyed by question id, from the domain sheets."""
    found = {}
    aspect_names = {}
    for sheet_name in wb.sheetnames:
        if " - " not in sheet_name:
            continue
        domain = sheet_name.split(" - ")[0].strip()
        if domain not in DOMAIN_LETTER:
            continue
        letter = DOMAIN_LETTER[domain]
        ws = wb[sheet_name]

        aspect_number = None
        for row in ws.iter_rows(min_row=1, max_row=12, max_col=2):
            a, b = (list(row) + [None] * 2)[:2]
            if a is not None and b is not None and b.value:
                try:
                    aspect_number = int(str(a.value).strip())
                except (TypeError, ValueError):
                    continue
                # The heading on the sheet itself is what an assessor reads, and
                # it is the one place the official aspect name appears in full.
                # It is preferred over the _Output section name, which abbreviates
                # some of them, and over the sheet code, which is stale for a few
                # aspects (the "NDR" sheet is headed "IDPS Tooling").
                aspect_names[(letter, aspect_number)] = {
                    "name": str(b.value).strip(),
                    "code": sheet_name.split(" - ", 1)[1].strip(),
                    "domain": domain,
                    "number": aspect_number,
                }
                break
        if aspect_number is None:
            continue

        for row in ws.iter_rows(min_row=10, max_col=16):
            # Merged cells have no column_letter; index by position instead.
            cells = {}
            for offset, cell in enumerate(row):
                cells[chr(ord("A") + offset)] = cell.value
            number = cells.get("B")
            text = cells.get("C")
            if not number or not text:
                continue
            number = str(number).strip()
            if not re.match(r"^\d+(\.\d+)+$", number):
                continue
            text = str(text).strip()
            if not text or text.lower().startswith("specify rationale"):
                continue
            qid = f"{letter} {number}"
            remarks = cells.get("P")
            found[qid] = {
                "text": text,
                "remarks": str(remarks).strip() if remarks else "",
                "domain": domain,
                "sheet": sheet_name,
            }
    return found, aspect_names


def build(wb):
    sections, spine = read_output_spine(wb)
    guidance = read_guidance(wb)
    sheet_questions, sheet_aspect_names = read_sheet_questions(wb)

    domains = []
    for index, name in enumerate(SCORED_DOMAINS, start=1):
        domains.append({
            "id": index,
            "name": name,
            "description": f"{name} domain of the SOC-CMM framework",
            "order_index": index,
        })
    domain_id = {d["name"]: d["id"] for d in domains}

    aspects = []
    aspect_id = {}
    for key in sorted(sheet_aspect_names,
                      key=lambda k: (SCORED_DOMAINS.index(sheet_aspect_names[k]["domain"]), k[1])):
        meta = sheet_aspect_names[key]
        owner = meta["domain"]
        if owner not in domain_id:
            continue
        name = meta["name"]
        new_id = len(aspects) + 1
        aspect_id[key] = new_id
        aspects.append({
            "id": new_id,
            "domain_id": domain_id[owner],
            "name": name,
            "code": meta["code"],
            "description": f"{name} aspect of the {owner} domain",
            "order_index": meta["number"],
        })

    questions = []
    options = []
    skipped_no_text = 0
    skipped_no_options = 0
    for qid, meta in spine.items():
        section = meta["section"]
        if section not in aspect_id:
            continue
        sheet = sheet_questions.get(qid)
        if not sheet:
            skipped_no_text += 1
            continue

        levels = guidance.get(qid)
        if levels and len(levels) >= 2:
            scale = sorted((lv, text) for lv, text in levels.items())
        else:
            scale = GENERIC_SCALES.get(meta["type"], [])
        if not scale:
            skipped_no_options += 1
            continue

        qpk = len(questions) + 1
        questions.append({
            "id": qpk,
            "aspect_id": aspect_id[section],
            "code": qid,
            "question_text": sheet["text"],
            "question_type": "multiple_choice",
            "guidance": sheet["remarks"],
            "nist_csf": meta["nist"],
            "order_index": len(questions) + 1,
        })
        for order, (level, text) in enumerate(scale, start=1):
            options.append({
                "id": len(options) + 1,
                "question_id": qpk,
                "option_text": text,
                "maturity_level": level,
                "order_index": order,
            })

    return {
        "source": {
            "framework": "SOC-CMM(R)",
            "version": SOURCE_VERSION,
            "author": "Rob van Os",
            "url": "https://www.soc-cmm.com",
            "license": "CC BY-SA 4.0",
            "workbook": WORKBOOK.name,
            "generated_by": "scripts/extract_soc_cmm.py",
        },
        "domains": domains,
        "aspects": aspects,
        "questions": questions,
        "answer_options": options,
    }, {"no_text": skipped_no_text, "no_options": skipped_no_options}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--out", default=str(OUTPUT), help="output JSON path")
    parser.add_argument("--check", action="store_true",
                        help="report what would be written without writing it")
    args = parser.parse_args()

    wb = load_workbook()
    data, skipped = build(wb)

    by_domain = {}
    for a in data["aspects"]:
        name = next(d["name"] for d in data["domains"] if d["id"] == a["domain_id"])
        by_domain.setdefault(name, []).append(a["name"])

    log(f"source: {WORKBOOK.name} ({SOURCE_VERSION})")
    for name, names in by_domain.items():
        log(f"  {name}: {len(names)} aspects — {', '.join(names)}")
    scorable = len({o['question_id'] for o in data["answer_options"]})
    log(f"domains={len(data['domains'])} aspects={len(data['aspects'])} "
        f"questions={len(data['questions'])} options={len(data['answer_options'])}")
    log(f"questions with answer options: {scorable} of {len(data['questions'])}")
    if skipped["no_text"]:
        log(f"  {skipped['no_text']} question ids in _Output had no text on a domain "
            f"sheet (sub-items and totals) — not emitted")
    if skipped["no_options"]:
        log(f"  {skipped['no_options']} had no usable answer scale — not emitted")

    if args.check:
        log("--check: nothing written")
        return 0

    out = Path(args.out)
    out.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    log(f"wrote {out} ({out.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
