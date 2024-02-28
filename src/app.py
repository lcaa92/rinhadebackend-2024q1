from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# POST /clientes/[id]/transacoes
@app.route("/clientes/<int:id>/transacoes", methods=['POST'])
def transaction(id):
    return {}, 200


# GET /clientes/[id]/extrato
@app.route("/clientes/<int:id>/extrato", methods=['GET'])
def extract(id):
    return {}, 200
