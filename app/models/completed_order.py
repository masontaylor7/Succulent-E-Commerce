from .db import db

class Completed_Order(db.Model):
    __tablename__ = 'completed_orders'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    order_date = db.Column(db.DateTime, nullable=False,server_default=db.func.now())
    shipping_address_id = db.Column(db.Integer, db.ForeignKey('addresses.id'), nullable=False)
    order_total = db.Column(db.Numeric, nullable=False)
    order_status = db.Column(db.String(40), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'order_date': self.order_date,
            'shipping_address_id': self.shipping_address_id,
            'order_total': self.order_total,
            'order_status': self.order_status
        }
