# Generated questionnaire dataset

`soc_cmm_2.3.3_basic.json` is generated from the official workbook by
`python scripts/extract_soc_cmm.py`. Do not edit it by hand — regenerate it.

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
