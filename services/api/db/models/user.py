from sqlalchemy import Boolean, Column, Integer, String, false, true
from sqlalchemy.orm import relationship

from ..base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, index=True, nullable=False)
    email = Column(String(320), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True, server_default=true(), nullable=False)
    is_superuser = Column(Boolean, default=False, server_default=false(), nullable=False)

    projects = relationship(
        "Project",
        back_populates="user",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )