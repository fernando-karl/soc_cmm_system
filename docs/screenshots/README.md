# Screenshots

Captured from a local instance running **2.1.0**, seeded with demo data — a
fictional customer, "Northwind Energy", with two assessments six months apart.
No real assessment data appears here.

Regenerate them with `python scripts/capture_screenshots.py` (see
[`../../scripts/capture_screenshots.py`](../../scripts/capture_screenshots.py)
for the options) so a release can refresh the gallery instead of leaving
screenshots that show counts and scores the software no longer produces.

## English interface

| | |
| --- | --- |
| **Sign in** — SOC-CMM® attribution is shown on every page, including the public ones.<br>![Login](01-login.png) | **Register**<br>![Register](02-register.png) |
| **Dashboard** — assessment overview for the signed-in user.<br>![Dashboard](03-dashboard.png) | **Customers** — multiple client organisations, scoped per user.<br>![Customers](04-customers.png) |

### Guided questionnaire
Step-by-step through the five SOC-CMM® domains and their 27 aspects — 649
questions in all. Each question carries the workbook's own guidance, and each
of its five maturity levels is worded for that specific question rather than
with a generic label.

![Questionnaire](05-assessment-questionnaire.png)

### Results
Radar chart across the five scored domains. Scores follow the official
SOC-CMM® formula, so the lowest answer reads 0% rather than a fifth of the
scale.

![Radar chart](06-results-radar.png)

Overall maturity gauge above the radar, with the per-domain and per-aspect
breakdown and progress over time further down the page.

![Results overview](15-results-overview.png)

### Attribution
The About page carries the full SOC-CMM® attribution, license and
non-affiliation notice.

![About / attribution](07-about-attribution.png)

### Administration

| | |
| --- | --- |
| ![Admin dashboard](08-admin-dashboard.png) | ![User management](09-admin-users.png) |

## Portuguese (PT-BR) interface

Not only the interface: all 649 questions, their guidance and all 3245 answer
options are translated, so the assessment itself is in Portuguese. Most of that
is machine-translated and unreviewed — see
[help wanted: review the Brazilian Portuguese translation](https://github.com/fernando-karl/soc_cmm_system/issues/22).

| | |
| --- | --- |
| ![Questionário PT-BR](14-questionnaire-pt-br.png) | ![Sobre nós PT-BR](11-about-pt-br.png) |

![Resultados PT-BR](10-results-pt-br.png)

## Mobile

| | |
| --- | --- |
| ![Mobile dashboard](12-mobile-dashboard.png) | ![Mobile results](13-mobile-results.png) |

---

Built on the [SOC-CMM®](https://www.soc-cmm.com) framework by Rob van Os,
licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
Not affiliated with or endorsed by soc-cmm.com. See [`../../NOTICE`](../../NOTICE).
