from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

def create_app(config):
    
    app = Flask(__name__)
    app.config.from_pyfile("../config.py")

    db.init_app(app)
    
    return app
