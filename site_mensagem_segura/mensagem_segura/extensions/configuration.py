from dynaconf import FlaskDynaconf

# Função que invoca a classe responsável por indentificar as
# configurações definidas nos arquivos ".env" e "settings.toml"
# Os mesmos possuem variáveis de ambiente do Flask e seus valores
def init_app(app):
    FlaskDynaconf(app)
