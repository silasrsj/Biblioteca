from sistema_de_biblioteca.src.model.usuario import Usuario
from sistema_de_biblioteca.src.model.livro import Livro

class Aluno(Usuario):
    def __init__(self, nome, cpf, livros_emprestados: list[Livro]):
        super().__init__(nome, cpf)
        self.__livros_emprestados = livros_emprestados

    def get_livros_emprestados(self):
        return self.__livros_emprestados

    def set_livros_emprestados(self, livros_emprestados):
        self.__livros_emprestados = livros_emprestados

    def adicionar_livro(self, livro: Livro):
        self.__livros_emprestados.append(livro)

