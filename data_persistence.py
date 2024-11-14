# data_persistence.py

import shutil
import os

# Define the path to the database file
DATABASE_FILE = "database\\finance_manager.db"
BACKUP_FILE = 'database\\finance_manager_backup.db'

# Function to back up the database
def backup_data():
    if os.path.exists(DATABASE_FILE):
        shutil.copy2(DATABASE_FILE, BACKUP_FILE)
        print("Backup created successfully!")
    else:
        print("No database found to back up.")

# Function to restore the database from backup
def restore_data():
    if os.path.exists(BACKUP_FILE):
        shutil.copy2(BACKUP_FILE, DATABASE_FILE)
        print("Data restored successfully!")
    else:
        print("No backup found to restore.")
