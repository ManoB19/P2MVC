class Noticia:
    def __init__(self, estado, curtidas):
        self.estado = estado
        self.curtidas = curtidas

    def get_estado(self):
        return self.__estado
    
    def set_estado(self, estado):
        self.__estado = estado

    def get_curtidas(self):
        return self.__curtidas

    def set_curtidas(self, curtidas):
        self.__curtidas = curtidas
