from sqlalchemy import Column, Float, ForeignKey, Integer, String, Text, text
from sqlalchemy.orm import relationship

from ..base import Base

class Clip(Base):
    __tablename__ = "clips"

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("projects.id", ondelete="CASCADE"), index=True, nullable=False)
    title = Column(String(200), index=True, nullable=False)
    start_time = Column(Float, nullable=False)
    end_time = Column(Float, nullable=False)
    duration = Column(Float, nullable=False)
    highlight_score = Column(Float, default=0.0, server_default=text("0"), nullable=False)
    metadata_json = Column("metadata", Text, nullable=True)

    project = relationship("Project", back_populates="clips")

    def __repr__(self):
        return f"<Clip(id={self.id}, title={self.title}, start_time={self.start_time}, end_time={self.end_time})>"