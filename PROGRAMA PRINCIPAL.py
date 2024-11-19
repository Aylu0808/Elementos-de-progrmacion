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

def SieteSegmentos(valor): #es el valor del aspersor
    if valor == 1:
        pin_B.value(1)
        pin_A.value(1)
        pin_C.value(0)
        pin_D.value(0)
        pin_E.value(0)
        pin_F.value(0)
        pin_G.value(0)
    elif valor == 2:
        pin_A.value(1)
        pin_B.value(1)
        pin_C.value(0)
        pin_G.value(1)
        pin_E.value(1)
        pin_D.value(1)
        pin_F.value(0)
    elif valor == 3:
        pin_A.value(1)
        pin_B.value(1)
        pin_G.value(1)
        pin_C.value(1)
        pin_D.value(1)
        pin_E.value(0)
        pin_F.value(0)
    elif valor == 4:
        pin_A.value(0)
        pin_E.value(0)
        pin_D.value(0)
        pin_F.value(1)
        pin_G.value(1)
        pin_B.value(1)
        pin_C.value(1)
    elif valor == 5:
        pin_A.value(1)
        pin_B.value(0)
        pin_E.value(0)
        pin_F.value(1)
        pin_G.value(1)
        pin_C.value(1)
        pin_D.value(1)
    elif valor == 6:
        pin_A.value(1)
        pin_B.value(0)
        pin_F.value(1)
        pin_G.value(1)
        pin_C.value(1)
        pin_E.value(1)
        pin_D.value(1)
    elif valor == 7:
        pin_A.value(1)
        pin_B.value(1)
        pin_C.value(1)
        pin_D.value(0)
        pin_E.value(0)
        pin_F.value(0)
        pin_G.value(0)
    elif valor == 8:
        pin_A.value(1)
        pin_B.value(1)
        pin_C.value(1)
        pin_D.value(1)
        pin_E.value(1)
        pin_F.value(1)
        pin_G.value(1)
    elif valor == 0:
        pin_A.value(0)
        pin_B.value(0)
        pin_C.value(0)
        pin_D.value(0)
        pin_E.value(0)
        pin_F.value(0)
        pin_G.value(0)

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
        SieteSegmentos(valor)
        if s1 != s2:
            aspersor = random.randint(0, 255)
            # Registrar mediciones para cada iteración
            vivero.registrar_mediciones(aspersor, alcance, hora_actual[3])
            if aspersor == 0b00000001:
                valor = 1
                SieteSegmentos(valor)
                led_1.value(1)
            elif aspersor == 0b00000010:
                valor = 2
                SieteSegmentos(valor)
                led_1.value(1)
                led_2.value(1)
            elif aspersor == 0b00000011:
                valor = 3
                SieteSegmentos(valor)
                led_1.value(1)
                led_2.value(1)
                led_3.value(1)
            elif aspersor == 0b00000100:
                valor = 4
                SieteSegmentos(valor)
                led_1.value(1)
                led_2.value(1)
                led_3.value(1)
                led_4.value(1)
            elif aspersor == 0b00000101:
                valor = 5
                SieteSegmentos(valor)
                led_1.value(1)
                led_2.value(1)
                led_3.value(1)
                led_4.value(1)
                led_5.value(1)
            elif aspersor == 0b00000110:
                valor = 6
                SieteSegmentos(valor)
                led_1.value(1)
                led_2.value(1)
                led_3.value(1)
                led_4.value(1)
                led_5.value(1)
                led_6.value(1)
            elif aspersor == 0b00000111:
                valor = 7
                SieteSegmentos(valor)
                led_1.value(1)
                led_2.value(1)
                led_3.value(1)
                led_4.value(1)
                led_5.value(1)
                led_6.value(1)
                led_7.value(1)

            valor = 0
            SieteSegmentos(valor)
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
