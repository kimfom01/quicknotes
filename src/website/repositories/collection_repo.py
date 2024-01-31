from typing import List
from ..models.Collection import Collection
from ..schema.Response import Response
from .. import db


DEFAULT_COLLECTION = "Default Collection"


class CollectionRepo:
    def get_collections(self, user_id: int) -> List[Collection]:
        return Collection.query.filter_by(user_id=user_id).all()

    def get_default_collection(self, user_id: int) -> Collection:
        return Collection.query.filter_by(
            user_id=user_id, title=DEFAULT_COLLECTION
        ).first()

    def create_collection(self, title: str, user_id: int) -> Collection:
        collection = Collection(title=title, user_id=user_id)

        db.session.add(collection)
        db.session.commit()
        db.session.refresh(collection)

        return collection

    def create_default_collection(self, user_id: int) -> Collection:
        collection = Collection(title=DEFAULT_COLLECTION, user_id=user_id)

        db.session.add(collection)
        db.session.commit()
        db.session.refresh(collection)

        return collection


collection_repo = CollectionRepo()
