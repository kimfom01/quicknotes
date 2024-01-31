import pytest
from unittest import mock


from website.schema.Response import Response
from website.services.note_service import NoteService
from website.repositories.notes_repo import NotesRepo


@pytest.fixture
def note_repo():
    mock_note_repo = mock.create_autospec(NotesRepo)

    yield mock_note_repo


def test_get_by_id_valid(note_repo):
    note_service = NoteService(note_repo)

    response = note_service.get_by_id(id=1, collection_id=1, user_id=1)

    assert response.success == True
    assert response.message == "Success"


def test_get_by_id_collection_id_invalid(note_repo):
    note_repo.get_by_id.return_value = Response(
        success=False,
        message="Id, user id or Collection id cannot be less than or equal to 0",
        body=None,
    )
    note_service = NoteService(note_repo)

    response = note_service.get_by_id(id=1, collection_id=0, user_id=1)

    assert response.success == False
    assert (
        response.message
        == "Id, user id or Collection id cannot be less than or equal to 0"
    )


def test_get_by_id_user_id_invalid(note_repo):
    note_repo.get_by_id.return_value = Response(
        success=False,
        message="Id, user id or Collection id cannot be less than or equal to 0",
        body=None,
    )
    note_service = NoteService(note_repo)

    response = note_service.get_by_id(id=1, collection_id=1, user_id=0)

    assert response.success == False
    assert (
        response.message
        == "Id, user id or Collection id cannot be less than or equal to 0"
    )


def test_get_by_id_note_id_invalid(note_repo):
    note_repo.get_by_id.return_value = Response(
        success=False,
        message="Id, user id or Collection id cannot be less than or equal to 0",
        body=None,
    )
    note_service = NoteService(note_repo)

    response = note_service.get_by_id(id=0, collection_id=1, user_id=1)

    assert response.success == False
    assert (
        response.message
        == "Id, user id or Collection id cannot be less than or equal to 0"
    )


def test_get_all_valid(note_repo):
    note_service = NoteService(note_repo)

    response = note_service.get_all(collection_id=1, user_id=1)

    assert response.success == True
    assert response.message == "Success"


def test_get_all_collection_id_invalid(note_repo):
    note_repo.get_all.return_value = Response(
        success=False,
        message="User id or collection id cannot be less than or equal to 0",
        body=None,
    )
    note_service = NoteService(note_repo)

    response = note_service.get_all(collection_id=0, user_id=1)

    assert response.success == False
    assert (
        response.message == "User id or collection id cannot be less than or equal to 0"
    )


def test_get_all_user_id_invalid(note_repo):
    note_repo.get_all.return_value = Response(
        success=False,
        message="User id or collection id cannot be less than or equal to 0",
        body=None,
    )
    note_service = NoteService(note_repo)

    response = note_service.get_all(collection_id=1, user_id=0)

    assert response.success == False
    assert (
        response.message == "User id or collection id cannot be less than or equal to 0"
    )


def test_create_note_valid(note_repo):
    note_service = NoteService(note_repo)

    response = note_service.create_note(data="test data", user_id=1, collection_id=1)

    assert response.success == True
    assert response.message == "Successfully created"


def test_create_note_data_invalid(note_repo):
    note_repo.create_note.return_value = Response(
        success=False, message="Note text cannot be empty", body=None
    )
    note_service = NoteService(note_repo)

    response = note_service.create_note(data="", user_id=1, collection_id=1)

    assert response.success == False
    assert response.message == "Note text cannot be empty"


def test_create_note_collection_id_invalid(note_repo):
    note_repo.create_note.return_value = Response(
        success=False,
        message="User id or collection id cannot be less than or equal to 0",
        body=None,
    )

    note_service = NoteService(note_repo)

    response = note_service.create_note(data="test data", user_id=1, collection_id=0)

    assert response.success == False
    assert (
        response.message
        == "User id or collection id cannot be less than or equal to 0"
    )


