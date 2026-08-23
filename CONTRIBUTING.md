# Contributing

Thank you for considering a contribution to the SOC CMM Assessment System.

> **License:** This project is **CC BY-SA 4.0**. Contributions are accepted
> under the same license. Please read [`LICENSE`](LICENSE) and
> [`NOTICE`](NOTICE). This software is a derivative of the SOC-CMM®
> framework by Rob van Os (<https://www.soc-cmm.com>) and is **not
> affiliated with** soc-cmm.com.

Portuguese version: [`docs/pt-br/contribuindo.md`](docs/pt-br/contribuindo.md).

## Development setup

1. Fork and clone the repository
2. Create a virtualenv and install dependencies: `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and set `SECRET_KEY` and `ADMIN_PASSWORD`
4. Bootstrap auth: `python migrate_to_auth.py`
5. Run: `python main.py` (default port `8400`)

Do **not** commit `.env`, `*.db`, or real assessment data.

## Pull requests

- Open an issue first for large changes
- Keep PRs focused; one logical change per PR
- Update `docs/en/` and `docs/pt-br/` together when behaviour or install steps change
- Follow existing code style (FastAPI + Jinja2 templates)
- Add or update tests under `test_*.py` when touching auth or API behaviour

## Code of conduct

See [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).

## Security

See [`SECURITY.md`](SECURITY.md). Do not disclose vulnerabilities in public issues.

## Attribution

When documenting or redistributing, credit:

1. Rob van Os / SOC-CMM® (<https://www.soc-cmm.com>)
2. This project and its contributors
