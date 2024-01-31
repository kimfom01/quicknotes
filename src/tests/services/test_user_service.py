import pytest
from unittest import mock


from website.repositories.collection_repo import CollectionRepo
from website.services.user_service import UserService
from website.repositories.user_repo import UserRepo


@pytest.fixture
def user_repo():
    mock_user_repo = mock.create_autospec(UserRepo)

    yield mock_user_repo


@pytest.fixture
def collection_repo():
    mock_collection_repo = mock.create_autospec(CollectionRepo)

    yield mock_collection_repo


def test_get_by_email_valid(user_repo, collection_repo):
    user_service = UserService(user_repo, collection_repo)
    response = user_service.get_by_email(email="demo@mail.com")

    assert response.success == True
    assert response.message == "Success"


def test_get_by_email_email_invalid(user_repo, collection_repo):
    user_service = UserService(user_repo, collection_repo)
    response = user_service.get_by_email("janat16mail.com")

    assert response.success == False
    assert (
        response.message
        == "The email address is not valid. It must have exactly one @-sign."
    )


def test_create_user_valid(user_repo, collection_repo):
    user_service = UserService(user_repo, collection_repo)
    response = user_service.create_user(
        email="test@mail.com", first_name="Test", password="Pa$$w0rd"
    )

    assert response.success == True
    assert response.message == "Successfully registered"


def test_create_user_email_invalid(user_repo, collection_repo):
    user_service = UserService(user_repo, collection_repo)
    response = user_service.create_user(
        email="testmail.com", first_name="Test", password="Pa$$w0rd"
    )

    assert response.success == False
    assert (
        response.message
        == "The email address is not valid. It must have exactly one @-sign."
    )


def test_create_user_first_name_invalid(user_repo, collection_repo):
    user_service = UserService(user_repo, collection_repo)
    response = user_service.create_user(
        email="testmail.com", first_name="T", password="Pa$$w0rd"
    )

    assert response.success == False
    assert response.message == "First name must be greater than 1 character"


def test_create_user_password_invalid(user_repo, collection_repo):
    user_service = UserService(user_repo, collection_repo)
    response = user_service.create_user(
        email="testmail.com", first_name="Test", password="12345"
    )

    assert response.success == False
    assert response.message == "Password must be greater than 6 characters"
