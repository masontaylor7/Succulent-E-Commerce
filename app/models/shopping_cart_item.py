from .db import db

class Shopping_Cart_Item(db.Model):
    __tablename__ = 'shopping_cart_items'

    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('shopping_carts.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    product = db.relationship('Product', back_populates='shopping_cart_item')

    def to_dict(self):
        return {
            'id': self.id,
            'cart_id': self.cart_id,
            'quantity': self.quantity,
            'product': self.product,
        }
