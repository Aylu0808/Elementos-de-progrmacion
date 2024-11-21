import time
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

    def get_alcance_prompar(self):
        # Calcula y retorna el promedio del alcance de aspersores pares
        # Si no hay mediciones válidas, evita la división por cero usando `(self.cont_pares or 1)`
        return self.acum_promediopar // (self.cont_pares or 1)

    def get_alcance_promimpar(self):
        # Calcula y retorna el promedio del alcance de aspersores impares
        return self.acum_promedioimpar // (self.cont_impares or 1) 
#Metodo Setters  
    def set_cont_alarmaspar(self, valor):
        # Asigna un nuevo valor al contador de alarmas de aspersores pares
        self.cont_alarmaspar = valor

    def set_cont_alarmasimpar(self, valor):
        # Asigna un nuevo valor al contador de alarmas de aspersores impares
        self.cont_alarmasimpar = valor

    def set_cant_mediciones(self, indice, valor):
        # Modifica el número de mediciones de un aspersor específico
        # `indice` debe estar entre 0 y 7 (aspirando a 8 aspersores)
        if 0 <= indice < len(self.cant_mediciones):
            self.cant_mediciones[indice] = valor

    def set_cant_medicioneshora(self, indice, valor):
        # Modifica el número de mediciones de una hora específica
        # `indice` debe estar entre 0 y 23 (24 horas)
        if 0 <= indice < len(self.cant_medicioneshora):
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
#Metodo para registrar las mediciones
    def registrar_mediciones(self, aspersor, alcance, hora):
        if 0b00000001 <= aspersor <= 0b00001000:  # Verifica que el aspersor sea válido
            self.cant_mediciones[aspersor - 1] += 1  # Incrementa el contador del aspersor
            self.cant_medicioneshora[hora] += 1  # Incrementa el contador para la hora

            if (aspersor & 0b00000001) == 0:  # Si el aspersor es par
                if 0b00000100 <= alcance <= 0b00000111:  # Alcance válido para pares
                    self.acum_promediopar += alcance  # Suma al acumulador de pares
                    self.cont_pares += 1  # Incrementa el contador de pares válidos
                else:
                    self.cont_alarmaspar += 1  # Incrementa el contador de alarmas de pares
                    print(f"ALARMA: Aspersor",aspersor,"fuera de rango (alcance:", alcance, ") a las",hora)
            else:  # Si el aspersor es impar
                if 0b00000110 <= alcance <= 0b00001111:  # Alcance válido para impares
                    self.acum_promedioimpar += alcance  # Suma al acumulador de impares
                    self.cont_impares += 1  # Incrementa el contador de impares válidos
                else:
                    self.cont_alarmasimpar += 1  # Incrementa el contador de alarmas de impares
                    print(f"ALARMA: Aspersor",aspersor,"fuera de rango (alcance:", alcance, ") a las",hora)
#Metodo para mostrar los resultados de los atributos
    def reportar_resultados(self):
        print("Resultados:")
        print(f"Alarmas en aspersores pares: {self.cont_alarmaspar}")
        print(f"Alarmas en aspersores impares: {self.cont_alarmasimpar}")
        print(f"Mediciones por aspersor: {self.cant_mediciones}")
        print(f"Mediciones por hora: {self.cant_medicioneshora}")
        print(f"Alcance promedio de los pares: {self.get_alcance_prompar()}")
        print(f"Alcance promedio de los impares: {self.get_alcance_promimpar()}")

        # Reporte de aspersores defectuosos
        print("\nAspersores defectuosos:")
        for i in range(8):
            if self.cant_mediciones[i] == 0:  # Sin mediciones
                print(f"Aspersor {i + 1}: Sin mediciones.")
            else:
                print(f"Aspersor {i + 1}: Operativo.")

import random
def main():
    vivero = Vivero()

    print("Simulacion del sistema de riego iniciada...\n") 

    hora_actual = time.localtime()
    alcance = random.randint(0, 255)
    s1 = (alcance >> 1) & 0b1          # Bit 1 (sincronismo S1)
    s2 = alcance & 0b1                 # Bit 0 (sincronismo S2)
    x = 0  # Variable para controlar la salida del bucle

    while x == 0:
        # Verificar si los sincronismos son diferentes, si no lo son, intentamos con nuevos valores
        valor = 0
        if s1 != s2:
            aspersor = random.randint(0, 255)
            # Registrar mediciones para cada iteración
            vivero.registrar_mediciones(aspersor, alcance, hora_actual[3])
            if aspersor == 0:
                    print("Finalizó el proceso debido a aspersor igual a 0.")
                    #led_8.value(1)
                    x = 1  # Cambiar x a 1 para salir del bucle
        else:
            # Si los sincronismos son iguales, generamos nuevos valores
            print("Sincronismo S1 igual a S2, intentando con nuevos valores.")
    
        alcance = random.randint(0, 255)
        s1 = (alcance >> 1) & 0b1          # Bit 1 (sincronismo S1)
        s2 = alcance & 0b1  
    vivero.reportar_resultados()  # Esta función debe ser definida

if __name__ == "__main__":
    main()
