
from flask import render_template


def home():
    return render_template("public/index.html")


def shop():
    return render_template("public/shop.html")


def about():
    return render_template("public/about.html")


def contact():
    return render_template("public/contact.html")



def login():
    return render_template("public/login.html")