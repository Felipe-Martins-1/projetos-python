from flask import Flask
from .extensions import configuration
from .blueprints import home


def create_app():
    app = Flask(__name__)
    configuration.init_app(app)
    app.register_blueprint(home.bp)
    return app
