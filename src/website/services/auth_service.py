from flask_login import login_user
from werkzeug.security import check_password_hash

from ..schema.Response import Response
from ..services.user_service import UserService, user_service
from ..services.collection_service import CollectionService, collection_service


class AuthService:
    def __init__(
        self, collection_service: CollectionService, user_service: UserService
    ) -> None:
        self.collection_service = collection_service
        self.user_service = user_service

    def login_user(
        self, email: str, password: str | None = None, demo: bool = False
    ) -> Response:
        if password and len(password) < 7:
            return Response(
                success=False,
                message="Password must be greater than 6 characters",
                body=None,
            )
        else:
            response = self.user_service.get_by_email(email=email)

            if not response.success:
                return Response(success=False, message=response.message, body=None)

            user = response.body

            response = self.collection_service.get_default_collection(user_id=user.id)

            if not response.success:
                return Response(success=False, message=response.message, body=None)

            default_collection = response.body

            if not user.password:
                return Response(
                    success=False,
                    message="You do not have a password!\nClick Sign in with Google to continue",
                    body=None,
                )

            if demo:
                login_user(user, remember=True)
                return Response(
                    success=True,
                    message="Demo logged in successfully!",
                    body=default_collection,
                )

            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                return Response(
                    success=True,
                    message="Logged in successfully!",
                    body=default_collection,
                )
            return Response(
                success=False,
                message="Invalid email or password!",
                body=None,
            )

    def sign_up_user(
        self,
        first_name: str,
        email: str,
        password: str | None = None,
        google: bool = False,
    ) -> Response:
        response = self.user_service.get_by_email(email=email)
        if response.success:
            if google:
                user = response.body
                login_user(user)
                return Response(
                    success=True, message="Logged in successfully!", body=user
                )
            else:
                return Response(success=False, message="User already exist!", body=None)

        response = self.user_service.create_user(
            email=email, password=password, first_name=first_name, google=google
        )

        if not response.success:
            return Response(success=False, message=response.message, body=None)

        user = response.body
        login_user(user)

        return Response(success=True, message=response.message, body=user)


auth_service = AuthService(collection_service, user_service)
