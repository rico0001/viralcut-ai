import pytest
from services.api.services.authz import authorize_user, check_permissions
from services.api.db.models.user import User
from services.api.db.models.project import Project

@pytest.fixture
def user():
    return User(id=1, username='testuser', role='admin')

@pytest.fixture
def project():
    return Project(id=1, owner_id=1)

def test_authorize_user_success(user):
    assert authorize_user(user) is True

def test_authorize_user_failure():
    assert authorize_user(None) is False

def test_check_permissions_success(user, project):
    assert check_permissions(user, project) is True

def test_check_permissions_failure(user, project):
    project.owner_id = 2  # Change owner to simulate permission failure
    assert check_permissions(user, project) is False