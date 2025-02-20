from flask import Flask
from app.config import Config
from app.extensions import db, login_manager, migrate, bootstrap
from app.views.auth import auth_bp
from app.models.user import User

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    bootstrap.init_app(app)

    login_manager.login_view = "auth.login_view"

    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app
