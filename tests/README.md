# Tests

These are **manual integration scripts**, not an automated unit-test suite.
Each one drives the HTTP API of a locally running instance and prints results
for a human to read; there are no assertions collected by a test runner.

## Requirements

1. A running server on `http://localhost:8400`:
   ```bash
   python main.py
   ```
2. The `requests` package, which is not an application dependency:
   ```bash
   pip install requests
   ```
3. Credentials via environment variables (never hard-coded):
   - `ADMIN_PASSWORD` — the admin password of your local instance (required
     by the scripts that log in as `admin`).
   - `TEST_USER_PASSWORD` — optional password for the disposable user that
     `test_admin_access.py` creates.

## Running

From the repository root:

```bash
ADMIN_PASSWORD='...' python tests/test_auth.py
```

> **Warning:** these scripts create users, customers, and assessments. Run them
> against a disposable local database only — never against production data.

Contributions that convert these into a proper `pytest` suite are welcome; see
[`../CONTRIBUTING.md`](../CONTRIBUTING.md).
