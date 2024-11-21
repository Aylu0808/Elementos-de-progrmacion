import random
import machine
import time
from vivero import Vivero
#Configuracion de los pines
# Pines para los segmentos del display de 7 segmentos
pin_A = machine.Pin(2, machine.Pin.OUT)
pin_B = machine.Pin(4, machine.Pin.OUT)
pin_C = machine.Pin(5, machine.Pin.OUT)
pin_D = machine.Pin(18, machine.Pin.OUT)
pin_E = machine.Pin(19, machine.Pin.OUT)
pin_F = machine.Pin(21, machine.Pin.OUT)
pin_G = machine.Pin(22, machine.Pin.OUT)

# Pines para los LEDs que representan los aspersores
led_1 = machine.Pin(13, machine.Pin.OUT)
led_2 = machine.Pin(12, machine.Pin.OUT)
led_3 = machine.Pin(14, machine.Pin.OUT)
led_4 = machine.Pin(27, machine.Pin.OUT)
led_5 = machine.Pin(26, machine.Pin.OUT)
led_6 = machine.Pin(25, machine.Pin.OUT)
led_7 = machine.Pin(33, machine.Pin.OUT)
led_8 = machine.Pin(32, machine.Pin.OUT)
led_9 = machine.Pin(17, machine.Pin.OUT)
#Funcion para apagar los leds
def apagar_led():
    """Apaga todos los LEDs, simulando que ningún aspersor está activo."""
    led_1.value(0)
    led_2.value(0)
    led_3.value(0)
    led_4.value(0)
    led_5.value(0)
    led_6.value(0)
    led_7.value(0)
    led_8.value(0)
    led_9.value(0)
#Control del display de 7 Segmentos
def SieteSegmentos(A, B, C, D, E, F, G):
    pin_A.value(A)
    pin_B.value(B)
    pin_C.value(C)
    pin_D.value(D)
    pin_E.value(E)
    pin_F.value(F)
    pin_G.value(G)
#Funcion Principal
def main():
    vivero = Vivero()# Crear una instancia de la clase Vivero
    print("Simulación del sistema de riego iniciada...\n") 
    hora_actual = time.localtime()# Obtener la hora actual del sistema
    alcance = random.randint(0, 255)# Generar un valor aleatorio para el alcance
    # Obtener los bits de sincronismo S1 y S2 del valor `alcance`
    s1 = (alcance >> 1) & 0b1  # Bit 1
    s2 = alcance & 0b1         # Bit 0
    # Variable para controlar el bucle principal
    x = 0
    while x == 0:
        # Si los bits de sincronismo son diferentes
        if s1 != s2:
            aspersor = random.randint(0, 255)  # Generar un valor aleatorio para el aspersor
            # Registrar medición en el vivero
            vivero.registrar_mediciones(aspersor, alcance, hora_actual[3])
            # Determinar cuál aspersor está activo y mostrarlo en el display de 7 segmentos
            if aspersor == 0b00000001:  # Aspersor 1
                SieteSegmentos(1, 0, 0, 1, 1, 1, 1)
                led_1.value(1)
                time.sleep(2)
                SieteSegmentos(1,1,1,1,1,1,1)
            elif aspersor == 0b00000010:  # Aspersor 2
                SieteSegmentos(0, 0, 1, 0, 0, 1, 0)
                led_2.value(1)
                time.sleep(2)
                SieteSegmentos(1,1,1,1,1,1,1)
            elif aspersor == 0b00000011:  # Aspersor 3
                SieteSegmentos(0, 0, 0, 0, 1, 1, 0)
                led_3.value(1)
                time.sleep(2)
                SieteSegmentos(1,1,1,1,1,1,1)
            elif aspersor == 0b00000100:  # Aspersor 4
                SieteSegmentos(1, 0, 0, 1, 1, 0, 0)
                led_4.value(1)
                time.sleep(2)
                SieteSegmentos(1,1,1,1,1,1,1)
            elif aspersor == 0b00000101:  # Aspersor 5
                SieteSegmentos(0, 1, 0, 0, 1, 0, 0)
                led_5.value(1)
                time.sleep(2)
                SieteSegmentos(1,1,1,1,1,1,1)
            elif aspersor == 0b00000110:  # Aspersor 6
                SieteSegmentos(0, 1, 0, 0, 0, 0, 0)
                led_6.value(1)
                time.sleep(2)
                SieteSegmentos(1,1,1,1,1,1,1)
            elif aspersor == 0b00000111:  # Aspersor 7
                SieteSegmentos(0, 0, 0, 1, 1, 1, 1)
                led_7.value(1)
                time.sleep(2)
                SieteSegmentos(1,1,1,1,1,1,1)
            elif aspersor == 0b00001000:
                SieteSegmentos(0,0,0,0,0,0,0)
                led_8.value(1)
                time.sleep(2)
                SieteSegmentos(1,1,1,1,1,1,1)
            # Restablecer el display a un estado inactivo
            SieteSegmentos(1, 1, 1, 1, 1, 1, 1)
            time.sleep(1)
            apagar_led()
        # Si el aspersor es igual a 0, finalizamos la simulación
            if aspersor == 0:
                print("Finalizó el proceso debido a aspersor igual a 0.")
                led_9.value(1)
                x = 1  # Salir del bucle
        else: # Si los bits de sincronismo son iguales, generar nuevos valores
            print("Sincronismo S1 igual a S2, intentando con nuevos valores.")
        # Actualizar los valores aleatorios para la siguiente iteración
        alcance = random.randint(0, 255)
        s1 = (alcance >> 1) & 0b1
        s2 = alcance & 0b1
    # Reportar los resultados después de salir del bucle
    vivero.reportar_resultados()
if __name__ == "__main__":
  main()
