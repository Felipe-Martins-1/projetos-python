from flask import Blueprint, request, render_template
from .keys import generate
from .cryptography_rsa import encrypt, decrypt


# Classe responsável pela conexão da rota e método com o
# aplicativo Flask
bp = Blueprint("home", __name__)


# Função que retorna a renderização do arquivo html
@bp.route("/", methods=["GET", "POST"])
def index():

    # Valores iniciais das variáveis
    keys = {}
    encr_text = ""
    decr_text = ""

    if request.method == "POST":

        # Identifica cada botão
        if request.form.get("bt_encrypt"):

            # Cada variável recebe um valor digitado no formulário
            text = request.form.get("text")
            key_e = int(request.form.get("key_e"))
            key_n = int(request.form.get("key_n"))

            # Invoca o método de criptografia
            encr_text = encrypt(text, key_e, key_n)

        elif request.form.get("bt_decrypt"):

            # Cada variável recebe um valor digitado no formulário
            text = request.form.get("text")
            key_d = int(request.form.get("key_d"))
            key_n = int(request.form.get("key_n"))

            # Invoca o método de descriptografia
            decr_text = decrypt(text, key_d, key_n)

        elif request.form.get("bt_generate"):

            # Invoca o método de gerar as chaves
            keys = generate()

    return render_template(
        "home/index.html", keys=keys, encr_text=encr_text, decr_text=decr_text
    )
