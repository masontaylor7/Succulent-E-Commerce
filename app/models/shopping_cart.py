from .db import db

class Shopping_Cart(db.Model):
    __tablename__ = 'shopping_carts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=True)

    user = db.relationship('User', uselist=False, back_populates='shopping_cart')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id
        }
