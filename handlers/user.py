from flask import render_template, request

from models.settings import db
from models.user import User
from hashlib import sha256


def dashboard():
    session_cookie = request.cookies.get('session')
    if session_cookie:

        user = db.query(User).filter_by(session_token=session_cookie).first()
        if user:
            return render_template("user/dashboard.html", user=user)

    return render_template("public/error.html")


def edit_profile():
    session_cookie = request.cookies.get('session')
    if session_cookie:
        user = db.query(User).filter_by(session_token=session_cookie).first()

        if not user:
            return render_template("public/error.html")

    else:
        return render_template("public/error.html")

    if request.method == "GET":
        return render_template("user/edit-profile.html", user=user)

    if request.method == "POST":
        first_name = request.form.get("first-name")
        last_name = request.form.get("last-name")
        email = request.form.get("email")
        address = request.form.get("address")
        country = request.form.get("country")
        phone_number = request.form.get("phone-number")
        password = request.form.get("password")

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.address = address
        user.country = country
        user.phone_number = phone_number
        user.password = sha256(password.encode("utf-8")).hexdigest()

        user.save()

        return render_template("user/profile-changes.html")



