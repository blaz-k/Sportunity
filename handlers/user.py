from flask import render_template, request

from models.settings import db
from models.user import User


def dashboard():
    session_cookie = request.cookies.get('session')
    if session_cookie:

        user = db.query(User).filter_by(session_token=session_cookie).first()
        if user:
            return render_template("user/dashboard.html", user=user)

    return render_template("public/error.html")


def edit_profile():
    return render_template("user/edit-profile.html")
