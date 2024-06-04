import requests

def cadastrar_livro(api_url, nome, autor, genero):
    dados_livro = {
        'nome': nome,
        'autor': autor,
        'genero': genero
    }

    try:
        resposta = requests.post(api_url, json=dados_livro)
        if resposta.status_code // 100 == 2:
            print("Livro cadastrado com sucesso!")
        else:
            print(f"Erro ao cadastrar livro: {resposta.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar à API: {e}")

if __name__ == '__main__':
    api_url = 'http://127.0.0.1:5000/api/cadastrar_livro'
    nome = 'Dom Quixote'
    autor = 'Miguel de Cervantes'
    genero = 'Romance'
    cadastrar_livro(api_url, nome, autor, genero)

