from flask import Flask
from models.settings import db
from handlers import public, auth, user, admin


app = Flask(__name__)

db.create_all()


# AUTHENTICATION
app.add_url_rule(rule="/registration", endpoint="auth.registration", view_func=auth.registration, methods=["GET", "POST"])
app.add_url_rule(rule="/login", endpoint="public.login", view_func=auth.login, methods=["GET", "POST"])
app.add_url_rule(rule="/logout", endpoint="public.logout", view_func=auth.logout, methods=["GET"])

# PUBLIC
app.add_url_rule(rule="/", endpoint="public.home", view_func=public.home, methods=["GET"])
app.add_url_rule(rule="/shop", endpoint="public.shop", view_func=public.shop, methods=["GET"])
app.add_url_rule(rule="/about", endpoint="public.about", view_func=public.about, methods=["GET"])
app.add_url_rule(rule="/contact", endpoint="public.contact", view_func=public.contact, methods=["GET"])
app.add_url_rule(rule="/cart", endpoint="public.cart", view_func=public.cart, methods=["GET"])
app.add_url_rule(rule="/billing", endpoint="public.billing", view_func=public.billing, methods=["GET"])


# USER
app.add_url_rule(rule="/dashboard", endpoint="user.dashboard", view_func=user.dashboard, methods=["GET"])
app.add_url_rule(rule="/edit-profile", endpoint="user.edit-profile", view_func=user.edit_profile, methods=["GET", "POST"])

# ADMIN
app.add_url_rule(rule="/add-product", endpoint="admin.add-product", view_func=admin.add_product, methods=["GET", "POST"])


if __name__ == '__main__':
    app.run(use_reloader=True)