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


def add_more_product(product_id):
    session_cookie = request.cookies.get("session")
    product = db.query(Product).get(int(product_id))
    user = db.query(User).filter_by(session_token=session_cookie).first()
    cart_item = db.query(Cart).filter_by(user=user, product=product, invoice=None).first()

    cart_item.quantity += 1
    cart_item.save()

    return redirect(url_for("public.cart", product_id=product_id))


def billing():
    session_cookie = request.cookies.get("session")

    if not session_cookie:
        return "ERROR"

    user = db.query(User).filter_by(session_token=session_cookie).first()
    cart_items = db.query(Cart).filter_by(user=user, invoice=None).all()

    if request.method == "GET":

        return render_template("public/billing.html", carts=cart_items)

    elif request.method == "POST":
        first_name = request.form.get("first-name")
        last_name = request.form.get("last-name")
        address = request.form.get("address")
        phone_number = request.form.get("phone-number")
        country = request.form.get("country")
        city = request.form.get("city")

        total = 0
        for cart_item in cart_items:
            total += float(cart_item.product.price) * cart_item.quantity

        # SHIPPING: If total is less than 80 than we add 5 eur
        if total < 80:
            total += 5

        invoice = Invoice(first_name=first_name, last_name=last_name, address=address, phone_number=phone_number,
                          country=country, city=city, user=user, tax="22", total=total)
        invoice.save()

        for cart_item in cart_items:
            cart_item.invoice = invoice
            cart_item.save()

        return redirect(url_for("public.invoice", invoice_id=invoice.id))


def remove_one_cart_product(product_id):
    session_cookie = request.cookies.get("session")
    product = db.query(Product).get(int(product_id))
    user = db.query(User).filter_by(session_token=session_cookie).first()
    cart_item = db.query(Cart).filter_by(user=user, product=product, invoice=None).first()
    # if it is more than 0 you can remove one
    if cart_item.quantity > 1:

        cart_item.quantity -= 1
        cart_item.save()

    return redirect(url_for("public.cart", product_id=product_id))


def add_to_cart(product_id):
    session_cookie = request.cookies.get("session")
    product = db.query(Product).get(int(product_id))
    user = db.query(User).filter_by(session_token=session_cookie).first()
    cart_item = db.query(Cart).filter_by(user=user, product=product, invoice=None).first()

    if not cart_item:
        add_cart = Cart(user=user, product=product, quantity=1)
        add_cart.save()

    else:
        cart_item.quantity += 1
        cart_item.save()

    return redirect(url_for("public.cart", product_id=product_id))


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


def invoice_show(invoice_id):
    invoice = db.query(Invoice).get(int(invoice_id))
    cart_items = db.query(Cart).filter_by(invoice=invoice).all()

    return render_template("public/invoice.html", cart_items=cart_items, invoice=invoice)


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
        session_cookie = request.cookies.get("session")
        product = db.query(Product).get(int(product_id))
        user = db.query(User).filter_by(session_token=session_cookie).first()
        cart_item = db.query(Cart).filter_by(user=user, product=product, invoice=None).first()
        # urediti da ce je produkt zbrisan s strani admina da pokaze template  --- naredi fake delete
        if product:
            cart_item.delete()
        else:
            return "This product does not exist"

        return redirect(url_for("public.cart"))