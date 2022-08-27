from turtle import title
from flask import Blueprint, render_template, request, flash, session, redirect, url_for
from . import db
from .models import User, Post
from .email_verification import *

blog = Blueprint("blog", __name__)



@blog.route("/")
def blog_home():
    posts = Post.query.all()
    return render_template("blog.html", posts=posts)

@blog.route("/<key>")
def full_blog(key):
    post = Post.query.filter_by(key=key).first()
    if post:
        print(post)
        return render_template("full_blog.html", key=key, post=post)
    else:
        return redirect(url_for("blog.blog_home"))

"""
@blog.route("/login", methods=["GET", "POST"])
def blog_login():
    email = request.form.get("login_email")
    password = request.form.get("login_password")

    return render_template("blog_login.html")

@blog.route("/signup", methods=["GET", "POST"])
def blog_signup():
    if request.method == "POST":
        email = request.form.get("signup_email")
        username = request.form.get("signup_username")
        password1 = request.form.get("signup_password1")
        password2 = request.form.get("signup_password2")

        print(email, username, password1, password2)

        # Returns the first and the only user with the email if it exist
        email_exists = User.query.filter_by(email=email).first()

        # Returns the first and the only user with the username if it exist
        username_exists = User.query.filter_by(username=username).first()


        if email_exists:
            flash("User with email already exists.", category="error")

        elif username_exists:
            flash("Username already taken.", category="error")

        elif password1 != password2:
            flash("Passwords don\'t match", category="error")

        elif len(username) < 2:
            flash("Username too short", category="error")

        elif len(password1) < 6:
            flash("Password too short", category="error")

        else:
            otp =  generate_OTP()

            session["email"] = email
            session["username"] = username
            session["password"] = password2
            session["otp"] = otp

            send_verification_code(email=email, username=username, otp=otp)


    return render_template("blog_signup.html")

"""
