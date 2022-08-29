from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import json

db = SQLAlchemy()

DB_DIR = "dbdir"
DB_FILE_NAME = "database.db"
DB_PATH = f"{os.getcwd()}\{DB_DIR}\{DB_FILE_NAME}"

CONFIG_FILE = "config.json"


def create_app():

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
    db.init_app(app)

    # Creates the config file if it does not already exist
    create_config_file()

    with open(CONFIG_FILE, "r") as f:
        json_file = json.load(f)
        app.config['SECRET_KEY'] = json_file["secret_key"]


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

def create_config_file():
    if not os.path.exists(CONFIG_FILE):

        # Data to be written
        data = {
            "secret_key": "sathiyajith",
            "email_address": "",
            "email_password": ""

        }

        # Serializing json
        json_object = json.dumps(data, indent=4)

        # Writing to sample.json
        with open(CONFIG_FILE, "w") as file:
            file.write(json_object)