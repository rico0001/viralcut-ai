from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..db import session as db_session
from ..schemas.auth import UserCreate, UserOut
from ..db.models.user import User
from ..core.security import hash_password, verify_password

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create_user(user: UserCreate, db: Session = Depends(db_session.get_db)):
    db_user = get_user(db, user.id)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
    hashed_password = hash_password(user.password)
    new_user = User(email=user.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def authenticate_user(email: str, password: str, db: Session = Depends(db_session.get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.hashed_password):
        return False
    return user