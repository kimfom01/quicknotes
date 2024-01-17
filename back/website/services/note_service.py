from ..repositories import notes_repo
from ..schema.Response import Response
from ..repositories.notes_repo import NotesRepo, notes_repo


class NoteService:
    def __init__(self, notes_repo: NotesRepo) -> None:
        self.notes_repo = notes_repo

    def get_by_id(self, id: int, collection_id: int) -> Response:
        if id <= 0 or collection_id <= 0:
            return Response(
                success=False,
                message="Id or Collection id cannot be less than or equal to 0",
                body=None,
            )

        note = self.notes_repo.get_by_id(id=id, collection_id=collection_id)

        if note is None:
            return Response(success=False, message="Note not found", body=None)
        return Response(success=True, message="Success", body=note)

    def get_all(self, collection_id: int) -> Response:
        if collection_id <= 0:
            return Response(
                success=False,
                message="Collection id cannot be less than or equal to 0",
                body=None,
            )

        notes = self.notes_repo.get_all(collection_id=collection_id)

        if notes is None:
            return Response(success=False, message="Notes not found", body=None)
        return Response(success=True, message="Success", body=notes)

    def create_note(self, data: str, user_id: int, collection_id: int) -> Response:
        try:
            if len(data) < 1:
                return Response(
                    success=False,
                    message="Unable to create, data is invalid",
                    body=None,
                )

            if user_id <= 0 or collection_id <= 0:
                raise Exception(
                    "Unable to create, user id or collection id cannot be less than or equal to 0"
                )

            note = self.notes_repo.create_note(
                data=data, user_id=user_id, collection_id=collection_id
            )

            return Response(success=True, message="Successfully created", body=note)
        except Exception as ex:
            return Response(
                success=False,
                message=str(ex),
                body=None,
            )

    def delete_note(self, note_id: int, collection_id: int) -> Response:
        try:
            if note_id <= 0 or collection_id <= 0:
                raise Exception(
                    "Unable to delete, note id or collection id cannot be less than or equal to 0"
                )

            self.notes_repo.delete_note(note_id=note_id, collection_id=collection_id)

            return Response(success=True, message="Successfully deleted", body=None)
        except Exception as ex:
            return Response(success=False, message=str(ex), body=None)


note_service = NoteService(notes_repo)
