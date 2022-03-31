import flask
from flask import Flask, request

import funçoes_8

app = Flask("contato")

@app.route("/", methods=["GET"])
def raiz():
    return {"mensagem": "Bem vindo a nossa API"}

@app.route("/contato", methods=["POST"])
def adicionar_contato():
    contato = request.json

    if funçoes_8.cadastrar(contato.get("nome"), contato.get("email"), contato.get("fone"),contato.get("data_nasc")):
       codigo =201
    else:
        codigo = 409

    return {}, codigo


@app.route("/contato", methods=["DELETE"])
def remover_contato(email):
    codigo = 200 if funçoes_8.remover(email) else 404
    return {}, codigo



@app.route("/contato", methods = ["PATCH"])
def atualizar_contato():
    codigo = 200 if funçoes_8.atualizar(request.json.get("n_nome"), request.json.get("n_email"), request.json.get("n_tell"),request.json.get("n_data_nasc"),request.json.get("id")) else 404
    return{}, codigo




@app.route ("/contato", methods=["GET"])
def listar_contato():
    contato = funçoes_8.listar()
    codigo = 200 if contato else 404

    return flask.jsonify(contato), codigo




@app.route("/contato", methods=["GET"])
def buscar(nome):
    contato = funçoes_8.buscar(nome)
    codigo =200 if contato else 404
    return flask.jsonify(contato), codigo




def main():
    funçoes_8.criar_basedata()
    app.run(host="0.0.0.0", port=4443, debug=False)



if __name__ == "__main__":
    main()