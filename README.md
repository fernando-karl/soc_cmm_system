# SOC CMM Assessment System

A comprehensive Security Operations Center Capability Maturity Model assessment
system built with FastAPI, SQLite, and modern web technologies.

> **Attribution:** This project is a derivative work of the **SOC-CMM®
> framework** created by **Rob van Os** (<https://www.soc-cmm.com>) and
> distributed under the [Creative Commons Attribution-ShareAlike 4.0
> International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/)
> license. In compliance with the ShareAlike requirement, this entire
> project is also licensed under **CC BY-SA 4.0**. See [`LICENSE`](LICENSE)
> and [`NOTICE`](NOTICE) for full details.

## Features

- **Customer Management**: Create and manage multiple customers/organizations
- **Step-by-Step Assessment**: Guided questionnaire broken into manageable sections by domain and aspect
- **Maturity Evaluation**: SOC-CMM® maturity scale (0–5: Non-existent through Optimizing), as implemented in the questionnaire scoring
- **Visual Results**: Interactive radar charts showing maturity levels across all domains
- **Progress Tracking**: Multiple assessments per customer to track improvements over time
- **Mobile Optimized**: Responsive design for desktop and mobile devices
- **Modern UI**: Clean, professional interface with smooth animations and interactions

## SOC CMM Domains

The assessment covers six key domains:

1. **Business** - Strategy, governance, cost management, and privacy
2. **People** - Employment, training, performance, and knowledge management
3. **Process** - Management, operations, reporting, and use case management
4. **Technology** - Security information management, detection, and analytics
5. **Services** - Service catalog, analysis, threat hunting, and vulnerability management
6. **Results** - Overview, critical success factors, and sharing

## Technology Stack

- **Backend**: FastAPI (Python 3.11+)
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3, JavaScript with Jinja2 templates
- **Visualization**: Chart.js for radar charts and progress tracking
- **Styling**: Modern CSS with responsive design
- **Icons**: Font Awesome

## Documentation

Full documentation is available in two languages:

- **English:** [`docs/en/`](docs/en/README.md)
- **Português (Brasil):** [`docs/pt-br/`](docs/pt-br/README.md)

Also see [`CONTRIBUTING.md`](CONTRIBUTING.md), [`SECURITY.md`](SECURITY.md),
and [`CHANGELOG.md`](CHANGELOG.md).

Documentação completa em dois idiomas:

- **English:** [`docs/en/`](docs/en/README.md)
- **Português (Brasil):** [`docs/pt-br/`](docs/pt-br/README.md)

## Installation

> **Looking for a deeper guide?** See
> [`docs/en/installation.md`](docs/en/installation.md) (English) or
> [`docs/pt-br/instalacao.md`](docs/pt-br/instalacao.md) (Portuguese).

### Prerequisites

- Python **3.11** or higher
- `pip`
- Optional: Docker + Docker Compose (containerised flow)

### Quick start

```bash
# 1. Clone the repository
git clone https://github.com/fernando-karl/soc_cmm_system.git
cd soc_cmm_system

# 2. Install dependencies (use a virtualenv if you prefer)
pip install -r requirements.txt

# 3. Configure environment variables
cp .env.example .env
# edit .env and set at least SECRET_KEY and ADMIN_PASSWORD
# generate SECRET_KEY:
#   python -c "import secrets; print(secrets.token_urlsafe(48))"

# 4. Bootstrap the database (creates the admin user from $ADMIN_PASSWORD)
export ADMIN_PASSWORD="your-strong-password"
python migrate_to_auth.py

# 5. Start the application
python main.py
```

The application listens on **port 8400** by default. Override with
`PORT=9000 python main.py`. Browse to <http://localhost:8400>, log in as
`admin` with `$ADMIN_PASSWORD`, and **change the password right away**.

### Required environment variables

| Variable                      | Required | Description                                                                                                          |
| ----------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------- |
| `SECRET_KEY`                  | **Yes**  | Secret used to sign JWT tokens. The application refuses to start without it.                                          |
| `ADMIN_PASSWORD`              | **Yes**¹ | Initial password for the bootstrap admin account created by `migrate_to_auth.py`.                                     |
| `ALLOWED_ORIGINS`             | No       | Comma-separated list of CORS origins. Defaults to `http://localhost:8400`. Use `*` only in trusted networks.          |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | No       | JWT lifetime in minutes (default: `30`).                                                                              |
| `HOST`, `PORT`                | No       | Network interface and port (defaults: `0.0.0.0` and `8400`).                                                          |
| `ADMIN_EMAIL`                 | No       | Email for the bootstrap admin user (default: `admin@soc-cmm.local`).                                                  |

¹ Required only for the initial migration. Unset it after the first login
and password change.

### Docker

```bash
cp .env.example .env             # set SECRET_KEY, ADMIN_PASSWORD
docker compose up -d --build
docker compose exec soc-cmm python migrate_to_auth.py
```

See [`docs/en/docker.md`](docs/en/docker.md) for the full Docker guide.

## Usage

> **Detailed walkthrough:** [`docs/en/usage.md`](docs/en/usage.md) (English)
> or [`docs/pt-br/uso.md`](docs/pt-br/uso.md) (Portuguese).

### 1. Log in or register

- Browse to <http://localhost:8400>.
- Log in as `admin` with the password you set in `ADMIN_PASSWORD` (first
  run only) or register a new account at `/register`.
- Each user only sees their **own** customers and assessments.
- Change the admin password from the profile page after the first login.

### 2. Manage customers

- Navigate to **Customers** and click **Add Customer**.
- Provide a name (required) plus optional email and organisation.

### 3. Run an assessment

- From the customer list, click **New Assessment**.
- Answer the questionnaire by domain and aspect (Business, People,
  Process, Technology, Services, Results).
- The assessment supports multiple question types: maturity scale
  (SOC-CMM® 0–5), multiple choice, numeric, free text, and checkboxes.
- Answers autosave; the progress bar shows what is still pending.
- When every aspect is complete, click **Complete Assessment**.

### 4. View results

- The results page shows a **radar chart** with maturity per domain,
  detailed per-aspect scores, and an export option.
- Run multiple assessments per customer to track progress over time.

### 5. Switch language (EN/PT-BR)

- Use the 🇺🇸 / 🇧🇷 flags in the top bar.
- The choice is stored in a `language` cookie (1 year).

## API Endpoints

### Customer Management
- `POST /api/customers` - Create new customer
- `GET /api/customers` - List all customers
- `GET /api/customers/{id}` - Get customer details

### Assessment Management
- `POST /api/assessments` - Create new assessment
- `GET /api/customers/{id}/assessments` - Get customer assessments
- `GET /api/assessments/{id}` - Get assessment details
- `PUT /api/assessments/{id}/complete` - Mark assessment as complete

### Questionnaire
- `GET /api/domains` - Get all domains
- `GET /api/domains/{id}/aspects` - Get aspects for domain
- `GET /api/aspects/{id}/questions` - Get questions for aspect
- `POST /api/answers` - Submit answers

### Results and Analytics
- `GET /api/assessments/{id}/scores` - Get assessment scores
- `GET /api/assessments/{id}/radar-data` - Get radar chart data
- `GET /api/customers/{id}/progress` - Get progress over time

## Database Schema

The system uses SQLite with the following main tables:

- **customers** - Customer information
- **domains** - SOC CMM domains
- **aspects** - Domain aspects/subcategories
- **questions** - Assessment questions
- **answer_options** - Multiple choice options with maturity levels
- **assessments** - Assessment instances
- **assessment_answers** - User responses
- **assessment_scores** - Calculated scores

## Customization

### Adding or editing questions

The questionnaire data lives directly in the SQLite database (the
`domains`, `aspects`, `questions`, and `answer_options` tables — see
[`docs/en/database.md`](docs/en/database.md)). Edit it via SQL, via the
admin pages, or rebuild the database from the seed scripts
(`run_populate_database_fixed.py`, `complete_populate_database.sql`).

> Editing `soc_cmm_complete_data.json` after the first install will **not**
> be reloaded automatically — the database is the source of truth at
> runtime.

### Styling

- Modify `static/css/style.css` for visual customisation.
- Update CSS variables under `:root` to change the colour scheme.

### Functionality

- Extend `static/js/main.js` for additional JavaScript functionality.
- Modify templates in `templates/` for layout changes (templates exist in
  EN and `*_pt_br.html` variants).

## Mobile Optimization

The system is fully responsive and optimized for mobile devices:

- Touch-friendly interface elements
- Responsive grid layouts
- Optimized form inputs
- Mobile navigation patterns
- Progressive web app capabilities

## Security Considerations

- **Authentication is required.** All assessment data is scoped per user via
  JWT-based authentication (`auth.py`).
- The application **refuses to start** if `SECRET_KEY` is not configured —
  there is no insecure fallback.
- The bootstrap admin password must be supplied through the
  `ADMIN_PASSWORD` environment variable; there is **no hard-coded default**.
- **CORS** is restricted to the origins listed in the `ALLOWED_ORIGINS`
  environment variable (default: `http://localhost:8400`).
- All database queries use parameterized statements to prevent SQL
  injection.
- **Never commit `.env` files or `*.db` files** — both are excluded by
  `.gitignore`.
- For production: run behind a reverse proxy (nginx/Caddy) with TLS, set
  short `ACCESS_TOKEN_EXPIRE_MINUTES`, and rotate `SECRET_KEY` periodically.

## Deployment

### Local development

```bash
python main.py
```

### Docker

A production-style `Dockerfile` and `docker-compose.yml` are included.
See [`docs/en/docker.md`](docs/en/docker.md) for details.

### Production checklist

1. Run behind a reverse proxy (nginx, Caddy, Traefik) terminating TLS.
2. Restrict `ALLOWED_ORIGINS` to your real domains (never `*`).
3. Set a strong `SECRET_KEY` and rotate it periodically.
4. Change the admin password and unset `ADMIN_PASSWORD` after the
   migration.
5. Persist the database under a mounted volume (or migrate to PostgreSQL/
   MySQL for multi-user installs).
6. Configure structured logging and regular backups.
7. Consider running uvicorn with multiple workers behind the proxy
   (`uvicorn main:app --workers 4`) instead of `python main.py`.

## Troubleshooting

Common issues and fixes — see also
[`docs/en/troubleshooting.md`](docs/en/troubleshooting.md):

- **`SECRET_KEY environment variable is required`** — define it in `.env`
  or export it before starting.
- **`ADMIN_PASSWORD environment variable is required`** — set it before
  running `migrate_to_auth.py`.
- **Port conflict** — change with `PORT=9000 python main.py`.
- **CORS errors** — list your origin in `ALLOWED_ORIGINS`.
- **Missing dependencies** — `pip install -r requirements.txt`.
- **Logs** — check the uvicorn console; for Docker, run
  `docker compose logs -f soc-cmm`.

## Support

Maintainer contact for this project (not affiliated with soc-cmm.com):

- **Email:** fernando.karl@gmail.com
- **GitHub Issues:** <https://github.com/fernando-karl/soc_cmm_system/issues>

For self-help:
1. Check [Troubleshooting](docs/en/troubleshooting.md) / [Solução de problemas](docs/pt-br/solucao_de_problemas.md)
2. Review the API docs (`docs/en/api.md` or Swagger at `/docs`)
3. Examine the browser console for JavaScript errors
4. Check server logs for backend issues

## License & Attribution

This software is distributed under the **Creative Commons
Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0)**.

