from sistema_biblioteca.src.model.usuario import Usuario
from sistema_biblioteca.src.model.aluno import Aluno
from sistema_biblioteca.src.model.livro import Livro
from sistema_biblioteca.src.utils.util import gerar_id

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
        print(f"Livro [{titulo}] adicionado com sucesso!")

    def remover_livro(self, lista_de_alunos: list[Aluno], lista_livros: list[Livro]):
        if not lista_livros:
            input("Lista de livros vazia, pressione ENTER para continuar.")
        else:
            id_busca = input("Informe o ID do livro que deseja remover: ")
            if id_busca.isnumeric():
                for livro in lista_livros:
                    if int(id_busca) == livro.get_id():
                        if livro.disponivel:
                            lista_livros.remove(livro)
                            input(f"Livro [{livro.titulo}] removido com sucesso! Pressione ENTER para continuar.")
                            return
                        else:
                            encontrou = False
                            for aluno in lista_de_alunos:
                                for livro_emprestado in aluno.get_livros_emprestados():
                                   if livro ==  livro_emprestado:
                                       encontrou = True
                                       input(f"Não é possível remover este livro pois ele se encontra emprestado no momento com o aluno {aluno.get_nome()}, precione ENTER para continuar.")
                if not encontrou:
                    input(f"ID {id_busca} não encontrado, pressione ENTER para continuar.")
            else:
                print("ID inválido")

    def adicionar_aluno(self,):
        pass

    def remover_aluno(self, lista_de_alunos: list[Aluno]):
        if not lista_de_alunos:
            input("Lista de aluno(s) vazia, pressione ENTER para continuar.")
        else:
            cpf_busca = input("informe o CPF do aluno que deseja remover: ")
            if cpf_busca.isnumeric():
                for aluno in lista_de_alunos:
                    if cpf_busca == aluno.get_cpf():
                        if not aluno.get_livros_emprestados():
                            lista_de_alunos.remove(aluno)
                            input(f"Aluno [{aluno.get_nome()}] removido com sucesso! Pressione ENTER para continuar.")
                            return
                        else:
                            input(f"Não é possível remover o aluno [{aluno.get_nome()}], pois há pendêndia de livro(s) a devolver, precione ENTER para continuar")
                            return
                input(f"Nenhum CPF {cpf_busca} encontrado, pressione ENTER para continuar.")
            else:
                input(" CPF inválido, pressione ENTER para continuar.")

    def listar_alunos(self, lista_alunos: list[Aluno]):
        if not lista_alunos:
            input("Lista de aluno(s) vazia, pressione ENTER para continuar.")
        else:
            print("|-----------------------------------------|")
            print(f"| {'CPF':<11} | {'NOME':<25} |" )
            print("|-----------------------------------------|")
            for aluno in lista_alunos:
                print(f"| {aluno.get_cpf():<11} | {aluno.get_nome():<25} | ")
                print("|-----------------------------------------|")







