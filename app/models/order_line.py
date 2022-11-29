from .db import db

class Order_Line(db.Model):
    __tablename__ = 'order_lines'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('completed_orders.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric, nullable=False)

    product = db.relationship('Product', back_populates='order_line')

    def to_dict(self):
        return {
            'id': self.id,
            'product': self.product,
            'order_id': self.order_id,
            'quantity': self.quantity,
            'price': self.price
        }
