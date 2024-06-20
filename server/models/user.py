from config import db, bcrypt
from flask_login import UserMixin, login_manager
from sqlalchemy_serializer import SerializerMixin


class User(db.Model, UserMixin, SerializerMixin):
    # __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(150), nullable=True)
    cart = db.relationship("Cart", back_populates="user")
    order = db.relationship("Order", back_populates="user")



