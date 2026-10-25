# Architectural Overview of ViralCut AI

## 1. Introduction
ViralCut AI is an AI-powered platform designed to transform long-form videos into engaging short-form clips suitable for platforms like YouTube Shorts. The architecture is modular, allowing for scalability, maintainability, and ease of integration with various services.

## 2. High-Level Architecture
The architecture consists of several key components:

### 2.1 Frontend
- **Framework**: Next.js with TypeScript and React.
- **Styling**: Tailwind CSS for responsive design.
- **Components**: A consistent UI component system for a polished user experience.
- **Routing**: App Router for managing navigation and state.

### 2.2 Backend API
- **Framework**: FastAPI for building RESTful APIs.
- **Database**: PostgreSQL for persistent storage of user data, projects, and processing jobs.
- **ORM**: SQLAlchemy for database interactions and Alembic for migrations.
- **Authentication**: Secure user authentication and authorization mechanisms.

### 2.3 Background Processing
- **Task Queue**: Celery with Redis as the broker for managing background tasks.
- **Workers**: Dedicated workers for processing video tasks asynchronously, ensuring that the API remains responsive.

### 2.4 AI and Video Processing
- **AI Agents**: Modular agents for tasks such as transcription, highlight detection, and content understanding.
- **Video Processing**: FFmpeg for rendering videos, including cropping, captioning, and format conversion.
- **Transcription**: Integration with speech-to-text services for generating accurate transcripts with timestamps.

## 3. Component Responsibilities
### 3.1 Frontend
- User interface for project management, video uploads, and clip editing.
- Displays processing status and results.

### 3.2 Backend API
- Handles requests for project creation, video uploads, and clip generation.
- Manages user authentication and authorization.

### 3.3 Background Workers
- Executes long-running tasks such as video processing and AI analysis.
- Provides real-time updates on task progress.

### 3.4 AI Agents
- **Source Inspector**: Validates video sources and extracts metadata.
- **Transcription Service**: Converts audio to text with timestamps.
- **Highlight Detection**: Identifies engaging moments in videos.
- **Clip Ranking**: Scores and ranks candidate clips based on engagement potential.

## 4. Data Flow
1. **User Interaction**: Users upload videos and configure project settings through the frontend.
2. **API Requests**: The frontend communicates with the backend API to initiate processing.
3. **Background Processing**: The API enqueues tasks in Redis, which are picked up by Celery workers.
4. **AI Analysis**: Workers execute AI tasks, generating transcripts and identifying highlights.
5. **Video Rendering**: FFmpeg processes the selected highlights into short clips.
6. **Results Delivery**: Processed clips and metadata are stored in PostgreSQL and made available for user download.

## 5. Security Considerations
- Implement strict authentication and authorization checks.
- Validate all user inputs to prevent injection attacks.
- Use secure storage for sensitive data and API keys.

## 6. Conclusion
The architecture of ViralCut AI is designed to be robust, scalable, and user-friendly, ensuring a seamless experience for users looking to create engaging video content. The modular design allows for easy updates and integration of new features as the platform evolves.