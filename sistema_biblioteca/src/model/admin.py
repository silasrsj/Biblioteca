from sistema_de_biblioteca.src.model.usuario import Usuario
from sistema_de_biblioteca.src.model.aluno import Aluno
from sistema_de_biblioteca.src.model.livro import Livro
from sistema_de_biblioteca.src.utils.util import gerar_id

class Admin(Usuario):
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)

    def adicionar_livro(self, lista_livros: list[Livro]):
        titulo = input("Informe o título do livro: ")
        autor = input("Informe o autor do livro: ")
        novo_livro = Livro(titulo, autor)
        id = gerar_id(lista_livros)
        novo_livro.set_id(id)
        lista_livros.append(novo_livro)
        print(f"Livro {titulo} adicionado com sucesso!")

    def remover_livro(self, lista_livros: list[Livro]):
        id_busca = input("Informe o ID do livro que deseja remover: ")
        if id_busca.isnumeric():
            for livro in lista_livros:
                if int(id_busca) == livro.get_id():
                    lista_livros.remove(livro)
                    input(f"Livro {livro.titulo} removido com sucesso! Pressione ENTER para continuar.")
                    return
            input(f"ID {id_busca} não encontrado, pressione ENTER para continuar.")
        else:
            print("Id invalido")

    def adicionar_aluno(self, aluno: Aluno, lista_de_alunos: list[Aluno]):
        lista_de_alunos.append(aluno)

    def remover_aluno(self, aluno: Aluno, lista_de_alunos: list[Aluno]):
        lista_de_alunos.remove(aluno)

    def listar_alunos(self, lista_alunos: list[Aluno]):
        for aluno in lista_alunos:
            print(aluno.get_nome())





