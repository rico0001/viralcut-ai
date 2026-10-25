# ViralCut AI

ViralCut AI is an early-stage video repurposing application for turning videos users own or are authorized to process into reviewable vertical clips. It does not download YouTube videos. Viral potential is never guaranteed.

## Current milestone

The foundation includes a minimal FastAPI health service, a Next.js landing page, and resource-limited PostgreSQL/Redis services. Uploads, transcription, highlight analysis, clip editing, and rendering are not implemented yet. See [docs/IMPLEMENTATION_STATUS.md](docs/IMPLEMENTATION_STATUS.md) for scope and verification status.

## Stack

- Next.js 15, React, TypeScript, and Tailwind CSS
- FastAPI on Python
- PostgreSQL and Redis through Docker Compose
- Celery and FFmpeg are planned for asynchronous processing and rendering
- Hosted AI providers will be optional and configured only through server-side environment variables

## Windows setup

Prerequisites: Windows 10, Docker Desktop with the Linux container engine running, Node.js 22 LTS (npm included), and at least 2 GB of available memory for data containers. The API can run in Docker; a local Python installation is not required for that route.

From PowerShell at the repository root:

```powershell
Copy-Item .env.example .env
notepad .env
```

Set a local-only `POSTGRES_PASSWORD` in `.env`, then start only the database and queue:

```powershell
docker compose up -d db redis
docker compose ps
```

Start the API in another PowerShell window. Compose starts PostgreSQL and Redis as API dependencies:

```powershell
docker compose --profile api up --build api
```

Check the API at `http://localhost:8000/health` or `http://localhost:8000/docs`.

Start the frontend in a third PowerShell window:

```powershell
Set-Location apps/web
npm install
npm run dev
```

Open `http://localhost:3000`. Keep the frontend and API as the only application services during development; do not start the worker until its pipeline phase is implemented. Stop containers with `docker compose down`; PostgreSQL data remains in the `postgres_data` volume. `docker compose down -v` deletes that volume and should only be used when you intentionally want to erase local database data.

## Lightweight frontend checks

```powershell
Set-Location apps/web
npm run typecheck
npm run build
```

Python tests require Python 3.11+ and dependencies from `services/api/requirements.txt`. No AI models are downloaded as part of setup.

## Development principles

- Upload authorized media only; URLs are not treated as permission to download or republish.
- Keep provider keys in backend environment variables, never in `NEXT_PUBLIC_*` variables.
- Run long media jobs in workers, not in HTTP requests.
- Prefer deterministic validation and reviewable AI outputs; users approve clips before publishing.