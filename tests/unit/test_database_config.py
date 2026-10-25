import pytest
from sqlalchemy import Engine

from services.api.db.session import create_database_engine


def test_database_engine_uses_explicit_url_without_connecting():
    engine = create_database_engine("sqlite+pysqlite:///:memory:")
    try:
        assert isinstance(engine, Engine)
        assert engine.url.drivername == "sqlite"
    finally:
        engine.dispose()


def test_database_engine_reads_environment_url(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "sqlite+pysqlite:///:memory:")
    engine = create_database_engine()
    try:
        assert engine.url.drivername == "sqlite"
    finally:
        engine.dispose()


def test_database_engine_requires_configuration(monkeypatch):
    monkeypatch.delenv("DATABASE_URL", raising=False)
    with pytest.raises(RuntimeError, match="DATABASE_URL must be configured"):
        create_database_engine()