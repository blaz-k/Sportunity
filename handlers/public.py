from flask import redirect, url_for
from models.settings import db
from models.product import Product
from models.cart import Cart
from models.user import User
from models.invoice import Invoice


from flask import render_template, request


def about():
    session_cookie = request.cookies.get("session")
    if request.method == "GET":

        if session_cookie:
            user = db.query(User).filter_by(session_token=session_cookie).first()
            if user:
                return render_template("public/about.html", user=user)
    return render_template("public/about.html")


def add_to_cart(product_id):
    session_cookie = request.cookies.get("session")
    product = db.query(Product).get(int(product_id))
    user = db.query(User).filter_by(session_token=session_cookie).first()

    add_cart = Cart(user=user, product=product)
    add_cart.save()

    return redirect(url_for("public.cart", product_id=product_id))


def billing():
    session_cookie = request.cookies.get("session")

    if request.method == "GET":

        if session_cookie:
            user = db.query(User).filter_by(session_token=session_cookie).first()
            if user:
                return render_template("public/billing.html", user=user)
    return render_template("public/billing.html")


def cart():
    session_cookie = request.cookies.get("session")
    products = db.query(Product).all()
    user = db.query(User).filter_by(session_token=session_cookie).first()
    carts = db.query(Cart).filter_by(user=user).all()

    if request.method == "GET":

        if session_cookie:
            user = db.query(User).filter_by(session_token=session_cookie).first()
            if user:
                return render_template("public/cart.html", user=user, products=products, carts=carts)
    return render_template("public/cart.html", products=products, carts=carts)


def contact():
    session_cookie = request.cookies.get("session")

    if request.method == "GET":

        if session_cookie:
            user = db.query(User).filter_by(session_token=session_cookie).first()
            if user:
                return render_template("public/contact.html", user=user)
        return render_template("public/contact.html")


def home():
    return render_template("public/index.html")


def shop():
    session_cookie = request.cookies.get("session")
    products = db.query(Product).all()
    if request.method == "GET":

        if session_cookie:
            user = db.query(User).filter_by(session_token=session_cookie).first()
            if user:
                return render_template("public/shop.html", user=user, products=products)
        return render_template("public/shop.html", products=products)


def delete_cart_product(product_id):
    if request.method == "POST":

        product = db.query(Product).filter_by(id=int(product_id)).first()
        """
        image = request.form.get("image")
        product_name
        price = 
        """
        product.delete()

        return redirect(url_for("public.cart"))