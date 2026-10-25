# API Service Documentation

This directory contains the implementation of the API service for the ViralCut AI application. The API is built using FastAPI and provides endpoints for managing projects, jobs, clips, and user authentication.

## Structure

- **app/**: Contains the main application code, including the entry point, configuration, and dependency management.
- **core/**: Contains core functionalities such as authentication, security, error handling, and logging.
- **db/**: Contains database models, session management, and migration scripts.
- **schemas/**: Contains Pydantic models for request and response validation.
- **routers/**: Contains route definitions for different resources such as projects, jobs, and clips.
- **services/**: Contains utility functions for storage, file uploads, and media probing.
- **requirements.txt**: Lists the Python dependencies required for the API service.
- **Dockerfile**: Contains instructions for building the Docker image for the API service.

## Getting Started

1. **Install Dependencies**: Use the `requirements.txt` file to install the necessary Python packages.
2. **Run the Application**: Use the command `uvicorn app.main:app --reload` to start the FastAPI application in development mode.
3. **Access the API**: The API will be available at `http://localhost:8000`. You can access the interactive API documentation at `http://localhost:8000/docs`.

## API Endpoints

The API provides various endpoints for managing projects, jobs, and clips. Refer to the individual router files for detailed endpoint specifications.

## Contributing

Contributions to the API service are welcome. Please follow the project's coding standards and ensure that all new features are accompanied by tests.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.