# Manual check scripts

These are **manual integration scripts**, not an automated test suite. Each one
drives the HTTP API of a locally running instance and prints results for a human
to read; there are no assertions collected by a test runner.

They are named `check_*.py` rather than `test_*.py` on purpose, so `pytest` does
not collect them. There is currently no automated test suite — adding one is a
welcome contribution (see [`../../CONTRIBUTING.md`](../../CONTRIBUTING.md)); real
`pytest` tests belong in `tests/` alongside this directory.

## Requirements

1. A running server on `http://localhost:8400`:
   ```bash
   python main.py
   ```
2. Packages that are **not** application dependencies:
   ```bash
   pip install requests beautifulsoup4
   ```
   `requests` is used by all of them; `beautifulsoup4` by
   `check_dropdown_visibility.py`, `check_flag_icons.py` and
   `check_language_dropdown.py`.
3. Credentials via environment variables (never hard-coded):
   - `ADMIN_PASSWORD` — the admin password of your local instance, required by
     the scripts that log in as `admin`.
   - `TEST_USER_PASSWORD` — optional password for the disposable user that
     `check_admin_access.py` creates.

## Running

From the repository root:

```bash
ADMIN_PASSWORD='...' python tests/manual/check_auth.py
```

> **Warning:** these scripts create users, customers, and assessments. Run them
> against a disposable local database only — never against production data.
