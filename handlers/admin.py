from flask import render_template, request, redirect, url_for

from models.settings import db
from models.user import User
from models.product import Product
from models.invoice import Invoice
from models.cart import Cart


def add_product():
    session_cookie = request.cookies.get("session")
    user = db.query(User).filter_by(session_token=session_cookie).first()

    if user.admin is False:
        return render_template("admin/not-admin.html")

    if request.method == "GET":
        return render_template("admin/add-product.html")

    if request.method == "POST":

        product_name = request.form.get("product-name")
        tags = request.form.get("tags")
        size = request.form.get("size")
        price = request.form.get("price")
        information = request.form.get("information")
        image = request.form.get("image")
        stock = request.form.get("stock")

        new_product = Product(product_name=product_name, tags=tags, size=size,
                              price=price, information=information, image=image, stock=stock)
        new_product.save()

        return redirect(url_for("user.dashboard"))

    if not user:
        return redirect(url_for("/auth/login"))


def billing():
    session_cookie = request.cookies.get("session")
    products = db.query(Product).all()
    user = db.query(User).filter_by(session_token=session_cookie).first()
    carts = db.query(Cart).filter_by(user=user).all()

    if session_cookie:
        user = db.query(User).filter_by(session_token=session_cookie).first()
        if user:
            return render_template("public/billing.html", user=user, products=products, carts=carts)
    return render_template("public/billing.html", products=products, carts=carts)


def delete_product(product_id):
    session_cookie = request.cookies.get("session")
    user = db.query(User).filter_by(session_token=session_cookie).first()

    if user.admin is False:
        return render_template("admin/not-admin.html")

    product = db.query(Product).get(int(product_id))

    if request.method == "POST":
        product.delete()
        return redirect(url_for("user.dashboard"))


def invoice(cart_id):
    first_name = request.form.get("first-name")
    last_name = request.form.get("last-name")
    address = request.form.get("address")
    phone_number = request.form.get("phone-number")
    country = request.form.get("country")

    # dobi userja
    session_cookie = request.cookies.get("session")

    # dobit moras cart_id
    carts = db.query(Cart).get(int(cart_id))

    new_invoice = Invoice(first_name=first_name, last_name=last_name,
                          address=address, phone_number=phone_number, country=country)
    new_invoice.save()

    #carts.invoice
    #carts
    return render_template("admin/invoice.html")

