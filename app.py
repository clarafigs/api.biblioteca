from flask import Flask, request, jsonify

app = Flask(__name__)

livros = []

@app.route('/api/cadastrar_livro', methods=['POST'])
def cadastrar_livro():
    dados_livro = request.json
    livros.append(dados_livro)
    return jsonify({'mensagem': 'Livro cadastrado com sucesso'}), 201

if __name__ == '__main__':
    app.run(debug=True)
