from flask import Flask

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

    with SecretKeyFile("secret_key.txt", "r") as f:
        secret_key = f.readline()
        app.config['SECRET_KEY'] = secret_key


    from .views import views

    app.register_blueprint(views, url_prefix="/")



    return app
