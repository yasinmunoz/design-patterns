from Modo import Modo

class Perezoso (Modo):
    
    #duerme al bicho perezoso
    def dormir (self):
        print ("Bicho PEREZOSO usa DORMIR") 
        print ("ZZZ ZZZ")

    #despierta al bicho perezoso
    def despertar (self):
        print ("Bicho PEREZOSO se despertó") 

    #ataque del bicho perezoso
    def atacar (self):
        print ("Bicho PEREZOSO atacó!")

    #bicho perezoso se mueve de habitación
    def mover (self):
        print ("Bicho PEREZOSO entró en la habitacion y no parece que vaya a moverse de ahi...")

    #Verifica si el bicho es perezoso
    def es_perezoso (self):
        print ("SOY UN BICHO DORMILON ZZZ ZZZ")
        return True

   