The SOC-CMM® framework on which this project is based was created by
**Rob van Os** and is also published under CC BY-SA 4.0
(<https://www.soc-cmm.com>). Because the SOC-CMM ShareAlike clause requires
derivative works to be released under the same license, the entirety of this
repository — source code, documentation, translations and database content
derived from the SOC-CMM® materials — is licensed under CC BY-SA 4.0.

Summary of your rights and obligations:

- You may **share** and **adapt** the material, including for commercial
  purposes.
- You **must give credit** to Rob van Os and to the SOC-CMM® framework, link
  to the license, and indicate any changes you have made.
- You **must distribute** any derivative work under the same CC BY-SA 4.0
  license.

See [`LICENSE`](LICENSE) for the full license summary and
[`NOTICE`](NOTICE) for the complete third-party attribution. The full legal
text of CC BY-SA 4.0 is available at
<https://creativecommons.org/licenses/by-sa/4.0/legalcode>.

> "SOC-CMM" is a trademark of Rob van Os. This project is **not affiliated
> with or endorsed by** Rob van Os or soc-cmm.com. The CC BY-SA 4.0 license
> does not grant trademark rights.

You remain responsible for ensuring compliance with your organisation's
security and data-handling policies when deploying this software.

## Version History

See [`CHANGELOG.md`](CHANGELOG.md).

