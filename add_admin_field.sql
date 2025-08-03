-- Add admin field to users table
ALTER TABLE users ADD COLUMN is_admin BOOLEAN DEFAULT FALSE;

-- Create a default admin user if none exists
INSERT OR IGNORE INTO users (username, email, hashed_password, full_name, is_active, is_admin, created_at, updated_at)
VALUES (
    'admin',
    'admin@soc-cmm.com',
    '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj/RK.sJwZ2y', -- password: admin123
    'System Administrator',
    TRUE,
    TRUE,
    CURRENT_TIMESTAMP,
    CURRENT_TIMESTAMP
);

-- Update existing admin user to have admin privileges (if exists)
UPDATE users SET is_admin = TRUE WHERE username = 'admin'; 