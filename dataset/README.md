# Dataset

Source data for the questionnaire, derived from the SOC-CMM® framework
(version 2.3.3, basic) by Rob van Os — licensed CC BY-SA 4.0.
See [`../NOTICE`](../NOTICE) for the full attribution and license terms.

| File | Description |
| --- | --- |
| `soc-cmm2.3.3-basic.xlsx` | Original SOC-CMM® spreadsheet (upstream source). |
| `soc_cmm_complete_data.json` | Domains, aspects and questions extracted from the spreadsheet. |
| `soc_cmm_questions.json` | English questionnaire. |
| `soc_cmm_questions-port.json` | Portuguese (PT-BR) questionnaire. |
| `soc_cmm_port.txt` | Raw Portuguese translation text. |
| `traduzido.json` | Translated questions returned by the translation pass. |
| `questions_for_gemini_translation.json` | Export prepared for machine translation. |
| `import_template.json` | Shape expected when importing translated questions. |

`soc_cmm_complete_data.json` is the file `DatabaseManager.populate_initial_data()`
reads, and `sql/schema/database_schema.sql` is the one `init_database()` reads.
Note that **neither method is called automatically** — both calls are commented
out in `DatabaseManager.__init__` (`database.py`), so a fresh clone does not get
a seeded database on first run. See [`../sql/README.md`](../sql/README.md).

These files contain no user or customer data — only framework content.