def test_create_note_user_id_invalid(note_repo):
    note_repo.create_note.return_value = Response(
        success=False,
        message="User id or collection id cannot be less than or equal to 0",
        body=None,
    )

    note_service = NoteService(note_repo)

    response = note_service.create_note(data="test data", user_id=0, collection_id=1)

    assert response.success == False
    assert (
        response.message
        == "User id or collection id cannot be less than or equal to 0"
    )


def test_update_note_valid(note_repo):
    note_service = NoteService(note_repo)

    response = note_service.update_note(
        data="test update data", note_id=1, user_id=1, collection_id=1
    )

    assert response.success == True
    assert response.message == "Successfully updated"


def test_update_note_user_id_invalid(note_repo):
    note_repo.update_note.side_effect = Exception(
        "Note id, user_id or collection id cannot be less than or equal to 0"
    )
    note_service = NoteService(note_repo)

    response = note_service.update_note(
        data="test update data", note_id=1, user_id=0, collection_id=1
    )

    assert response.success == False
    assert (
        response.message
        == "Note id, user_id or collection id cannot be less than or equal to 0"
    )


def test_update_note_note_id_invalid(note_repo):
    note_repo.update_note.side_effect = Exception(
        "Note id, user_id or collection id cannot be less than or equal to 0"
    )
    note_service = NoteService(note_repo)

    response = note_service.update_note(
        data="test update data", note_id=0, user_id=1, collection_id=1
    )

    assert response.success == False
    assert (
        response.message
        == "Note id, user_id or collection id cannot be less than or equal to 0"
    )


def test_update_note_collection_id_invalid(note_repo):
    note_repo.update_note.side_effect = Exception(
        "Note id, user_id or collection id cannot be less than or equal to 0"
    )
    note_service = NoteService(note_repo)

    response = note_service.update_note(
        data="test update data", note_id=1, user_id=1, collection_id=0
    )

    assert response.success == False
    assert (
        response.message
        == "Note id, user_id or collection id cannot be less than or equal to 0"
    )


def test_update_note_not_found_invalid(note_repo):
    note_repo.update_note.side_effect = Exception(
        "Note you are trying to update does not exist"
    )

    note_service = NoteService(note_repo)

    response = note_service.update_note(
        data="test update data", note_id=1, user_id=1, collection_id=1
    )

    assert response.success == False
    assert response.message == "Note you are trying to update does not exist"


def test_delete_note(note_repo):
    note_service = NoteService(note_repo)

    response = note_service.delete_note(note_id=1, user_id=1, collection_id=1)

    assert response.success == True
    assert response.message == "Successfully deleted"


def test_delete_note_collection_id_invalid(note_repo):
    note_repo.delete_note.side_effect = Exception(
        "Note id, user id or collection id cannot be less than or equal to 0"
    )

    note_service = NoteService(note_repo)

    response = note_service.delete_note(note_id=1, user_id=1, collection_id=0)

    assert response.success == False
    assert (
        response.message
        == "Note id, user id or collection id cannot be less than or equal to 0"
    )


def test_delete_note_note_id_invalid(note_repo):
    note_repo.delete_note.side_effect = Exception(
        "Note id, user id or collection id cannot be less than or equal to 0"
    )

    note_service = NoteService(note_repo)

    response = note_service.delete_note(note_id=0, user_id=1, collection_id=1)

    assert response.success == False
    assert (
        response.message
        == "Note id, user id or collection id cannot be less than or equal to 0"
    )


def test_delete_note_user_id_invalid(note_repo):
    note_repo.delete_note.side_effect = Exception(
        "Note id, user id or collection id cannot be less than or equal to 0"
    )

    note_service = NoteService(note_repo)

    response = note_service.delete_note(note_id=1, user_id=0, collection_id=1)

    assert response.success == False
    assert (
        response.message
        == "Note id, user id or collection id cannot be less than or equal to 0"
    )


def test_delete_note_not_found_invalid(note_repo):
    note_repo.delete_note.side_effect = Exception(
        "Note you are trying to delete does not exist"
    )

    note_service = NoteService(note_repo)

    response = note_service.delete_note(note_id=1, user_id=1, collection_id=1)

    assert response.success == False
    assert response.message == "Note you are trying to delete does not exist"
