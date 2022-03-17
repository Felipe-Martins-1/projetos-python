from dynaconf import FlaskDynaconf


def init_app(app) -> None:
    FlaskDynaconf(app)
