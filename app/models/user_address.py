from .db import db

class User_Address(db.Model):
    __tablename__ = 'user_addresses'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('addresses.id'), nullable=False)
