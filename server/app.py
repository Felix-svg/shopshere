from config import app
from models.cart import Cart
from models.cart_item import CartItem
from models.order import Order
from models.order_item import OrderItem
from models.product import Product
from models.user import User




if __name__ == "__main__":
    app.run(debug=True)