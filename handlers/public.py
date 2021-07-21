from models.settings import db
from models.user import User

from flask import render_template, request


def home():
    return render_template("public/index.html")


def shop():
    session_cookie = request.cookies.get("session")

    if request.method == "GET":

        if session_cookie:
            user = db.query(User).filter_by(session_token=session_cookie).first()
            if user:
                return render_template("public/shop.html", user=user)
        return render_template("public/shop.html")


def about():
    session_cookie = request.cookies.get("session")

    if request.method == "GET":

        if session_cookie:
            user = db.query(User).filter_by(session_token=session_cookie).first()
            if user:
                return render_template("public/about.html", user=user)
    return render_template("public/about.html")


def contact():
    session_cookie = request.cookies.get("session")

    if request.method == "GET":

        if session_cookie:
            user = db.query(User).filter_by(session_token=session_cookie).first()
            if user:
                return render_template("public/contact.html", user=user)
        return render_template("public/contact.html")

