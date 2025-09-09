class Livro:
    def __init__(self, id, titulo, autor):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True


    def disponibilidade(self):
        if self.disponivel:
            return "Disponível"
        else:
            return "Indisponível"