from fastapi import Depends
from sqlalchemy.orm import Session

from ..db.session import get_db
from ..core.auth import get_current_user
from ..schemas.auth import User

def get_db_session(db: Session = Depends(get_db)):
    return db

def get_current_active_user(current_user: User = Depends(get_current_user)):
    return current_user