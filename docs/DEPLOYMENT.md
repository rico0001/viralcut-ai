# DEPLOYMENT INSTRUCTIONS

## Prerequisites

Before deploying the ViralCut AI application, ensure you have the following installed:

- Docker
- Docker Compose
- PostgreSQL
- Redis

## Environment Configuration

1. Create a `.env` file in the root directory of the project based on the provided `.env.example` file. Update the necessary environment variables, including database connection strings, API keys, and other configurations.

## Building the Application

1. Navigate to the root directory of the project.
2. Run the following command to build the Docker images:

   ```
   docker-compose build
   ```

## Starting the Application

1. Start the application using Docker Compose:

   ```
   docker-compose up
   ```

2. This command will start all services defined in the `docker-compose.yml` file, including the API, worker, and web applications.

## Database Migration

1. After starting the application, run the database migrations to set up the initial schema:

   ```
   docker-compose exec api alembic upgrade head
   ```

## Accessing the Application

- The web application will be accessible at `http://localhost:3000`.
- The API will be accessible at `http://localhost:8000`.

## Stopping the Application

To stop the application, use the following command:

```
docker-compose down
```

This command will stop and remove all containers defined in the `docker-compose.yml` file.

## Backup and Restore

### Backup Database

To back up the PostgreSQL database, run the following command:

```
docker-compose exec api ./scripts/backup_db.sh
```

### Restore Database

To restore the database from a backup, ensure you have a backup file and run:

```
docker-compose exec api psql -U <username> -d <database> -f /path/to/backup/file.sql
```

## Additional Notes

- Ensure that all services are running correctly by checking the logs. You can view logs using:

  ```
  docker-compose logs
  ```

- For production deployments, consider using a reverse proxy like Nginx for better performance and security.

- Monitor resource usage and adjust Docker configurations as necessary to optimize performance.

By following these instructions, you should be able to successfully deploy the ViralCut AI application.