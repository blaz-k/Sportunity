
from flask import render_template, request

from models.user import User
from models.settings import db


def home():
    return render_template("public/index.html")


def shop():
    return render_template("public/shop.html")


def about():
    return render_template("public/about.html")


def contact():
    return render_template("public/contact.html")


def registration():
    return render_template("public/registration.html")