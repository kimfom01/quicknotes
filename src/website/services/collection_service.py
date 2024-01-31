from ..schema.Response import Response
from ..repositories.collection_repo import CollectionRepo, collection_repo


class CollectionService:
    def __init__(self, collection_repo: CollectionRepo) -> None:
        self.collection_repo = collection_repo

    def get_collections(self, user_id: int) -> Response:
        if user_id <= 0:
            return Response(
                success=False,
                message="User id cannot be less than or equal to 0",
                body=None,
            )

        collections = self.collection_repo.get_collections(user_id=user_id)

        if collections is None:
            return Response(success=False, message="Collections not found", body=None)
        return Response(success=True, message="Success", body=collections)

    def get_default_collection(self, user_id: int) -> Response:
        if user_id <= 0:
            return Response(
                success=False,
                message="User id cannot be less than or equal to 0",
                body=None,
            )

        collection = self.collection_repo.get_default_collection(user_id=user_id)

        if collection is None:
            return Response(
                success=False, message="Default Collection not found", body=None
            )
        return Response(success=True, message="Success", body=collection)

    def create_collection(self, title: str, user_id: int) -> Response:
        try:
            if user_id <= 0:
                raise Exception("User id cannot be less than or equal to 0")

            title = title.strip()

            if len(title) <= 0:
                raise Exception("Collection title cannot be empty")

            collection = self.collection_repo.create_collection(
                title=title, user_id=user_id
            )

            return Response(
                success=True, message="Successfully created", body=collection
            )
        except Exception as ex:
            return Response(success=False, message=str(ex), body=None)


collection_service = CollectionService(collection_repo)
