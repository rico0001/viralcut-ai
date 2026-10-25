from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func, text
from sqlalchemy.orm import relationship

from ..base import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("projects.id", ondelete="CASCADE"), index=True, nullable=False)
    status = Column(String(32), default="pending", server_default=text("'pending'"), index=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    project = relationship("Project", back_populates="jobs")