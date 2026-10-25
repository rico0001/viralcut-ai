from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from services.api.db.session import get_db
from services.api.db.models.user import User
from services.api.core.security import verify_password

def authorize_user(username: str, password: str, db: Session = Depends(get_db)) -> User:
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

def is_admin(user: User) -> bool:
    return user.is_admin

def require_admin(user: User):
    if not is_admin(user):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Operation not permitted",
        )