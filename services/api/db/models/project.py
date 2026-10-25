from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship

from ..base import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    name = Column(String(200), index=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), index=True, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    user = relationship("User", back_populates="projects")
    media = relationship(
        "Media",
        back_populates="project",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    jobs = relationship(
        "Job",
        back_populates="project",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    clips = relationship(
        "Clip",
        back_populates="project",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )