from emprestimo import Emprestimo
class Funcionario:
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

    def pesquisar_livro(self, livro, lista_livros):
        for l in lista_livros:
            if l.nome == livro:
                return l
        return None

    def fazer_emprestimo(self, usuario, livro, data_emprestimo, data_devolucao):
        if not livro.emprestado:
            emprestimo = Emprestimo(usuario, livro, data_emprestimo, data_devolucao)
            usuario.adicionar_emprestimo(emprestimo)
            livro.emprestar()
            print("Empréstimo realizado com sucesso!")
        else:
            print("O livro já está emprestado.")

    def devolucao(self, usuario, livro):
        for emprestimo in usuario.emprestimos:
            if emprestimo.livro == livro:
                usuario.remover_emprestimo(emprestimo)
                livro.devolver()
                print("Devolução realizada com sucesso!")
                return
        print("O usuário não possui este livro emprestado.")
