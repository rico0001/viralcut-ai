from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from services.api.db import models, session
from services.api.schemas import project as project_schemas
from services.api.core.auth import get_current_user

router = APIRouter()

@router.post("/", response_model=project_schemas.Project)
def create_project(project: project_schemas.ProjectCreate, db: Session = Depends(session.get_db), current_user: models.User = Depends(get_current_user)):
    db_project = models.Project(**project.dict(), owner_id=current_user.id)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

@router.get("/", response_model=list[project_schemas.Project])
def read_projects(skip: int = 0, limit: int = 10, db: Session = Depends(session.get_db), current_user: models.User = Depends(get_current_user)):
    projects = db.query(models.Project).filter(models.Project.owner_id == current_user.id).offset(skip).limit(limit).all()
    return projects

@router.get("/{project_id}", response_model=project_schemas.Project)
def read_project(project_id: int, db: Session = Depends(session.get_db), current_user: models.User = Depends(get_current_user)):
    project = db.query(models.Project).filter(models.Project.id == project_id, models.Project.owner_id == current_user.id).first()
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.patch("/{project_id}", response_model=project_schemas.Project)
def update_project(project_id: int, project: project_schemas.ProjectUpdate, db: Session = Depends(session.get_db), current_user: models.User = Depends(get_current_user)):
    db_project = db.query(models.Project).filter(models.Project.id == project_id, models.Project.owner_id == current_user.id).first()
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    for key, value in project.dict(exclude_unset=True).items():
        setattr(db_project, key, value)
    db.commit()
    db.refresh(db_project)
    return db_project

@router.delete("/{project_id}", response_model=dict)
def delete_project(project_id: int, db: Session = Depends(session.get_db), current_user: models.User = Depends(get_current_user)):
    db_project = db.query(models.Project).filter(models.Project.id == project_id, models.Project.owner_id == current_user.id).first()
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    db.delete(db_project)
    db.commit()
    return {"detail": "Project deleted successfully"}