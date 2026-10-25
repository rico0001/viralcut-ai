from sqlalchemy import inspect
from sqlalchemy.orm import configure_mappers

from services.api.db.base import Base
from services.api.db.models import Clip, Job, Media, Project, User


def test_all_models_share_base_metadata():
    assert {"users", "projects", "media", "jobs", "clips"}.issubset(Base.metadata.tables)
    assert all(model.metadata is Base.metadata for model in (User, Project, Media, Job, Clip))


def test_model_relationships_configure_and_point_both_directions():
    configure_mappers()

    assert inspect(User).relationships.projects.back_populates == "user"
    assert inspect(Project).relationships.user.back_populates == "projects"
    assert inspect(Project).relationships.media.back_populates == "project"
    assert inspect(Media).relationships.project.back_populates == "media"
    assert inspect(Project).relationships.jobs.back_populates == "project"
    assert inspect(Job).relationships.project.back_populates == "jobs"
    assert inspect(Project).relationships.clips.back_populates == "project"
    assert inspect(Clip).relationships.project.back_populates == "clips"


def test_clip_metadata_maps_to_metadata_column():
    assert Clip.__table__.c.metadata.name == "metadata"
    assert Clip.metadata_json.property.columns[0].name == "metadata"