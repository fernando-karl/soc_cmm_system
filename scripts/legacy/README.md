# Legacy scripts

Historical, one-off scripts used while building the questionnaire dataset and
the Portuguese translation. They are kept for provenance and reproducibility of
the data in `dataset/` and `sql/`, **not** as a supported workflow.

Expect rough edges:

- Several scripts are near-duplicates representing successive attempts
  (`create_portuguese_database.py`, `..._correct.py`, `..._fixed.py`).
- They assume a specific database state and will fail or corrupt data if run
  out of order.
- Some depend on packages that are not in `requirements.txt`
  (for example `openpyxl` for the Excel extraction scripts).

They expect to be run from the repository root, e.g.:

```bash
python scripts/legacy/extract_questions_from_excel.py
```

**Do not run these against a database you care about.** If you only want a
working instance, follow the installation guide in `docs/` instead.
