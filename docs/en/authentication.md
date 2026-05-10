# Authentication

The system uses JWT-based user authentication with HTTP-only cookies.

## Features
- User registration and login
- JWT tokens (default expiration: 30 minutes)
- Bcrypt password hashing
- Per-user scoping: users only see their own customers/assessments

## Installation and migration
1. Install dependencies: `pip install -r requirements.txt`
2. Configure the environment: `cp .env.example .env` and set both
   **`SECRET_KEY`** and **`ADMIN_PASSWORD`** (the application refuses to
   start without `SECRET_KEY` and the migration aborts without
   `ADMIN_PASSWORD`).
3. Run the migration: `python migrate_to_auth.py`
   - Creates the `users` tables and indexes
   - Backs up any existing database
   - Creates the `admin` user using the password from `$ADMIN_PASSWORD`
4. Start the application: `python main.py`

Change the admin password after the first login and unset
`ADMIN_PASSWORD` from the environment.

## API

Pass the JWT in the `Authorization` header:

```
Authorization: Bearer <your-token>
```

Useful endpoints (see also [`api.md`](./api.md)):
- `POST /api/auth/register` — register a new user
- `POST /api/auth/login` — log in and obtain a JWT
- `POST /api/auth/logout` — log out (clears cookie)
- `GET  /api/auth/me` — return the current user's profile

## Security defaults

- Passwords stored as bcrypt hashes; never logged or returned by the API.
- Tokens signed with HS256 using `SECRET_KEY`.
- HTTP-only cookies prevent XSS-driven token theft.
- All customer/assessment endpoints check ownership server-side.
