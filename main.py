from flask import Flask
from models.settings import db
from handlers import public, auth


app = Flask(__name__)

db.create_all()

# PUBLIC
app.add_url_rule(rule="/", endpoint="public.home", view_func=public.home, methods=["GET"])
app.add_url_rule(rule="/shop", endpoint="public.shop", view_func=public.shop, methods=["GET"])
app.add_url_rule(rule="/about", endpoint="public.about", view_func=public.about, methods=["GET"])
app.add_url_rule(rule="/contact", endpoint="public.contact", view_func=public.contact, methods=["GET"])

# AUTHENTICATION
app.add_url_rule(rule="/registration", endpoint="auth.registration", view_func=auth.registration, methods=["GET", "POST"])
app.add_url_rule(rule="/login", endpoint="public.login", view_func=public.login, methods=["GET"])


if __name__ == '__main__':
    app.run(use_reloader=True)