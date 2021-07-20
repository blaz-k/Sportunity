from flask import Flask
from models.settings import db

from handlers import public


app = Flask(__name__)

db.create_all()

# PUBLIC
app.add_url_rule(rule="/", endpoint="public.home", view_func=public.home, methods=["GET"])

if __name__ == '__main__':
    app.run(use_reloader=True)