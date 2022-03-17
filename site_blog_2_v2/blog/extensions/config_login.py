from flask_login import LoginManager

login_manager = LoginManager()


def init_app(app) -> None:
    login_manager.init_app(app)
    login_manager.session_protection = "strong"

    login_manager.login_view = "authentication.login"
    login_manager.login_message = "Não autorizado!"
    login_manager.login_message_category = "info"
