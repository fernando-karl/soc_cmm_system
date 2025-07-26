#!/usr/bin/env python3
"""
Migration script to add user authentication to existing SOC CMM database
"""

import sqlite3
import os
from datetime import datetime

def migrate_database(db_path="soc_cmm_translated.db"):
    """Migrate existing database to include user authentication"""
    
    if not os.path.exists(db_path):
        print(f"Database {db_path} not found!")
        return False
    
    # Create backup
    backup_path = f"{db_path}.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    print(f"Creating backup: {backup_path}")
    
    try:
        # Copy database file
        with open(db_path, 'rb') as src, open(backup_path, 'wb') as dst:
            dst.write(src.read())
    except Exception as e:
        print(f"Failed to create backup: {e}")
        return False
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # Check if users table already exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
        if cursor.fetchone():
            print("Users table already exists. Skipping migration.")
            return True
        
        print("Starting database migration...")
        
        # Create users table
        print("Creating users table...")
        cursor.execute("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username VARCHAR(50) UNIQUE NOT NULL,
                email VARCHAR(255) UNIQUE NOT NULL,
                hashed_password VARCHAR(255) NOT NULL,
                full_name VARCHAR(255),
                is_active BOOLEAN DEFAULT TRUE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Create indexes for users table
        cursor.execute("CREATE INDEX idx_users_username ON users(username)")
        cursor.execute("CREATE INDEX idx_users_email ON users(email)")
        
        # Check if customers table exists and has user_id column
        cursor.execute("PRAGMA table_info(customers)")
        columns = [column[1] for column in cursor.fetchall()]
        
        if 'user_id' not in columns:
            print("Adding user_id column to customers table...")
            cursor.execute("ALTER TABLE customers ADD COLUMN user_id INTEGER")
            cursor.execute("CREATE INDEX idx_customers_user ON customers(user_id)")
        
        # Create a default admin user
        print("Creating default admin user...")
        from auth import auth_manager
        
        try:
            admin_user_id = auth_manager.create_user(
                username="admin",
                email="admin@soc-cmm.com",
                password="(use-ADMIN_PASSWORD)",
                full_name="System Administrator"
            )
            print(f"Created admin user with ID: {admin_user_id}")
            
            # Update existing customers to belong to admin user
            cursor.execute("UPDATE customers SET user_id = ? WHERE user_id IS NULL", (admin_user_id,))
            updated_count = cursor.rowcount
            print(f"Updated {updated_count} existing customers to belong to admin user")
            
        except Exception as e:
            print(f"Warning: Could not create admin user: {e}")
            print("You will need to create a user manually after migration")
        
        conn.commit()
        print("Migration completed successfully!")
        return True
        
    except Exception as e:
        print(f"Migration failed: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def create_default_user(db_path="soc_cmm_translated.db"):
    """Create a default user if none exists"""
    from auth import auth_manager
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # Check if any users exist
        cursor.execute("SELECT COUNT(*) FROM users")
        user_count = cursor.fetchone()[0]
        
        if user_count == 0:
            print("No users found. Creating default admin user...")
            admin_user_id = auth_manager.create_user(
                username="admin",
                email="admin@soc-cmm.com",
                password="(use-ADMIN_PASSWORD)",
                full_name="System Administrator"
            )
            print(f"Created admin user with ID: {admin_user_id}")
            print("Default credentials: admin / (use-ADMIN_PASSWORD)")
            print("Please change these credentials after first login!")
        else:
            print(f"Found {user_count} existing user(s)")
            
    except Exception as e:
        print(f"Error creating default user: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    print("SOC CMM Database Migration Tool")
    print("=" * 40)
    
    # Check for database file
    db_files = [
        "soc_cmm_translated.db",
        "soc_cmm.db",
        "soc_cmm_portuguese.db"
    ]
    
    db_path = None
    for file in db_files:
        if os.path.exists(file):
            db_path = file
            break
    
    if not db_path:
        print("No database file found!")
        print("Available files:", db_files)
        exit(1)
    
    print(f"Using database: {db_path}")
    
    # Run migration
    if migrate_database(db_path):
        create_default_user(db_path)
        print("\nMigration completed successfully!")
        print("You can now start the application with authentication enabled.")
    else:
        print("\nMigration failed!")
        exit(1)