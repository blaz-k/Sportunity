from models.settings import db
from datetime import datetime


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tags = db.Column(db.String)
    price = db.Column(db.String)
    tax = db.Column(db.String)
    total = db.Column(db.String)
    information = db.Column(db.String)
    product_name = db.Column(db.String)
    size = db.Column(db.String)
    image = db.Column(db.String)
    stock = db.Column(db.Integer)
    deleted = db.Column(db.Boolean, default=False)
    created = db.Column(db.DateTime, default=datetime.now())
