from .database import User, Post, db
from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
)
from flask_login import current_user, login_required
from time import strftime, localtime
from werkzeug.security import generate_password_hash


bp = Blueprint("blog", __name__)


@bp.route("/")
def index():
    try:
        results = (
            db.session.query(
                Post.id,
                Post.title,
                Post.text,
                Post.created_date_time,
                Post.updated_date_time,
                User.name,
            )
            .join(User)
            .filter(Post.users_id == User.id)
            .order_by(Post.id.desc())
            .all()
        )
        db.session.close()
        if results == []:
            flash("Não há postagens!")
    except Exception as e:
        flash("Erro ao consultar postagens!")
        print(f"\nERRO AO CONSULTAR POSTAGENS: {e}")
    return render_template("blog/index.html", title="Postagens", results=results)


@bp.route("/postagem/<int:id>")
def post(id: int):
    try:
        result = (
            db.session.query(
                Post.title,
                Post.text,
                Post.created_date_time,
                Post.updated_date_time,
                User.name,
            )
            .join(User)
            .filter(Post.id == id)
            .first()
        )
        db.session.close()
        if result is None:
            return redirect(url_for("blog.index"))
    except Exception as e:
        flash("Erro ao consultar postagem!")
        print(f"\nERRO AO CONSULTAR POSTAGEM: {e}")
    return render_template("blog/post.html", title="Postagem", result=result)


@bp.route("/minhas-postagens")
@login_required
def my_posts():
    try:
        posts = (
            Post.query.filter_by(users_id=current_user.id)
            .order_by(Post.id.desc())
            .all()
        )
        db.session.close()
        if posts == []:
            flash("Não há postagens!")
    except Exception as e:
        flash("Erro ao consultar postagens!")
        print(f"\nERRO AO CONSULTAR POSTAGENS: {e}")
    return render_template("blog/my_posts.html", title="Minhas Postagens", posts=posts)


@bp.route("/adicionar-postagem", methods=["GET", "POST"])
@login_required
def add_post():
    try:
        if request.method == "POST":
            title = request.form["title"]
            text = request.form["text"]
            created_date_time = strftime("%d/%m/%Y %H:%M", localtime())
            updated_date_time = "--/--/---- --:--"
            post = Post(
                title, text, created_date_time, updated_date_time, current_user.id
            )
            db.session.add(post)
            db.session.commit()
            db.session.close()
            flash("Postado!")
    except Exception as e:
        flash("Erro ao postar!")
        print(f"\nERRO AO ADICIONAR POSTAGEM: {e}")
    return redirect(url_for("blog.my_posts"))


@bp.route("/altualizar-postagem/<int:id>", methods=["GET", "POST"])
@login_required
def update_post(id: int):
    try:
        post = Post.query.get(id)
        if post:
            if post.users_id == current_user.id:
                if request.method == "POST":
                    post.title = request.form["title"]
                    post.text = request.form["text"]
                    post.updated_date_time = strftime("%d/%m/%Y %H:%M", localtime())
                    db.session.commit()
                    db.session.close()
                    flash("Atualizado!")
                    return redirect(url_for("blog.my_posts"))
            else:
                return redirect(url_for("blog.my_posts"))
        else:
            return redirect(url_for("blog.my_posts"))
    except Exception as e:
        flash("Erro ao altualizar!")
        print(f"\nERRO AO ALTUALIZAR POSTAGEM: {e}")
    return render_template("blog/update_post.html", title="Altualizar", post=post)


@bp.route("/deletar-postagem/<int:id>")
@login_required
def delete_post(id: int):
    try:
        post = Post.query.get(id)
        if post:
            if post.users_id == current_user.id:
                db.session.delete(post)
                db.session.commit()
                db.session.close()
                flash("Deletado!")
    except Exception as e:
        flash("Erro ao deletar!")
        print(f"\nERRO AO DELETAR POSTAGEM: {e}")
    return redirect(url_for("blog.my_posts"))


@bp.route("/atualizar-usuario/<int:id>", methods=["GET", "POST"])
@login_required
def update_user(id: int):
    try:
        user = User.query.get(id)
        if user:
            if user.id == current_user.id:
                if request.method == "POST":
                    user.name = request.form["name"]
                    user.password = generate_password_hash(request.form["password"])
                    db.session.commit()
                    db.session.close()
                    flash("Perfil atualizado!")
                    return redirect(url_for("blog.my_posts"))
            else:
                return redirect(url_for("blog.my_posts"))
        else:
            return redirect(url_for("blog.my_posts"))
    except Exception as e:
        flash("Erro ao altualizar!")
        print(f"\nERRO AO ALTUALIZAR POSTAGEM: {e}")
    return render_template(
        "blog/update_user.html", title="Altualizar Perfil", user=user
    )
