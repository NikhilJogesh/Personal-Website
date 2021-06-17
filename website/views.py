from flask import Blueprint, render_template
# This file is used to store all the URLs the user can view

views = Blueprint("views", __name__)

@views.route("/home")
@views.route("/")
def home():
    return render_template("home.html")

@views.route("/projects")
def projects():
    return render_template("projects.html")

@views.route("/contacts")
def contacts():
    return render_template("contacts.html")

