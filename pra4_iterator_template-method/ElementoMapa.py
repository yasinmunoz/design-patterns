import abc
class ElementoMapa:

    #comprueba si el elem_mapa es bomba
    def es_bomba (self):
        return False

    #comprueba si el elem_mapa es pared
    def es_pared (self):
        return False

    #comprueba si el elem_mapa es habitación
    def es_habitacion(self):
        return False

    #comprueba si el elem_mapa es puerta
    def es_puerta (self):
        return False

    #accede al elem_mapa
    @abc.abstractmethod
    def entrar (self):
        pass

    #iterator que recorre un elem_mapa
    def recorrer(self, un_bloque):
        un_bloque(self)