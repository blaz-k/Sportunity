
from flask import render_template, request

from models.user import User
from models.settings import db


def home():
    return render_template("public/index.html")
