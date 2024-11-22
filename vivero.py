class Vivero:
        # Constructor: Inicializa los atributos de la clase
    def __init__(self):
        # Contadores para alarmas de aspersores pares e impares
        self.cont_alarmaspar = 0
        self.cont_alarmasimpar = 0
        # Listas para registrar mediciones por aspersor (8 aspersores) y por hora (24 horas)
        self.cant_mediciones = [0] * 8
        self.cant_medicioneshora = [0] * 24
        # Acumuladores para los promedios de alcance de aspersores pares e impares
        self.acum_promediopar = 0
        self.acum_promedioimpar = 0
        # Contadores de mediciones válidas de aspersores pares e impares
        self.cont_pares = 0
        self.cont_impares = 0
        
#Metodo getters
    def get_cont_alarmaspar(self):
        # Retorna el número de alarmas de aspersores pares
        return self.cont_alarmaspar

    def get_cont_alarmasimpar(self):
        # Retorna el número de alarmas de aspersores impares
        return self.cont_alarmasimpar

    def get_cant_mediciones(self):
        # Retorna la lista de mediciones por aspersor
        return self.cant_mediciones

    def get_cant_medicioneshora(self):
        # Retorna la lista de mediciones por hora
        return self.cant_medicioneshora
    
    def get_acum_promediopar(self, valor):
        # Asigna un nuevo valor al acumulador de promedios para aspersores pares
        return self.acum_promediopar

    def get_acum_promedioimpar(self, valor):
        # Asigna un nuevo valor al acumulador de promedios para aspersores impares
        return self.acum_promedioimpar
#Metodo Setters  
    def set_cont_alarmaspar(self, valor):
        # Asigna un nuevo valor al contador de alarmas de aspersores pares
        self.cont_alarmaspar = valor

    def set_cont_alarmasimpar(self, valor):
        # Asigna un nuevo valor al contador de alarmas de aspersores impares
        self.cont_alarmasimpar = valor

    def set_cant_mediciones(self, indice, valor):
        # Modifica el número de mediciones de un aspersor específico
        self.cant_mediciones[indice] = valor

    def set_cant_medicioneshora(self, indice, valor):
        # Modifica el número de mediciones de una hora específica
        self.cant_medicioneshora[indice] = valor

    def set_acum_promediopar(self, valor):
        # Asigna un nuevo valor al acumulador de promedios para aspersores pares
        self.acum_promediopar = valor

    def set_acum_promedioimpar(self, valor):
        # Asigna un nuevo valor al acumulador de promedios para aspersores impares
        self.acum_promedioimpar = valor

    def set_cont_pares(self, valor):
        # Modifica el contador de mediciones válidas de aspersores pares
        self.cont_pares = valor

    def set_cont_impares(self, valor):
        # Modifica el contador de mediciones válidas de aspersores impares
        self.cont_impares = valor  
