class Livro:
    def __init__(self, nome, autor, genero):
        self.nome = nome
        self.autor = autor
        self.genero = genero
        self.emprestado = False

    def emprestar(self):
        self.emprestado = True

    def devolver(self):
        self.emprestado = False
