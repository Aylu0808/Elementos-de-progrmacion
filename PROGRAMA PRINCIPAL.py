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

        print("\nAspersores defectuosos:")
                for i in range(8):
                    if self.cant_mediciones[i] == 0:
                        print(f"Aspersor {i + 1}: Sin mediciones.")
                    elif (self.cant_mediciones[i] > 0 and 
                          self.acum_promediopar == 0 and 
                          self.acum_promedioimpar == 0):  # Sin alcance válido
                        print(f"Aspersor {i + 1}: Todas las mediciones tuvieron alcance cero.")
import time
import random
import machine

pin_A = machine.Pin(2, machine.Pin.OUT)
pin_B = machine.Pin(4, machine.Pin.OUT)
pin_C = machine.Pin(5, machine.Pin.OUT)
pin_D = machine.Pin(18, machine.Pin.OUT)
pin_E = machine.Pin(19, machine.Pin.OUT)
pin_F = machine.Pin(21, machine.Pin.OUT)
pin_G = machine.Pin(22, machine.Pin.OUT)

# Declaración de pines para los LEDs (uno por cada aspersor)
led_1 = machine.Pin(13, machine.Pin.OUT)
led_2 = machine.Pin(12, machine.Pin.OUT)
led_3 = machine.Pin(14, machine.Pin.OUT)
led_4 = machine.Pin(27, machine.Pin.OUT)
led_5 = machine.Pin(26, machine.Pin.OUT)
led_6 = machine.Pin(25, machine.Pin.OUT)
led_7 = machine.Pin(33, machine.Pin.OUT)
led_8 = machine.Pin(32, machine.Pin.OUT)

def apagar_led():
    led_1.value(0)
    led_2.value(0)
    led_3.value(0)
    led_4.value(0)
    led_5.value(0)
    led_6.value(0)
    led_7.value(0)
    led_8.value(0)

def SieteSegmentos(A,B,C,D,E,F,G): #es el valor del aspersor
    pin_A.value(A)
    pin_B.value(B)
    pin_C.value(C)
    pin_D.value(D)
    pin_E.value(E)
    pin_F.value(F)
    pin_G.value(G)

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
            if aspersor == 0b00000001:
                valor = 1
                SieteSegmentos(1,0,0,1,1,1,1)
                led_1.value(1)
                time.sleep(3)
                SieteSegmentos(1,1,1,1,1,1,1)
            elif aspersor == 0b00000010:
                valor = 2
                SieteSegmentos(0,0,1,0,0,1,0)
                led_1.value(1)
                led_2.value(1)
                time.sleep(3)
                SieteSegmentos(1,1,1,1,1,1,1)
            elif aspersor == 0b00000011:
                valor = 3
                SieteSegmentos(0,0,0,0,1,1,0)
                led_1.value(1)
                led_2.value(1)
                led_3.value(1)
                time.sleep(3)
                SieteSegmentos(1,1,1,1,1,1,1)
            elif aspersor == 0b00000100:
                valor = 4
                SieteSegmentos(1,0,0,1,1,0,0)
                led_1.value(1)
                led_2.value(1)
                led_3.value(1)
                led_4.value(1)
                time.sleep(3)
                SieteSegmentos(1,1,1,1,1,1,1)
            elif aspersor == 0b00000101:
                valor = 5
                SieteSegmentos(0,1,0,0,1,0,0)
                led_1.value(1)
                led_2.value(1)
                led_3.value(1)
                led_4.value(1)
                led_5.value(1)
                time.sleep(3)
                SieteSegmentos(1,1,1,1,1,1,1)
            elif aspersor == 0b00000110:
                valor = 6
                SieteSegmentos(0,1,0,0,0,0,0)
                led_1.value(1)
                led_2.value(1)
                led_3.value(1)
                led_4.value(1)
                led_5.value(1)
                led_6.value(1)
                time.sleep(3)
                SieteSegmentos(1,1,1,1,1,1,1)
            elif aspersor == 0b00000111:
                valor = 7
                SieteSegmentos(0,0,0,1,1,1,1)
                led_1.value(1)
                led_2.value(1)
                led_3.value(1)
                led_4.value(1)
                led_5.value(1)
                led_6.value(1)
                led_7.value(1)
                time.sleep(3)
                SieteSegmentos(1,1,1,1,1,1,1)

            valor = 0
            SieteSegmentos(1,1,1,1,1,1,1)
            time.sleep(1)
            apagar_led()
            # Verificar si aspersor es igual a 0, entonces finalizar el proceso
            if aspersor == 0:
                print("Finalizó el proceso debido a aspersor igual a 0.")
                led_8.value(1)
                x = 1  # Cambiar x a 1 para salir del bucle
        else:
            # Si los sincronismos son iguales, generamos nuevos valores
            print("Sincronismo S1 igual a S2, intentando con nuevos valores.")
    
        alcance = random.randint(0, 255)
        s1 = (alcance >> 1) & 0b1          # Bit 1 (sincronismo S1)
        s2 = alcance & 0b1                 # Bit 0 (sincronismo S2)
    
    # Llamar a la función después de que se salga del bucle
    vivero.reportar_resultados()  # Esta función debe ser definida

if __name__ == "__main__":
    main()
