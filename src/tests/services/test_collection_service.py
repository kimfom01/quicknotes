import pytest
from unittest import mock


from website.services.collection_service import CollectionService
from website.repositories.collection_repo import CollectionRepo


@pytest.fixture
def collection_repo():
    mock_collection_repo = mock.create_autospec(CollectionRepo)

    yield mock_collection_repo


def test_get_collections_valid(collection_repo):
    collection_service = CollectionService(collection_repo)

    response = collection_service.get_collections(user_id=1)

    assert response.success == True
    assert response.message == "Success"


def test_get_collections_user_id_invalid(collection_repo):
    collection_service = CollectionService(collection_repo)

    response = collection_service.get_collections(user_id=0)

    assert response.success == False
    assert response.message == "User id cannot be less than or equal to 0"


def test_get_default_collection_valid(collection_repo):
    collection_service = CollectionService(collection_repo)

    response = collection_service.get_default_collection(user_id=1)

    assert response.success == True
    assert response.message == "Success"


def test_get_default_collection_user_id_invalid(collection_repo):
    collection_service = CollectionService(collection_repo)

    response = collection_service.get_collections(user_id=0)

    assert response.success == False
    assert response.message == "User id cannot be less than or equal to 0"


def test_create_collection_valid(collection_repo):
    collection_service = CollectionService(collection_repo)

    response = collection_service.create_collection(title="test collection", user_id=1)

    assert response.success == True
    assert response.message == "Successfully created"


def test_create_collection_title_invalid(collection_repo):
    collection_service = CollectionService(collection_repo)

    response = collection_service.create_collection(title="", user_id=1)

    assert response.success == False
    assert response.message == "Collection title cannot be empty"


def test_create_collection_user_id_invalid(collection_repo):
    collection_service = CollectionService(collection_repo)

    response = collection_service.create_collection(title="test collection", user_id=0)

    assert response.success == False
    assert response.message == "User id cannot be less than or equal to 0"
