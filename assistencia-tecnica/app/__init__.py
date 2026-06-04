from flask import Flask
from app.database.database import init_db


def create_app():
    app = Flask(__name__)
    init_db()
    return app
