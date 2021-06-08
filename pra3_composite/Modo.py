import abc

class Modo:

    #Verifica si el bicho es perezoso
    def es_perezoso (self):
        return False

    #Verifica si el bicho es agresivo
    def es_agresivo (self):
        return False

    #Pone al bicho en modo dormir
    @abc.abstractmethod
    def dormir (self):
        pass 

    #Despierta al bicho dormido
    @abc.abstractmethod
    def despertar (self):
        pass 

    #Pone al bicho en modo atacar
    @abc.abstractmethod
    def atacar (self):
        pass