import sys
import os

# Fix the database path in database.py
database_py_path = '/home/ubuntu/soc_cmm_system/database.py'

with open(database_py_path, 'r') as f:
    content = f.read()

# Replace the hardcoded paths with relative paths
content = content.replace(
    "with open('/home/ubuntu/database_schema.sql', 'r') as f:",
    "with open('database_schema.sql', 'r') as f:"
)

content = content.replace(
    "with open('/home/ubuntu/soc_cmm_complete_data.json', 'r') as f:",
    "with open('soc_cmm_complete_data.json', 'r') as f:"
)

with open(database_py_path, 'w') as f:
    f.write(content)

print("Database paths fixed!")

