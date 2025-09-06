class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True


    def disponibilidade(self):
        if self.disponivel == True:
            return "Disponível"
        else:
            return "Indisponível"