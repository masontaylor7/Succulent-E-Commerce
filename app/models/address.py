from .db import db

class Address(db.Model):
    __tablename__ = 'addresses'

    id = db.Column(db.Integer, primary_key=True)
    address_line1 = db.Column(db.String(255), nullable=False)
    address_line2 = db.Column(db.String(255), nullable=True)
    city = db.Column(db.String(255), nullable=False)
    postal_code = db.Column(db.String(10), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'address_line1': self.address_line1,
            'address_line2': self.address_line2,
            'city': self.city,
            'postal_code': self.postal_code,
        }
