# SOC CMM Assessment System

A comprehensive Security Operations Center Capability Maturity Model assessment system built with FastAPI, SQLite, and modern web technologies.

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

1. Clone or download the system files
2. Install dependencies:
   ```bash
   pip install fastapi uvicorn jinja2 python-multipart aiofiles
   ```

3. Run the application:
   ```bash
   cd soc_cmm_system
   python main.py
   ```

4. Open your browser and navigate to `http://localhost:8000`

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

- Input validation and sanitization
- SQL injection prevention through parameterized queries
- CORS configuration for API access
- No authentication required (designed for internal/integrated use)

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

## License

This system is built for SOC maturity assessment purposes. Ensure compliance with your organization's security and data handling policies.

## Version History

- **v1.0.0** - Initial release with full SOC CMM assessment functionality

