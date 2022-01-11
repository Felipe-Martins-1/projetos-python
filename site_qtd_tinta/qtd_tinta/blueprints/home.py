from flask import Blueprint, render_template, request
from .wall_paint_quantity import WallPaintQuantity

# Classe responsável pela conexão da rota e método com o
# aplicativo Flask
bp = Blueprint("home", __name__)

# Classe responsável pelos cálculos
wpq = WallPaintQuantity()


@bp.route("/", methods=["GET", "POST"])
def index():
    tins = {}
    if request.method == "POST":
        values = dict(request.form.to_dict())
        wpq.calculate_quantity(values)
        tins = wpq.tins
    return render_template("home/index.html", tins=tins)
