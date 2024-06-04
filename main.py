from emprestimo import Emprestimo
from funcionario import Funcionario
from usuario import Usuario
from livro import Livro
from cadastro_api import cadastrar_livro


usuario1 = Usuario("João", "123456789", "999999999")
usuario2 = Usuario("Maria", "987654321", "888888888")
usuario3 = Usuario("Pedro", "111222333", "777777777")

livro1 = Livro("Dom Quixote", "Miguel de Cervantes", "Romance")
livro2 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", "Infantil")
livro3 = Livro("A Arte da Guerra", "Sun Tzu", "Estratégia")

funcionario = Funcionario("Carlos", "999888777", "666666666")

funcionario.fazer_emprestimo(usuario1, livro1, "2024-05-21", "2024-06-21")
funcionario.fazer_emprestimo(usuario2, livro2, "2024-05-21", "2024-06-21")
funcionario.fazer_emprestimo(usuario3, livro3, "2024-05-21", "2024-06-21")

funcionario.devolucao(usuario1, livro1)
funcionario.devolucao(usuario2, livro2)
funcionario.devolucao(usuario3, livro3)

api_url = 'http://127.0.0.1:5000/api/cadastrar_livro'
nome = 'Dom Quixote'
autor = 'Miguel de Cervantes'
genero = 'Romance'

cadastrar_livro(api_url, nome, autor, genero)


