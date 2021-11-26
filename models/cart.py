from models.settings import db


class Cart(db.Model):
    __tablename__ = "Cart"

    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User")
    id_product = db.Column(db.Integer, db.ForeignKey('products.id'))
    product = db.relationship("Product")
    id_invoice = db.Column(db.Integer, db.ForeignKey('invoices.id'))
    invoice = db.relationship("Invoice")
    quantity = db.Column(db.Integer)

