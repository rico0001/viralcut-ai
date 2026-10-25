import os
from typing import Generator, Optional

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

from .base import Base

DATABASE_URL = os.getenv("DATABASE_URL")
engine: Optional[Engine] = None
SessionLocal: Optional[sessionmaker] = None


def create_database_engine(database_url: Optional[str] = None) -> Engine:
    url = database_url or os.getenv("DATABASE_URL")
    if not url:
        raise RuntimeError("DATABASE_URL must be configured before using the database")
    return create_engine(url, pool_pre_ping=True)


if DATABASE_URL:
    engine = create_database_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator[Session, None, None]:
    if SessionLocal is None:
        raise RuntimeError("DATABASE_URL must be configured before opening a database session")

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()