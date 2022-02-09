from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    g,
)
from time import strftime, localtime
from .database import User, Post, db

bp = Blueprint("blog", __name__)


@bp.route("/")
def index():
    try:
        results = (
            db.session.query(
                Post.id_post,
                Post.title,
                Post.text,
                Post.created_date_time,
                Post.updated_date_time,
                User.name,
            )
            .join(User)
            .filter(Post.users_id_user == User.id_user)
            .order_by(Post.id_post.desc())
            .all()
        )
        db.session.close()
        if results == []:
            flash("Não há postagens!")
    except Exception as e:
        flash("Erro ao consultar postagens!")
        print(f"\nERRO AO CONSULTAR POSTAGENS: {e}")
    return render_template("blog/index.html", title="Postagens", results=results)


@bp.route("/minhas-postagens")
def my_posts():
    try:
        if g.id_user:
            user = User.query.get(g.id_user)
            posts = (
                Post.query.filter_by(users_id_user=g.id_user)
                .order_by(Post.id_post.desc())
                .all()
            )
            db.session.close()
            if posts == []:
                flash("Não há postagens!")
        else:
            return redirect(url_for("authentication.login"))
    except Exception as e:
        flash("Erro ao consultar postagens!")
        print(f"\nERRO AO CONSULTAR POSTAGENS: {e}")
    return render_template(
        "blog/my_posts.html", title="Minhas Postagens", user=user, posts=posts
    )


@bp.route("/adicionar-postagem", methods=["GET", "POST"])
def add_post():
    try:
        if g.id_user:
            if request.method == "POST":
                title = request.form["title"]
                text = request.form["text"]
                created_date_time = strftime("%d/%m/%Y %H:%M", localtime())
                updated_date_time = "--/--/-- --:--"
                post = Post(
                    title, text, created_date_time, updated_date_time, g.id_user
                )
                db.session.add(post)
                db.session.commit()
                db.session.close()
                flash("Postado!")
        else:
            return redirect(url_for("authentication.login"))
    except Exception as e:
        flash("Erro ao postar!")
        print(f"\nERRO AO ADICIONAR POSTAGEM: {e}")
    return redirect(url_for("blog.my_posts"))


@bp.route("/altualizar-postagem/<int:id>", methods=["GET", "POST"])
def update_post(id: int):
    try:
        post = Post.query.get(id)
        if post:
            if post.users_id_user == g.id_user:
                if request.method == "POST":
                    post.title = request.form["title"]
                    post.text = request.form["text"]
                    post.updated_date_time = strftime("%d/%m/%Y %H:%M", localtime())
                    db.session.commit()
                    db.session.close()
                    flash("Atualizado!")
                    return redirect(url_for("blog.my_posts"))
            else:
                return redirect(url_for("authentication.login"))
        else:
            return redirect(url_for("authentication.login"))
    except Exception as e:
        flash("Erro ao altualizar!")
        print(f"\nERRO AO ALTUALIZAR POSTAGEM: {e}")
    return render_template("blog/update_post.html", title="Altualizar", post=post)


@bp.route("/deletar-postagem/<int:id>")
def delete_post(id: int):
    try:
        post = Post.query.get(id)
        if post:
            if post.users_id_user == g.id_user:
                db.session.delete(post)
                db.session.commit()
                db.session.close()
                flash("Deletado!")
            else:
                return redirect(url_for("authentication.login"))
        else:
            return redirect(url_for("authentication.login"))
    except Exception as e:
        flash("Erro ao deletar!")
        print(f"\nERRO AO DELETAR POSTAGEM: {e}")
    return redirect(url_for("blog.my_posts"))


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
            .filter(Post.id_post == id)
            .first()
        )
        db.session.close()
        if result is None:
            return redirect(url_for("blog.index"))
    except Exception as e:
        flash("Erro ao consultar postagem!")
        print(f"\nERRO AO CONSULTAR POSTAGEM: {e}")
    return render_template("blog/post.html", title="Postagem", result=result)
