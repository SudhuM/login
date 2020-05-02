from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from login_system.config import Config


db = SQLAlchemy()


def create_app(config_class=Config):

    app = Flask(__name__)

    app.config.from_object(Config)

    with app.app_context():
        db.init_app(app)

        from login_system.users.routes import users

        app.register_blueprint(users, url_prefix='/users')

    return app
