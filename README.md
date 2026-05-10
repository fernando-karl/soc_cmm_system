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
- **Maturity Evaluation**: 5-level maturity scale (Initial, Developing, Defined, Managed, Optimized)
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

- **Backend**: FastAPI (Python 3.11)
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3, JavaScript with Jinja2 templates
- **Visualization**: Chart.js for radar charts and progress tracking
- **Styling**: Modern CSS with responsive design
- **Icons**: Font Awesome

## Installation

### Prerequisites

- Python 3.11 or higher
- pip package manager

### Setup

1. Clone or download the system files.

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the required environment variables.** Copy
   `.env.example` to `.env` and fill in real values:
   ```bash
   cp .env.example .env
   ```

   The application will refuse to start if `SECRET_KEY` is not set.

4. Run the application:
   ```bash
   cd soc_cmm_system
   python main.py
   ```

5. Open your browser and navigate to `http://localhost:8000`.

### Required environment variables

| Variable           | Required | Description                                                                                                  |
| ------------------ | -------- | ------------------------------------------------------------------------------------------------------------ |
| `SECRET_KEY`       | **Yes**  | Secret used to sign JWT tokens. Generate with `python -c "import secrets; print(secrets.token_urlsafe(48))"`. |
| `ADMIN_PASSWORD`   | **Yes**¹ | Initial password for the bootstrap admin account created by `migrate_to_auth.py`.                             |
| `ALLOWED_ORIGINS`  | No       | Comma-separated list of CORS origins. Defaults to `http://localhost:8000`. Use `*` only in trusted networks. |

¹ Required only when running the initial migration / bootstrap.

## Usage

### 1. Customer Management

- Navigate to the Customers page
- Click "Add Customer" to create a new customer
- Fill in customer details (name, email, organization)

### 2. Starting an Assessment

- From the customer list, click "New Assessment"
- The system will create a new assessment and redirect to the questionnaire

### 3. Completing the Assessment

- The assessment is organized by domains (Business, People, Process, Technology, Services, Results)
- Each domain contains multiple aspects with specific questions
- Select an aspect to view its questions
- Answer all questions using the 5-level maturity scale
- Complete all aspects in a domain before moving to the next
- Use the progress indicator to track completion

### 4. Viewing Results

- After completing all domains, click "Complete Assessment"
- View the radar chart showing maturity levels across all domains
- Review detailed scores by domain and aspect
- Export results if needed

### 5. Progress Tracking

- Complete multiple assessments for the same customer
- View progress over time with trend charts
- Compare current and previous assessments

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

### Adding Questions

1. Edit `soc_cmm_complete_data.json` to add new questions
2. Restart the application to reload the database

### Styling

- Modify `static/css/style.css` for visual customization
- Update CSS variables in `:root` for color scheme changes

### Functionality

- Extend `static/js/main.js` for additional JavaScript functionality
- Modify templates in `templates/` for layout changes

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
  environment variable (default: `http://localhost:8000`).
- All database queries use parameterized statements to prevent SQL
  injection.
- **Never commit `.env` files or `*.db` files** — both are excluded by
  `.gitignore`.
- For production: run behind a reverse proxy (nginx/Caddy) with TLS, set
  short `ACCESS_TOKEN_EXPIRE_MINUTES`, and rotate `SECRET_KEY` periodically.

## Deployment

### Local Development
```bash
python main.py
```

### Production Deployment
For production deployment, consider:

1. Using a production WSGI server (e.g., Gunicorn)
2. Setting up a reverse proxy (e.g., Nginx)
3. Using environment variables for configuration
4. Implementing proper logging
5. Setting up database backups

### Docker Deployment
Create a Dockerfile for containerized deployment:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "main.py"]
```

## Troubleshooting

### Common Issues

1. **Database errors**: Delete `soc_cmm.db` and restart the application
2. **Port conflicts**: Change the port in `main.py` (default: 8000)
3. **Missing dependencies**: Run `pip install -r requirements.txt`

### Logs

Check the console output for detailed error messages and API request logs.

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review the API documentation
3. Examine browser console for JavaScript errors
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

- **v1.0.0** - Initial release with full SOC CMM assessment functionality

