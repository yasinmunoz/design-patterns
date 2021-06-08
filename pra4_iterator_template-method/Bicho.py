class Bicho:
    
    #Construye el bicho
    def __init__ (self):                
        #El modo es null por defecto
        self.modo = None
        self.localizacion = None 

    #get y set de modo
    def get_modo (self):
        return self.modo    
    def set_modo (self, modo):
        self.modo = modo 

    #get y set de localizacion
    def get_localizacion (self):
        return self.localizacion 
    def set_localizacion (self, localizacion):
        self.localizacion = localizacion
    