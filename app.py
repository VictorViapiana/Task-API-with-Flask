from flask import Flask, jsonify, request

app = Flask(__name__)

tarefas = ["Estudar Python", "Treinar", "Ler livro"]

@app.route("/")
def home():
    return "API de Tarefas funcionando!"

# GET - listar tarefas
@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    return jsonify(tarefas)

# POST - criar tarefa
@app.route("/tarefas", methods=["POST"])
def criar_tarefa():
    dados = request.get_json()

    if not dados or "tarefa" not in dados:
        return jsonify({"erro": "Envie uma tarefa válida"}), 400

    nova_tarefa = dados.get("tarefa")
    tarefas.append(nova_tarefa)

    return jsonify({"mensagem": "Tarefa adicionada com sucesso!"})

# PUT - atualizar tarefa
@app.route("/tarefas/<int:indice>", methods=["PUT"])
def atualizar_tarefa(indice):
    if indice < 0 or indice >= len(tarefas):
        return jsonify({"erro": "Índice inválido"}), 404

    dados = request.get_json()

    if not dados or "tarefa" not in dados:
        return jsonify({"erro": "Envie uma tarefa válida"}), 400

    tarefas[indice] = dados["tarefa"]

    return jsonify({"mensagem": "Tarefa atualizada com sucesso!"})

# DELETE - deletar tarefa
@app.route("/tarefas/<int:indice>", methods=["DELETE"])
def deletar_tarefa(indice):
    if indice < 0 or indice >= len(tarefas):
        return jsonify({"erro": "Índice inválido"}), 404

    tarefas.pop(indice)

    return jsonify({"mensagem": "Tarefa removida com sucesso!"})

if __name__ == "__main__":
    app.run(debug=True)