from .database import User, db
from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
)
from ..extensions.config_login import login_manager
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint("authentication", __name__)


@bp.route("/registrar", methods=["GET", "POST"])
def register():
    try:
        if current_user.is_authenticated:
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


@login_manager.user_loader
def load_user(id):
    return User.query.get(id)


@bp.route("/entrar", methods=["GET", "POST"])
def login():
    try:
        if current_user.is_authenticated:
            return redirect(url_for("blog.my_posts"))
        else:
            if request.method == "POST":
                name_user = request.form["name_user"]
                password = request.form["password"]
                user = User.query.filter_by(name_user=name_user).first()
                if user:
                    if check_password_hash(user.password, password):
                        login_user(user)
                        print("LOGADO")
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
@login_required
def logout():
    try:
        logout_user()
        print("DESLOGADO!")
    except Exception as e:
        flash("Erro ao sair!")
        print(f"\nERRO AO SAIR: {e}")
    return redirect(url_for("blog.index"))
