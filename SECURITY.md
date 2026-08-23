# Security Policy

## Supported versions

Security fixes are applied on the default branch (`main`) of this repository.

## Reporting a vulnerability

Please **do not** open a public GitHub issue for security vulnerabilities.

Report privately to the maintainer:

- **Email:** fernando.karl@gmail.com
- Or use [GitHub Security Advisories](https://github.com/fernando-karl/soc_cmm_system/security/advisories/new) if available

Include:

1. A short description of the issue
2. Steps to reproduce (without weaponized exploit payloads)
3. Affected version / commit if known
4. Your assessment of impact

You should receive an acknowledgement within a few days. We will coordinate a fix and a public disclosure timeline when appropriate.

## Deployment notes

- Never commit `.env` files or SQLite databases containing real user data
- Set a strong `SECRET_KEY` and rotate it periodically
- Change the bootstrap admin password and unset `ADMIN_PASSWORD` after first login
- Restrict `ALLOWED_ORIGINS` in production; terminate TLS at a reverse proxy
