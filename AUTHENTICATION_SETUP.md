# SOC CMM Authentication System Setup

This document provides instructions for setting up and using the new authentication system in the SOC CMM Assessment System.

## Overview

The system now includes user authentication with the following features:
- User registration and login
- JWT token-based authentication
- User-specific customer and assessment management
- Secure password hashing
- Session management with cookies

## Prerequisites

1. Python 3.7+
2. All required dependencies (see requirements.txt)
3. Existing SOC CMM database

## Installation Steps

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure environment variables

Copy `.env.example` to `.env` and define **at minimum**:

```bash
cp .env.example .env
# then edit .env and set:
#   SECRET_KEY=...      (required for the app to start)
#   ADMIN_PASSWORD=...  (required for the initial admin user)
```

Generate a strong `SECRET_KEY` with:

```bash
python -c "import secrets; print(secrets.token_urlsafe(48))"
```

### 3. Run Database Migration

The migration script will:
- Add user authentication tables to your existing database
- Create a backup of your current database
- Create the initial admin user using the password from `$ADMIN_PASSWORD`
- Migrate existing customers to the admin user

```bash
python migrate_to_auth.py
```

### 4. Start the Application

```bash
python main.py
```

## Initial Credentials

After running the migration, log in with:

- **Username:** `admin`
- **Password:** the value you exported in `ADMIN_PASSWORD`

**Important:** Change the password immediately after the first login and
unset/remove `ADMIN_PASSWORD` from your environment.

## User Management

### Creating New Users

1. Navigate to `/register` in your browser
2. Fill out the registration form
3. Use the new credentials to log in

### User Permissions

- Each user can only see and manage their own customers
- Customers are automatically associated with the user who creates them
- Assessments are tied to customers and inherit user permissions

## Security Features

### Password Security
- Passwords are hashed using bcrypt
- Minimum password length: 8 characters
- Passwords are never stored in plain text

### Session Management
- JWT tokens with 30-minute expiration
- Secure HTTP-only cookies
- Automatic session cleanup

### Access Control
- All customer and assessment operations are user-scoped
- Users cannot access other users' data
- API endpoints require authentication

## API Authentication

For API access, include the JWT token in the Authorization header:

```
Authorization: Bearer <your-jwt-token>
```

## Database Schema Changes

### New Tables
- `users` - User accounts and authentication data
- Updated `customers` table with `user_id` foreign key

### Indexes
- `idx_users_username` - Fast username lookups
- `idx_users_email` - Fast email lookups  
- `idx_customers_user` - Fast user-customer queries

## Environment Variables

Set these environment variables for any deployment (the application will
**refuse to start** without `SECRET_KEY`):

```bash
export SECRET_KEY="$(python -c 'import secrets; print(secrets.token_urlsafe(48))')"
export ADMIN_PASSWORD="<strong password — only needed for the initial migration>"
export ALLOWED_ORIGINS="https://your-domain.example"  # comma-separated
```

## Troubleshooting

### Migration Issues

If the migration fails:

1. Check that your database file exists
2. Ensure you have write permissions
3. Verify the database is not locked by another process
4. Restore from the backup file if needed

### Authentication Issues

1. Clear browser cookies
2. Check that the SECRET_KEY is consistent
3. Verify the database contains the users table
4. Check server logs for JWT errors

### User Access Issues

1. Verify the user exists in the database
2. Check that customers are associated with the correct user_id
3. Ensure the user account is active

## Production Deployment

For production deployment:

1. Set a strong SECRET_KEY
2. Enable HTTPS and set secure cookies
3. Use a production database (PostgreSQL, MySQL)
4. Implement rate limiting
5. Set up proper logging
6. Configure backup strategies

## Backup and Recovery

The migration script creates a backup automatically. For manual backups:

```bash
cp soc_cmm_translated.db soc_cmm_translated.db.backup
```

To restore from backup:

```bash
cp soc_cmm_translated.db.backup soc_cmm_translated.db
```

## Support

If you encounter issues:

1. Check the application logs
2. Verify database integrity
3. Test with a fresh database
4. Review the authentication flow

## Migration Notes

- Existing customers will be assigned to the default admin user
- All existing data is preserved
- The migration is reversible using the backup file
- New users start with no customers and must create their own