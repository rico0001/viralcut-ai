from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.api.db.session import get_db
from services.api.schemas.auth import UserCreate, UserOut
from services.api.core.auth import create_user, get_user_by_email

router = APIRouter()

@router.post("/register", response_model=UserOut)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db, email=user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)

@router.post("/login")
def login_user(user: UserCreate, db: Session = Depends(get_db)):
    # Implement login logic here
    pass

@router.get("/me", response_model=UserOut)
def read_users_me(db: Session = Depends(get_db)):
    # Implement logic to return the current user
    pass