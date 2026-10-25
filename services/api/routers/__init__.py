from fastapi import APIRouter

router = APIRouter()

from . import auth, projects, jobs, clips, health

router.include_router(auth.router, prefix="/auth", tags=["auth"])
router.include_router(projects.router, prefix="/projects", tags=["projects"])
router.include_router(jobs.router, prefix="/jobs", tags=["jobs"])
router.include_router(clips.router, prefix="/clips", tags=["clips"])
router.include_router(health.router, prefix="/health", tags=["health"])