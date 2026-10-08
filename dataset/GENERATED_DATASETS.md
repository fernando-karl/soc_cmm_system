# Generated questionnaire datasets

Generated from the official SOC-CMM® workbooks by
`scripts/extract_soc_cmm.py`. Do not edit them by hand — regenerate.

```bash
# 2.4.2 advanced (the default, and what the application seeds)
python scripts/extract_soc_cmm.py

# 2.3.3 basic
python scripts/extract_soc_cmm.py \
    --workbook dataset/soc-cmm2.3.3-basic.xlsx \
    --version "2.3.3 (basic)" \
    --out dataset/soc_cmm_2.3.3_basic.json
```

| Version | Domains | Aspects | Questions | Options | NIST |
| --- | --- | --- | --- | --- | --- |
| 2.3.3 (basic) | 5 | 26 | 664 | 3320 | CSF 1.1 |
| 2.4.2 (advanced) | 5 | 27 | 649 | 3245 | CSF 2.0 |

Both are released by SOC-CMM® under CC BY-SA 4.0; the advanced workbook states
this itself ("The SOC-CMM advanced version is part of the SOC-CMM®. The
SOC-CMM® assessment tool is free software, released under the CC SA-BY
license").

The same extractor reads both without modification. 2.4.2 moves Log Management
from Services into Process, adds Automation Engineering, renames the Technology
aspects to Log / Network / Endpoint Monitoring and SecOps Automation, and
broadens Business "Customers" to "Customers / Stakeholders". Column positions in
`_Output` also moved, so the NIST columns are located by their header rather
than by position.

Each question is filed under the aspect its own id names (`S 2.3.1` belongs to
Services aspect 2), not under the last section header the extractor passed in
`_Output`. Up to 2.0.1 it used the header, which mis-filed 270 of the 2.4.2
questions and 283 of the 2.3.3 ones: `_Output` writes some headers with a space
(`S 2 - ...`) and re-lists capability items under `M5`. Security Incident
Management and Forensics came out empty, and 27 questions were dropped.
`tests/test_dataset_integrity.py` now checks every id against its aspect and
that the committed JSON matches a fresh extraction.

## Why it was regenerated

The dataset that shipped before (`soc_cmm_complete_data.json`) had been
reconstructed by hand and diverged from SOC-CMM® 2.3.3 in ways that would
misrepresent the framework:

| Sheet code | Official aspect | Previously shipped as |
| --- | --- | --- |
| CST | Customers | Cost |
| R&H | Roles and Hierarchy | Retention & Hiring |
| PEM | People Management | Performance Management |
| O&F | Operations and Facilities | Operations & Functions |
| DTE | Detection Engineering & Validation | Data & Technology Exchange |
| A&O | Automation & Orchestration Tooling | Analytics & Orchestration |
| SCM | Security Monitoring | Service Catalog Management |
| SIM (Services) | Security Incident Management | Security Information Management |
| THR | Threat Intelligence | Threat Hunting & Research |

The pattern is consistent with names having been inferred from the three-letter
sheet codes rather than read from the sheets.

`Results` was also scored as a sixth domain. In the workbook, `Results` holds
the output (Results, NIST CSF Scoring, Results Sharing) and contains no scored
questions — `_Output` enumerates exactly five scored domains. `General`
(Profile, Scope) is likewise informational.

## What the generated dataset contains

- **5 domains**: Business, People, Process, Technology, Services
- **26 aspects**, named from each sheet's own heading — the name an assessor
  reads. Note that a few sheet *codes* are stale in the workbook itself: the
  sheet coded `NDR` is headed "IDPS Tooling" and `EDR` is headed "Security
  Analytics Tooling". The heading wins.
- **664 scored questions**, each with its NIST CSF mapping where the workbook
  provides one
- **3320 answer options** — five per question, taken from the `_Guidance`
  sheet, so each option is that question's own description of what maturity
  levels 1–5 mean rather than a generic label

Every question is scorable, and an assessment answered at level 5 throughout
scores 5.0/5 (100%), which matches `calculate_assessment_scores`.

## What is deliberately not included

271 rows in the workbook are inventory checklists rather than maturity
questions — "Please specify your customers:" followed by Legal, Audit, IT and
so on. They carry no maturity level and are not scored by the spreadsheet
either, so they are not emitted.

---

Derived from the SOC-CMM® framework by Rob van Os, licensed CC BY-SA 4.0.
See [`../NOTICE`](../NOTICE). Not affiliated with soc-cmm.com.
