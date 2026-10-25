from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from services.api.db.session import get_db
from services.api.schemas.clip import ClipCreate, ClipUpdate, Clip
from services.api.db.models.clip import Clip as ClipModel

router = APIRouter()

@router.post("/", response_model=Clip)
def create_clip(clip: ClipCreate, db: Session = Depends(get_db)):
    db_clip = ClipModel(**clip.dict())
    db.add(db_clip)
    db.commit()
    db.refresh(db_clip)
    return db_clip

@router.get("/{clip_id}", response_model=Clip)
def read_clip(clip_id: int, db: Session = Depends(get_db)):
    db_clip = db.query(ClipModel).filter(ClipModel.id == clip_id).first()
    if db_clip is None:
        raise HTTPException(status_code=404, detail="Clip not found")
    return db_clip

@router.patch("/{clip_id}", response_model=Clip)
def update_clip(clip_id: int, clip: ClipUpdate, db: Session = Depends(get_db)):
    db_clip = db.query(ClipModel).filter(ClipModel.id == clip_id).first()
    if db_clip is None:
        raise HTTPException(status_code=404, detail="Clip not found")
    for key, value in clip.dict(exclude_unset=True).items():
        setattr(db_clip, key, value)
    db.commit()
    db.refresh(db_clip)
    return db_clip

@router.delete("/{clip_id}", response_model=dict)
def delete_clip(clip_id: int, db: Session = Depends(get_db)):
    db_clip = db.query(ClipModel).filter(ClipModel.id == clip_id).first()
    if db_clip is None:
        raise HTTPException(status_code=404, detail="Clip not found")
    db.delete(db_clip)
    db.commit()
    return {"detail": "Clip deleted successfully"}