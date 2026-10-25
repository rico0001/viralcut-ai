#!/bin/bash

# Backup the PostgreSQL database

# Set variables
DB_NAME="viralcut_ai"
DB_USER="your_db_user"
DB_PASSWORD="your_db_password"
BACKUP_DIR="./backups"
TIMESTAMP=$(date +"%Y%m%d%H%M%S")
BACKUP_FILE="$BACKUP_DIR/$DB_NAME-$TIMESTAMP.sql"

# Create backup directory if it doesn't exist
mkdir -p $BACKUP_DIR

# Export the database
PGPASSWORD=$DB_PASSWORD pg_dump -U $DB_USER $DB_NAME > $BACKUP_FILE

# Check if the backup was successful
if [ $? -eq 0 ]; then
  echo "Backup successful: $BACKUP_FILE"
else
  echo "Backup failed"
  exit 1
fi