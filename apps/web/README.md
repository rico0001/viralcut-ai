# README for the ViralCut AI Web Application

Welcome to the ViralCut AI web application! This application is designed to help users transform long-form videos into engaging short-form clips suitable for platforms like YouTube Shorts. Below is an overview of the project's structure and how to get started.

## Project Structure

The web application is organized into several key directories:

- **app/**: Contains the main application components.
  - **(auth)**: Authentication-related components for user login and registration.
  - **dashboard**: Components related to the user dashboard, displaying project statuses and highlights.
  - **projects**: Components for managing user projects, including creation and editing.
  - **settings**: Components for user settings and preferences.
  - **globals.css**: Global CSS styles for the application.

- **components/**: Contains reusable UI components used throughout the application.
  - **ui**: General UI components.
  - **dashboard**: Specific components for the dashboard view.
  - **projects**: Specific components for the projects view.
  - **video**: Components related to video playback and rendering.

- **lib/**: Contains utility functions and API calls.
  - **api.ts**: Functions for making API calls to the backend.
  - **utils.ts**: Utility functions used across the application.
  - **auth.ts**: Authentication-related utility functions.

- **public/**: Contains static assets such as images and icons.

## Getting Started

To get started with the ViralCut AI web application, follow these steps:

1. **Clone the Repository**: 
   ```
   git clone <repository-url>
   cd viralcut-ai/apps/web
   ```

2. **Install Dependencies**: 
   ```
   npm install
   ```

3. **Run the Development Server**: 
   ```
   npm run dev
   ```

4. **Access the Application**: Open your browser and navigate to `http://localhost:3000`.

## Features

- User authentication for secure access.
- Dashboard for monitoring project statuses and highlights.
- Project management capabilities including creation and editing.
- Video processing pipeline for generating short-form clips.
- Responsive design for optimal viewing on various devices.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

Thank you for using ViralCut AI! We hope you enjoy transforming your videos into engaging content.