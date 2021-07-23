from models.settings import db
from models.user import User
from models.product import Product

from flask import render_template, request


def about():
    session_cookie = request.cookies.get("session")

    if request.method == "GET":

        if session_cookie:
            user = db.query(User).filter_by(session_token=session_cookie).first()
            if user:
                return render_template("public/about.html", user=user)
    return render_template("public/about.html")


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

    if request.method == "GET":

        if session_cookie:
            user = db.query(User).filter_by(session_token=session_cookie).first()
            if user:
                return render_template("public/cart.html", user=user)
    return render_template("public/cart.html")


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
