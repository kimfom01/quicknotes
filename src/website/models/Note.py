from sqlalchemy import TIMESTAMP
from sqlalchemy.sql import func


from .. import db


class Note(db.Model):
    """
    Note model definition
    """

    __tablename__ = "notes"

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    created_at = db.Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    deleted = db.Column(db.Boolean, default=False)
    updated_at = db.Column(TIMESTAMP(timezone=True), onupdate=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"))
    collection_id = db.Column(db.Integer, db.ForeignKey("collections.id"))

    def __repr__(self):
        return f"Note {self.id}: User {self.user_id}"

    def __eq__(self, other):
        if isinstance(other, Note):
            return self.id == other.id
        return False

    def __ne__(self, other):
        return not self.__eq__(other)
