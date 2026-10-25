#!/bin/bash

# Start the application services

# Start PostgreSQL
docker-compose up -d postgres

# Start Redis
docker-compose up -d redis

# Start the API service
docker-compose up -d api

# Start the worker service
docker-compose up -d worker

# Start the web application
docker-compose up -d web

# Display the logs for all services
docker-compose logs -f