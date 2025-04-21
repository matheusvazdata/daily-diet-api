from flask import Flask
from .database import db
from .routes import bp as main_routes

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../.env')
    db.init_app(app)
    app.register_blueprint(main_routes)

    from . import models

    return app