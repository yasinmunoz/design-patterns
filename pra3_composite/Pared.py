from ElementoMapa import ElementoMapa

class Pared (ElementoMapa):

    #entrar en contacto con la pared
    def entrar (self):
        print ("Te has chocado con la pared")

    # verifica si el elem_mapa es pared
    def es_pared(self):
        return True