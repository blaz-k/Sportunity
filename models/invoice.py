from models.settings import db
from datetime import datetime


class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    address = db.Column(db.String)
    phone_number = db.Column(db.String)
    country = db.Column(db.String)
    tax = db.Column(db.String)  # v procentih
    total = db.Column(db.String)  # with tax
    quantity = db.Column(db.Integer)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User")
    id_product = db.Column(db.Integer, db.ForeignKey('products.id'))
    product = db.relationship("Product")
    created = db.Column(db.DateTime, default=datetime.now())
