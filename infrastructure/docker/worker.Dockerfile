FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY ./services/worker/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the worker application code
COPY ./services/worker/app /app

# Set the environment variable for the Celery broker URL
ENV CELERY_BROKER_URL=redis://redis:6379/0

# Command to run the Celery worker
CMD ["celery", "-A", "app.celery_app", "worker", "--loglevel=info"]