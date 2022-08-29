from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


db = SQLAlchemy()

DB_DIR = "dbdir"
DB_FILE_NAME = "database.db"
DB_PATH = f"{os.getcwd()}\{DB_DIR}\{DB_FILE_NAME}"

# Context Manger
class SecretKeyFile:
    def __init__(self, filename, method):
        try:
            self.file = open(filename, method)
        # Creates a new file and write a defual value to it
        except FileNotFoundError:
            self.file = open("secret_key.txt", "w+")
            self.file.write("default")

    def __enter__(self):
        return self.file

    def __exit__(self, type, value, traceback):
        self.file.close()

def create_app():

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
    db.init_app(app)

    with SecretKeyFile("secret_key.txt", "r") as f:
        secret_key = f.readline()
        app.config['SECRET_KEY'] = secret_key


    from .views import views
    from .blog import blog
    from.admin import admin

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(blog, url_prefix="/blog")
    app.register_blueprint(admin, url_prefix="/admin")

    from .models import User, Post

    create_database(app)

    return app

def create_database(app):
    #file_path = path.abspath(getcwd())+"database/database.db"

    if not os.path.exists(DB_PATH):
        os.makedirs("dbdir")
        db.create_all(app=app)
        print("Created Database!")
