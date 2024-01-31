import atexit
import json
import logging.config
import logging.handlers
import pathlib
from os import getenv
from flask import Flask, render_template
from authlib.integrations.flask_client import OAuth
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv
from flask_migrate import Migrate

db = SQLAlchemy()

load_dotenv()

app_config = {
    "OAUTH2_CLIENT_ID": getenv("OAUTH2_CLIENT_ID"),
    "OAUTH2_CLIENT_SECRET": getenv("OAUTH2_CLIENT_SECRET"),
    "OAUTH2_META_URL": getenv("OAUTH2_META_URL"),
    "FLASK_SECRET": getenv("FLASK_SECRET"),
    "DB_URI": getenv("DB_URI"),
}

oauth = OAuth()

oauth.register(
    "notes_app",
    client_id=app_config.get("OAUTH2_CLIENT_ID"),
    client_secret=app_config.get("OAUTH2_CLIENT_SECRET"),
    server_metadata_url=app_config.get("OAUTH2_META_URL"),
    client_kwargs={"scope": "openid profile email"},
)

# logger = logging.getLogger(__name__)


# def setup_loggin():
#     config_file = pathlib.Path("logging_configs/config.json")

#     with open(config_file) as file:
#         config = json.load(file)

#     logging.config.dictConfig(config)

#     queue_handler = logging.getHandlerByName("queue_handler")
#     if queue_handler is not None:
#         queue_handler.listener.start()
#         atexit.register(queue_handler.listener.stop)


def create_app():
    """
    Initialize app
    """
    app = Flask(__name__)
    app.config["SECRET_KEY"] = app_config.get("FLASK_SECRET")
    app.config["SQLALCHEMY_DATABASE_URI"] = app_config.get("DB_URI")

    db.init_app(app)

    # setup_loggin()

    from .routers.views_route import views
    from .routers.auth_route import auth
    from .routers.notes_route import notes

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(notes, url_prefix="/")

    @app.errorhandler(404)
    def not_found(error):
        return render_template("404.html"), 404

    from .models.User import User

    Migrate(app, db)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id: str) -> User | None:
        return User.query.get((int(id)))

    return app
