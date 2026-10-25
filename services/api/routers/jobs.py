from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..db import models, session
from ..schemas.job import JobCreate, JobResponse
from ..core.auth import get_current_user

router = APIRouter()

@router.post("/", response_model=JobResponse)
def create_job(job: JobCreate, db: Session = Depends(session.get_db), current_user: models.User = Depends(get_current_user)):
    db_job = models.Job(**job.dict(), owner_id=current_user.id)
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

@router.get("/{job_id}", response_model=JobResponse)
def read_job(job_id: int, db: Session = Depends(session.get_db), current_user: models.User = Depends(get_current_user)):
    db_job = db.query(models.Job).filter(models.Job.id == job_id, models.Job.owner_id == current_user.id).first()
    if db_job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return db_job

@router.get("/", response_model=list[JobResponse])
def read_jobs(skip: int = 0, limit: int = 10, db: Session = Depends(session.get_db), current_user: models.User = Depends(get_current_user)):
    jobs = db.query(models.Job).filter(models.Job.owner_id == current_user.id).offset(skip).limit(limit).all()
    return jobs

@router.delete("/{job_id}", response_model=JobResponse)
def delete_job(job_id: int, db: Session = Depends(session.get_db), current_user: models.User = Depends(get_current_user)):
    db_job = db.query(models.Job).filter(models.Job.id == job_id, models.Job.owner_id == current_user.id).first()
    if db_job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    db.delete(db_job)
    db.commit()
    return db_job