from typing import List


from ..models.Collection import Collection
from ..models.Note import Note
from .. import db


class NotesRepo:
    def get_by_id(self, id: int, user_id: int, collection_id: int) -> Note:
        return Note.query.filter_by(
            collection_id=collection_id, id=id, user_id=user_id
        ).first()

    def get_all(self, user_id: int, collection_id: int) -> List[Note]:
        return Note.query.filter_by(
            collection_id=collection_id, deleted=False, user_id=user_id
        ).all()

    def get_collections(self, user_id: int) -> List[Collection]:
        return Collection.query.filter_by(user_id=user_id).all()

    def create_note(self, data: str, user_id: int, collection_id: int) -> Note:
        note = Note(
            data=data, user_id=user_id, collection_id=collection_id, deleted=False
        )

        db.session.add(note)
        db.session.commit()
        db.session.refresh(note)

        return note

    def update_note(
        self, data: str, note_id: int, user_id: int, collection_id: int
    ) -> None:
        note = Note.query.filter_by(
            id=note_id, collection_id=collection_id, user_id=user_id
        ).first()

        if note is None:
            raise Exception("Note you are trying to update does not exist")

        note.data = data
        db.session.commit()

    def delete_note(self, note_id: int, user_id: int, collection_id: int) -> None:
        note = Note.query.filter_by(
            id=note_id, collection_id=collection_id, user_id=user_id
        ).first()

        if note is None:
            raise Exception("Note you are trying to delete does not exist")

        note.deleted = True
        db.session.commit()


notes_repo = NotesRepo()
