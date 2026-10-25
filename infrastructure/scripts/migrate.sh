#!/bin/bash

# This script is used to run database migrations for the ViralCut AI application.

set -e

# Navigate to the API service directory
cd ../services/api

# Run the Alembic migrations
alembic upgrade head

echo "Database migrations completed successfully."