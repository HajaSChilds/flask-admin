from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


db = SQLAlchemy()

def create_app(config_rule):
    
    app = Flask(__name__)
    app.config.from_object(config[config_rule])

    app.config.from_pyfile("../config.py")

    db.init_app(app)


    # Flask Admin Configuration
    app.config["FLASK_ADMIN_SWATCH"] = "Cyborg"
    admin = Admin(app, name="International Artists Database",
                template_mode="bootstrap3")

    admin.add_view(ModelView(models.User, db.session))
    admin.add_view(ModelView(models.Artists, db.session))
    admin.add_view(ModelView(models.Songs, db.session))
    
    return app
