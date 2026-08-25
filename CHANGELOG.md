# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added

- Open-source readiness: `SECURITY.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`,
  GitHub issue/PR templates, and minimal CI
- Maintainer contact on privacy/terms pages and README Support section
- Documentation alignment with SOC-CMM® maturity scale (0–5) and non-affiliation notice

### Changed

- Repository reorganised for public release: the project root now holds only
  the application entrypoints and project metadata. Supporting files moved to
  `dataset/` (SOC-CMM® source data), `sql/{schema,seed,migrations}/`,
  `scripts/` (operational tooling) with `scripts/legacy/` for historical
  one-offs, and `tests/`
- `main.py` and `database.py` now resolve templates, static assets, the SQL
  schema and the seed dataset relative to the module location instead of the
  current working directory, so the app runs from any directory
- Renamed `soc cmm port.txt` to `dataset/soc_cmm_port.txt` (removed spaces)
- Added `README.md` files to `dataset/`, `sql/`, `scripts/`, `scripts/legacy/`
  and `tests/` describing contents and safe usage
- Documented the layout in a "Project Structure" section of the README

### Security

- Removed hard-coded credentials from the integration scripts in `tests/`;
  they now read `ADMIN_PASSWORD` / `TEST_USER_PASSWORD` from the environment
  and refuse to run when the admin password is unset

### Removed

- Tracked SQLite databases and backups (and purged from git history) to avoid
  shipping credentials or personal data
- Root draft/summary markdown files moved to `docs/archive/`

## [1.0.0] - 2025-07

### Added

- Initial SOC CMM Assessment System (FastAPI, SQLite, bilingual EN/PT-BR UI)
- Authentication, admin features, REST API, MCP server
- CC BY-SA 4.0 license and NOTICE with SOC-CMM® attribution
