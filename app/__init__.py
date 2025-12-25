from flask import Flask
from dotenv import load_dotenv
from app.blueprints.auth.routes import auth_bp


def create_app():
    load_dotenv() 
    app = Flask(__name__)
    app.register_blueprint(auth_bp)
    return app
