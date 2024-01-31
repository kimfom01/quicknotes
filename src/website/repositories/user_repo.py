from werkzeug.security import generate_password_hash

from ..models.User import User
from .. import db


class UserRepo:
    def get_by_email(self, email: str) -> User:
        return User.query.filter_by(email=email).first()

    def create_user(self, email: str, first_name: str, password: str) -> User:
        password_hash = generate_password_hash(password, method="sha256")
        user = User(email=email, first_name=first_name, password=password_hash)

        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)

        return user

    def create_google_user(self, email: str, first_name: str) -> User:
        user = User(email=email, first_name=first_name)

        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)

        return user

user_repo = UserRepo()
