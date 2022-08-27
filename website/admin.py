from flask import Blueprint, flash, render_template, redirect, url_for, request, session
from .models import Post
from . import db
from hashlib import md5

admin = Blueprint("admin", __name__)

@admin.route("/", methods=["GET", "POST"])
def admin_home():
	if "is_admin" in session:
		if session["is_admin"]:

			if request.method == "POST":
				print("joe mama")
				title = request.form.get("post_title")
				content = request.form.get("post_content")
				title_exists = Post.query.filter_by(title=title).first()

				if len(title) > 0 and len(content) > 0 and not title_exists:
					print(0)
					key = md5(title.encode()).hexdigest()
					post = Post(title=title, content=content, key=key)
					db.session.add(post)
					db.session.commit()

					flash("Sucessfully Posted the blog")
					"""
					posts = Post.query.all()

					for post in posts:
						print(post.title)

					num_rows_deleted = db.session.query(Post).delete()
					db.session.commit()"""
				else:
					flash("Retry")


			return render_template("admin_home.html")

	return redirect(url_for("admin.admin_login"))


@admin.route("/login", methods=["GET", "POST"])
def admin_login():
	if request.method == "POST":
		username = request.form.get("login_username")
		password = request.form.get("login_password")

		username_key = "nikhil"
		password_key = "qwerty"

		if username == username_key and password == password_key:
			session["is_admin"] = True
			return redirect(url_for("admin.admin_home"))

	return render_template("admin_login.html")

