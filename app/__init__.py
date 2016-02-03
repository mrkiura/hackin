from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from config import config
from flask.ext.login import LoginManager

bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()
login_mgr = LoginManager()
login_mgr.session_protection = 'strong'
login_mgr.login_view = 'login'

def create_app(data):
    app = Flask(__name__)
    app.config.from_object(config[data])
    config[data].init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    login_mgr.init_app(app)

    from main import main as main_bp
    from .auth import auth as auth_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    return app
    