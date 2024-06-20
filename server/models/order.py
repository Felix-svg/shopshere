from config import db
from sqlalchemy_serializer import SerializerMixin


class Order(db.Model, SerializerMixin):
    __tabelname__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    order_items = db.relationship("OrderItem", back_populates="order")
    total_price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False, default="Pending")
