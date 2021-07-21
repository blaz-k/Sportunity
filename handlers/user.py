from flask import render_template, request

from models.settings import db
from models.user import User
from hashlib import sha256


def dashboard():
    if request.method == "GET":
        session_cookie = request.cookies.get('session')

        if session_cookie:
            #user = db.query(User).filter_by(session_token=session_cookie).first()
            return render_template("user/dashboard.html")
        else:
            return render_template("public/passwords-not-match.html")
