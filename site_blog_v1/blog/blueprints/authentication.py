from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash,
    g,
)
from werkzeug.security import generate_password_hash, check_password_hash
from .database import User, db

bp = Blueprint("authentication", __name__)


@bp.route("/registrar", methods=["GET", "POST"])
def register():
    try:
        if g.id_user:
            return redirect(url_for("blog.my_posts"))
        else:
            if request.method == "POST":
                name = request.form["name"]
                name_user = request.form["name_user"]
                password = generate_password_hash(request.form["password"])
                user = User.query.filter_by(name_user=name_user).first()
                if user:
                    flash(f"Nome de usuário indisponível!")
                else:
                    user = User(name, name_user, password)
                    db.session.add(user)
                    db.session.commit()
                    db.session.close()
                    flash("Registrado!")
    except Exception as e:
        flash("Erro ao registrar!")
        print(f"\nERRO AO REGISTRAR: {e}")
    return render_template("authentication/register.html", title="Registrar")


@bp.route("/entrar", methods=["GET", "POST"])
def login():
    try:
        if g.id_user:
            return redirect(url_for("blog.my_posts"))
        else:
            if request.method == "POST":
                name_user = request.form["name_user"]
                password = request.form["password"]
                user = User.query.filter_by(name_user=name_user).first()
                if user:
                    if check_password_hash(user.password, password):
                        session.clear()
                        session["id_user"] = user.id_user
                        print("ID SESSÃO SETADO")
                        return redirect(url_for("blog.my_posts"))
                    else:
                        flash("Senha inválida!")
                else:
                    flash("Nome de usuário invalído!")
    except Exception as e:
        flash("Erro ao entrar!")
        print(f"\nERRO AO ENTRAR: {e}")
    return render_template("authentication/login.html", title="Entrar")


@bp.route("/sair")
def logout():
    try:
        session.clear()
        print("ID SESSÃO APAGADO")
    except Exception as e:
        flash("Erro ao sair!")
        print(f"\nERRO AO SAIR: {e}")
    return redirect(url_for("blog.index"))


# Função que sempre é invocada automaticamente quando uma página web é carregada
# ou recarregada, a mesma, verifica se há um valor (id) armazenado na sessão do
# navegador
@bp.before_app_request
def load_logged_in_user():
    try:
        id_session = session.get("id_user")
        if id_session:
            print(f"USUÁRIO LOGADO, ID SESSÃO = {id_session}")
            g.id_user = id_session
        else:
            print("USUÁRIO DESLOGADO")
            g.id_user = None
    except Exception as e:
        flash("Erro para validar!")
        print(f"\nERRO AO VALIDAR: {e}")
