from ElementoMapa import ElementoMapa

class Bomba (ElementoMapa):
    
    #construye la bomba
    def __init__ (self):
        self.__activada = False

    #getter y setter de la activacion
    def get_activada(self):
        return self.__activada
    def set_activada(self, activada):
        self.__activada = activada

    #activa la bomba
    def entrar(self):
        __activada = True
        print("La bomba ha explotado.")

    #verifica si el elem_mapa es bomba
    def es_bomba(self):
        return True