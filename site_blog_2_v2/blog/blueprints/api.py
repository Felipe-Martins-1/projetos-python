from flask import Blueprint, render_template, redirect, url_for, flash, jsonify
from .database import User, Post, db

bp = Blueprint("api", __name__, url_prefix="/api-json")


@bp.route("/mesagem")
def message():
    return render_template("api/message.html")


@bp.route("/usuarios")
def users_api():
    try:
        users = User.query.all()
        db.session.close()
        if users:
            api = dict()
            for i in range(len(users)):
                api[i + 1] = {"nome": users[i].name}
        else:
            flash("Não há usuários!")
            return redirect(url_for("api.message"))
    except Exception as e:
        flash("Erro ao consultar!")
        print(f"\nERRO AO CONSULTAR: {e}")
        return redirect(url_for("api.message"))
    return jsonify(api)


@bp.route("/postagens")
def posts_api():
    try:
        results = (
            db.session.query(
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
        if results:
            api = dict()
            for i in range(len(results)):
                api[i + 1] = {
                    "autor": results[i].name,
                    "título": results[i].title,
                    "texto": results[i].text,
                    "criado": results[i].created_date_time,
                    "atualizado": results[i].updated_date_time,
                }
        else:
            flash("Não há postagens!")
            return redirect(url_for("api.message"))
    except Exception as e:
        flash("Erro ao consultar!")
        print(f"\nERRO AO CONSULTAR: {e}")
        return redirect(url_for("api.message"))
    return jsonify(api)
