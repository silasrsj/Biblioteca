class Livro:
    def __init__(self, titulo, autor):
        self.__id = None
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def disponibilidade(self):
        if self.disponivel:
            return "Disponível"
        else:
            return "Indisponível"