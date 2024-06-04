class Usuario:
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.emprestimos = []

    def adicionar_emprestimo(self, emprestimo):
        self.emprestimos.append(emprestimo)

    def remover_emprestimo(self, emprestimo):
        self.emprestimos.remove(emprestimo)
