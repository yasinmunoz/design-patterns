from Modo import Modo

class Agresivo (Modo):
    
    #duerme al bicho agresivo
    def dormir (self):
        print ("Bicho AGRESIVO usa DORMIR") 
        print ("ZZZ ZZZ")

    #despierta al bicho agresivo
    def despertar (self):
        print ("Bicho AGRESIVO se despertó") 

    #bicho agresivo usa ataque
    def atacar (self):
        print ("Bicho AGRESIVO atacó!")

    #bicho agresivo de mueve de habitacion
    def mover (self):
        print ("Bicho AGRESIVO entró en la habitacion")

    #Verifica si el bicho es agresivo
    def es_agresivo (self):
        print ("SOY UN BICHO AGRESIVO BRR BRR")
        return True
    
  