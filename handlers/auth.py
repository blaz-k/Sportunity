from flask import render_template, request, make_response, redirect, url_for

from models.settings import db
from models.user import User
from hashlib import sha256
import uuid


def registration():
    if request.method == "GET":
        return render_template("public/registration.html")

    elif request.method == "POST":

        first_name = request.form.get("first-name")
        last_name = request.form.get("last-name")
        email = request.form.get("email")
        address = request.form.get("address")
        country = request.form.get("country")
        phone_number = request.form.get("phone-number")
        password = request.form.get("password")
        password_repeat = request.form.get("password-repeat")

        existing_user = db.query(User).filter_by(email=email).first()

        if existing_user:
            return render_template("public/existing-email.html")

        else:
            if password == password_repeat:
                password_hash = sha256(password.encode("utf-8")).hexdigest()

                new_user = User(first_name=first_name, last_name=last_name, email=email,
                                address=address, country=country, phone_number=phone_number, password=password_hash)
                new_user.save()
                return render_template("public/successful-registration.html")
            else:
                return render_template("public/passwords-not-match.html")


def login():
    if request.method == "GET":
        return render_template("public/login.html")

    elif request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        password_hash = sha256(password.encode("utf-8")).hexdigest()

        existing_user = db.query(User).filter_by(email=email, password=password_hash).first()

        if existing_user:
            session_token = str(uuid.uuid4())
            existing_user.session_token = session_token
            existing_user.save()

            response = make_response(redirect(url_for("user.dashboard")))
            response.set_cookie("session", session_token)
            return response

        else:
            return render_template("public/email-password-incorrect.html")
    return redirect(url_for("user.dashboard"))


def logout():
    session_cookie = request.cookies.get("session")
    user = db.query(User).filter_by(session_token=session_cookie).first()
    user.session_token = ""
    user.save()

    return redirect(url_for("public.login"))


