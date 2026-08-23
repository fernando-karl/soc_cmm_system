# Usage (web interface)

This page describes the typical day-to-day workflow, from first login to
viewing results.

## 1. Log in and register

After installing the application (see [`installation.md`](./installation.md))
and starting the server, browse to <http://localhost:8400>:

- **First-time access (administrator):** log in as `admin` with the
  password you defined in `ADMIN_PASSWORD`. Open your profile page and
  change the password right away.
- **Self-service registration:** users can register at `/register` to
  create their own account. Each user only sees their own customers and
  assessments.
- **Log out:** available from the top menu; clears the session cookie.

> JWT tokens expire after 30 minutes by default (configurable via
> `ACCESS_TOKEN_EXPIRE_MINUTES`). Sessions are also kept in an HTTP-only
> cookie.

## 2. Manage customers

1. Click **Customers** in the navigation bar.
2. Click **Add Customer** and provide a name plus an optional email and
   organisation.
3. Each customer is owned by the user that created them — other users
   cannot see them.
4. Use the search box to filter the customer list.

## 3. Create and complete an assessment

1. From the customer list, click **New Assessment**.
2. The system redirects to the questionnaire.
3. Questions are organised by the six SOC-CMM® domains:
   - **Business** (strategy, governance, costs, privacy)
   - **People** (hiring, training, performance)
   - **Process** (management, operations, reporting, use cases)
   - **Technology** (SIEM, detection, analytics)
   - **Services** (catalogue, threat hunting, vulnerabilities)
   - **Results** (overview, success factors, sharing)
4. Each domain contains **aspects** with their own questions. Pick an
   aspect to view its questions.
5. Supported question types:
   - Maturity scale aligned with SOC-CMM® (0 — Non-existent · 1 — Initial ·
     2 — Managed · 3 — Defined · 4 — Quantitatively Managed ·
     5 — Optimizing; some UI labels may use shorter names)
   - Multiple choice
   - Numeric
   - Free text
   - Checkbox
6. Answers autosave. The progress indicator shows how many questions are
   still pending.
7. When every aspect is complete, click **Complete Assessment**.

## 4. View results

The results page shows:

- A **radar chart** with maturity per domain.
- **Detailed scores** broken down by domain and aspect.
- **Comparison** with previous assessments of the same customer, when
  available.
- **Export** of the data for offline analysis.

## 5. Track progress over time

Run multiple assessments for the same customer. The progress page shows
trend charts per domain and aspect, letting you observe how the SOC matures
over months or quarters.

## 6. Switch language (EN/PT-BR)

- Click the 🇺🇸 / 🇧🇷 flags in the top bar.
- The choice is persisted in a `language` cookie (1 year).
- You can also switch via URL: `?lang=en` / `?lang=pt_br` or
  `/change-language/{language}`.

Details in [`languages.md`](./languages.md).

## 7. Admin features

Only users with `is_admin = TRUE` see the admin menus. See
[`administration.md`](./administration.md) for the dashboard, user
management and privileged operations.

## 8. API and MCP

- **REST API:** quick reference in [`api.md`](./api.md). Interactive docs at
  `/docs` (Swagger) and `/redoc`. Pass the JWT in the
  `Authorization: Bearer <token>` header.
- **MCP (Model Context Protocol):** AI-model integration — see
  [`mcp.md`](./mcp.md).

## Next steps

- [Installation](./installation.md)
- [Authentication](./authentication.md)
- [Troubleshooting](./troubleshooting.md)
