from Decorator import Decorator

class Bomba (Decorator):
    
    #construye la bomba
    def __init__ (self):
        self.__activada = False

    #getter y setter de la activacion
    def get_activada(self):
        return self.__activada
    def set_activada(self, activada):
        self.__activada = activada

    #activa la bomba
    def activar(self):
        __activada = True
        print("La bomba ha explotado. Estás muerto!")

    #verifica si es bomba
    def es_bomba(self):
        return True