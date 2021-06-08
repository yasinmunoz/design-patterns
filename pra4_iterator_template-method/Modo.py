import abc

class Modo:

    #Verifica si el bicho es perezoso
    def es_perezoso (self):
        return False

    #Verifica si el bicho es agresivo
    def es_agresivo (self):
        return False   

    #template method
    def actua (self):
        self.atacar()
        self.dormir()
        self.despertar()

    #Pone al bicho en modo dormir
    def dormir (self):
         self.dormir()

    #Despierta al bicho dormido
    def despertar (self):
        self.despertar()

    #Pone al bicho en modo atacar
    def atacar (self):
        self.atacar()