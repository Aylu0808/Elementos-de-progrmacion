class Vivero:
    def __init__(self): #ATRIBUTOS
        self.cont_alarmaspar = 0
        self.cont_alarmasimpar = 0
        self.cant_mediciones = [0] * 8
        self.caNt_medicioneshora = [0] * 24
        self.acum_promediopar = 0
        self.acum_promedioimpar = 0
        self.alcance_prompar = 0 #No tiene set porque no lo envian es un calculo
        self.alcance_promimpar = 0
 #SETTERS       
    def set_cantalarmaspar(self):
        self.cont_alarmaspar + = 1
        
    def set_cantalarmasimpar(self):
        self.cont_alarmasimpar += 1
        
    def set_mediciones(self,POS): #PASA VALORES DEL MAIN.
        self.cant_medicione[POS] += 1
        
    def set_medicionesporhora(self,POS):
        self.cant_medicioneshora[POS] += 1
    
    def set_acumpar(self,valor):
        self.acum_promediopar += valor
        
    def set_acumimpar(self,valor):
        self.acum_promedioimpar += valor
#GETTERS
    def get_mediciones(self,POS):
        return self.mediciones[POS]

    def get_cantalarmaspar(self):
        return self.cantalarmaspar
            
    def get_cantalarmasimpar(self):
        return self.contalarmasimpar
            
    def set_medicionesporhora(self):
        return self.cant_medicioneshora[POS]
#PROMEDIO
    def get_acumpar(self):
        return self.acum_promediopar // self.cant_alarmaspar
            
    def get_acumimpar(self):
        return self.acum_promedioimpar // self.cant_alarmasimpar

        

