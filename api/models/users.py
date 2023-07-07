from models import db
from datetime import datetime


class User(db.Model):
    """User model for the application

    Attributes:
        id: unique id for the user
        username: username for the user
        email: unique email for the user
        password: password for the user
        phone: phone number for the user
        isverified: check if the user is verified(boolean)
        type: type of the user, admin or user(default)
        created_at: date and time the user was created
        updated_at: date and time the user was updated
    """

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), index=True, unique=True)
    email = db.Column(db.String(50), index=True, unique=True)
    password = db.Column(db.Text)
    phone = db.Column(db.String(15), index=True, unique=True)
    is_verified = db.Column(db.Boolean, default=False)
    type = db.Column(db.Enum("admin", "user", name="user_type"), default="user")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        """Return a string representation of the user model"""
        return "<User {}-{}>".format(self.username, self.username)
