from sistema_biblioteca.src.model.livro import Livro

class Biblioteca:

    def emprestar(self, livro: Livro):
        if livro.disponivel == True:
            livro.disponivel = False
            print("Livro emprestado com sucesso!")
        else:
            print("O livro não está disponível.")

    def devolver_livros(self, livro: Livro):
        if livro.disponivel:
            return "Não é possível devolver um livro que não foi emprestado."
        livro.disponivel = True
        print("Livro devolvido com sucesso!")



lista_de_livros: list[Livro] = []
