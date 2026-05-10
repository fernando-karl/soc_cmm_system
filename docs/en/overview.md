# Overview

The **SOC CMM Assessment System** is a web application for running SOC
(Security Operations Center) maturity assessments using the **SOC-CMM®**
framework published by **Rob van Os** (<https://www.soc-cmm.com>).

## Capabilities

- Customer (organisation) registry and management.
- Per-customer assessments with incremental autosave.
- Guided questionnaire across the six SOC-CMM® domains (Business, People,
  Process, Technology, Services, Results) and their aspects.
- Automatic scoring on a 1–5 maturity scale (Initial → Optimised).
- **Radar-chart** visualisation with historical comparison between past
  assessments of the same customer.
- Per-user authentication (JWT + HTTP-only cookie) with full data isolation.
- Admin features: dashboard, user management, deletion, admin promotion.
- Bilingual UI (**EN / PT-BR**) with live switching.
- **MCP (Model Context Protocol)** integration so AI models can drive the
  workflow.
- REST API documented at `/docs` (Swagger) and `/redoc`.

## Stack

- **Backend:** FastAPI (Python 3.11+), SQLite, Jinja2.
- **Auth:** JWT (`python-jose`), bcrypt (`passlib`).
- **Frontend:** HTML/CSS/JS, Chart.js, Font Awesome.
- **Containers:** Docker + Docker Compose.

## Default port

`8400`. Override with the `PORT` environment variable. Browse
<http://localhost:8400>.

## License & attribution

This project is a derivative of the SOC-CMM® framework (CC BY-SA 4.0) and
is therefore distributed under the same license: **Creative Commons
Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)**. See `LICENSE`
and `NOTICE` at the repository root.

## Next steps

- [Installation](./installation.md)
- [Usage](./usage.md)
- [Authentication](./authentication.md)
- [API](./api.md)
- [Docker](./docker.md)
- [Troubleshooting](./troubleshooting.md)
