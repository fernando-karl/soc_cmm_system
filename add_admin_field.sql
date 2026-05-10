-- Add admin field to the users table.
-- This script intentionally does NOT insert a default admin user — use
-- `python migrate_to_auth.py` (or `python run_admin_migration.py`) with the
-- ADMIN_PASSWORD environment variable set so that the bcrypt hash is
-- generated from a strong, deployer-supplied secret instead of being
-- hard-coded in version control.

ALTER TABLE users ADD COLUMN is_admin BOOLEAN DEFAULT FALSE;

-- Promote any pre-existing user named "admin" to administrator.
UPDATE users SET is_admin = TRUE WHERE username = 'admin';
