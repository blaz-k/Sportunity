from flask import render_template, request

from models.settings import db
from models.user import User
from hashlib import sha256



def add_product():
    return render_template("admin/add-product.html")