from sistema_biblioteca.src.model.livro import Livro


class Usuario:
    def __init__(self, nome, livros_emprestados: list[Livro]):
        self.__cpf = ""
        self.__nome = nome
        self.__livros_emprestados = livros_emprestados


    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_livros_emprestados(self):
        return self.__livros_emprestados

    def set_livros_emprestados(self, livros_emprestados):
        self.__livros_emprestados = livros_emprestados

    def adicionar_livro(self, livro: Livro):
        self.__livros_emprestados.append(livro)

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, cpf):
        self.__cpf = cpf