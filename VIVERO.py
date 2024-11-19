class Vivero:
    def __init__(self):
        self.cont_alarmaspar = 0
        self.cont_alarmasimpar = 0
        self.cant_mediciones = [0] * 8
        self.cant_medicioneshora = [0] * 24
        self.acum_promediopar = 0
        self.acum_promedioimpar = 0
        self.cont_pares = 0  # Contador de mediciones válidas en aspersores pares
        self.cont_impares = 0

    def get_cont_alarmaspar(self):
        return self.cont_alarmaspar

    def get_cont_alarmasimpar(self):
        return self.cont_alarmasimpar

    def get_cant_mediciones(self):
        return self.cant_mediciones

    def get_cant_medicioneshora(self):
        return self.cant_medicioneshora

    def get_alcance_prompar(self):
        return self.acum_promediopar // (self.cont_pares or 1)

    def get_alcance_promimpar(self):
        return self.acum_promedioimpar // (self.cont_impares or 1)
    
    def registrar_mediciones(self, aspersor,alcance,hora):

        if aspersor <= 0b00001000 and aspersor >= 0b00000001:
            self.cant_mediciones[aspersor -1] += 1
            self.cant_medicioneshora[hora] += 1

            if (aspersor & 0b00000001) == 0:
                if alcance >= 0b00000100 and alcance <= 0b00000111:
                    self.acum_promediopar += alcance
                    self.cont_pares += 1
                else:
                    self.cont_alarmaspar += 1
                    print(f"ALARMA: Aspersor {aspersor} fuera de rango (alcance: {alcance}) a las {hora}")
            else:
                if alcance >= 0b00000110 and alcance <= 0b00001111:
                    self.acum_promedioimpar += alcance
                    self.cont_impares += 1
                else:
                    self.cont_alarmasimpar += 1
                    print(f"ALARMA: Aspersor {aspersor} fuera de rango (alcance: {alcance}) a las {hora}")
                    
    def reportar_resultados(self):
        print("Resultados:")
        print(f"Alarmas en aspersores pares: {self.cont_alarmaspar}")
        print(f"Alarmas en aspersores impares: {self.cont_alarmasimpar}")
        print(f"Mediciones por aspersor: {self.cant_mediciones}")
        print(f"Mediciones por hora: {self.cant_medicioneshora}")
        print(f"Alcance promedio de los pares: {self.get_alcance_prompar()}")
        print(f"Alcance promedio de los impares: {self.get_alcance_promimpar()}")
