from flask import render_template, request, redirect, url_for

from models.settings import db
from models.user import User
from models.product import Product
from hashlib import sha256


def add_product():
    session_cookie = request.cookies.get("session")
    user = db.query(User).filter_by(session_token=session_cookie).first()

    if request.method == "GET":
        return render_template("admin/add-product.html")

    if request.method == "POST":

        product_name = request.form.get("product-name")
        tags = request.form.get("tags")
        size = request.form.get("size")
        price = request.form.get("price")
        information = request.form.get("information")
        image = request.form.get("image")

        new_product = Product(product_name=product_name, tags=tags, size=size,
                              price=price, information=information, image=image)
        new_product.save()

        return redirect(url_for("user.dashboard"))

    if not user:
        return redirect(url_for("/auth/login"))