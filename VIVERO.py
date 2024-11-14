class Vivero:
    def __init__(self):
        self.cant_alarmaspar = [0] * 4
        self.cant_alarmasimpar = [0] * 4
        self.medicionespar = [0] * 4
        self.medicionesimpar = [0] * 4
        self.mediciones_porhora = [0] * 24
#SETTERS
def set_medicionespar(self, indice,valor):
    if 0 <= indice < len(self.medicionespar):
        self.medicionespar[indice] = valor

def set_medicionesimpar(self,indice,valor):
    if 0 <= indice < len(self.medicionesimpar):
        self.medicionesimpar[indice] = valor

def set_cantpar(self,indice,valor):
    if 0 <= indice < len(self.cant_alarmaspar):
        self.cant_alarmaspar[indice] = valor

def set_cantimpar(self,indice,valor):
    if 0 <= indice < len(self.cant_alarmasimpar):
        self.cant_alarmasimpar[indice] = valor
#GETTERS
def get_medicionespar(self):
    return self.medicionespar

def get_medicionesimpar(self):
    return self.medicionesimpar

def get_cantpar(self):
    return self.cant_alarmaspar

def get_catimpar(self):
    return self.cant_alarmasimpar

def get_mediciones(self):
    return self.mediciones_porhora
