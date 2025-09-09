class Livro:
    def __init__(self, titulo, autor):
        self.id = None
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True


    def disponibilidade(self):
        if self.disponivel:
            return "Disponível"
        else:
            return "Indisponível"