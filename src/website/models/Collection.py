from .. import db


class Collection(db.Model):
    """
    Collection model definition
    """

    __tablename__ = "collections"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"))
    notes = db.relationship("Note", backref="Collection", passive_deletes=True)

    def __repr__(self):
        return f"User {self.id}: {self.email}"

    def __eq__(self, other):
        if isinstance(other, Collection):
            return self.id == other.id
        return False

    def __ne__(self, other):
        return not self.__eq__(other)
