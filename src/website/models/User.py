from flask_login import UserMixin
from sqlalchemy.sql.expression import func
from sqlalchemy.sql.sqltypes import TIMESTAMP


from .. import db


class User(db.Model, UserMixin):
    """
    User model definition
    """

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=True)
    created_at = db.Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    updated_at = db.Column(TIMESTAMP(timezone=True), onupdate=func.now())
    first_name = db.Column(db.String(150))
    collections = db.relationship(
        "Collection", cascade="all, delete", backref="User", passive_deletes=True
    )
    notes = db.relationship(
        "Note", cascade="all, delete", backref="User", passive_deletes=True
    )

    def __repr__(self):
        return f"User {self.id}: {self.email}"

    def __eq__(self, other):
        if isinstance(other, User):
            return self.id == other.id
        return False

    def __ne__(self, other):
        return not self.__eq__(other)
