from models.settings import db


class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.String)
    tax = db.Column(db.String)
    total = db.Column(db.String)
    product_name = db.Column(db.String)
    size = db.Column(db.String)
    quantity = db.Column(db.Integer)
