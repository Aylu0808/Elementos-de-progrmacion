import random
from time import sleep
from MODULO import Vivero
"""from machine import Pin

# Declaración de pines para el display de 7 segmentos
pin_A = Pin(0, Pin.OUT)
pin_B = Pin(1, Pin.OUT)
pin_C = Pin(2, Pin.OUT)
pin_D = Pin(3, Pin.OUT)
pin_E = Pin(4, Pin.OUT)
pin_F = Pin(5, Pin.OUT)
pin_G = Pin(6, Pin.OUT)

# Declaración de pines para los LEDs (uno por cada aspersor)
led_1 = Pin(18, Pin.OUT)
led_2 = Pin(19, Pin.OUT)
led_3 = Pin(20, Pin.OUT)
led_4 = Pin(21, Pin.OUT)
led_5 = Pin(22, Pin.OUT)
led_6 = Pin(23, Pin.OUT)
led_7 = Pin(24, Pin.OUT)
led_8 = Pin(25, Pin.OUT)

def encender_led(indice):
    if indice == 1:
        led_1.value(1)
    elif indice == 2:
        led_2.value(1)
    elif indice == 3:
        led_3.value(1)
    elif indice == 4:
        led_4.value(1)
    elif indice == 5:
        led_5.value(1)
    elif indice == 6:
        led_6.value(1)
    elif indice == 7:
        led_7.value(1)
    elif indice == 8:
        led_8.value(1)

def apagar_led(indice):
    if indice == 1:
        led_1.value(0)
    elif indice == 2:
        led_2.value(0)
    elif indice == 3:
        led_3.value(0)
    elif indice == 4:
        led_4.value(0)
    elif indice == 5:
        led_5.value(0)
    elif indice == 6:
        led_6.value(0)
    elif indice == 7:
        led_7.value(0)
    elif indice == 8:
        led_8.value(0)

def SieteSegmentos(valor): #es el valor del aspersor
    if valor == 1:
        pin_B.value(1)
        pin_A.value(1)
    elif valor == 2:
        pin_A.value(1)
        pin_B.value(1)
        pin_G.value(1)
        pin_E.value(1)
        pin_D.value(1)
    elif valor == 3:
        pin_A.value(1)
        pin_B.value(1)
        pin_G.value(1)
        pin_C.value(1)
        pin_D.value(1)
    elif valor == 4:
        pin_F.value(1)
        pin_G.value(1)
        pin_B.value(1)
        pin_C.value(1)
    elif valor == 5:
        pin_A.value(1)
        pin_F.value(1)
        pin_G.value(1)
        pin_C.value(1)
        pin_D.value(1)
    elif valor == 6:
        pin_A.value(1)
        pin_F.value(1)
        pin_G.value(1)
        pin_C.value(1)
        pin_E.value(1)
        pin_D.value(1)
    elif valor == 7:
        pin_A.value(1)
        pin_B.value(1)
        pin_C.value(1)
    elif valor == 8:
        pin_A.value(1)
        pin_B.value(1)
        pin_C.value(1)
        pin_D.value(1)
        pin_E.value(1)
        pin_F.value(1)
        pin_G.value(1)"""
        
def main():
    vivero = Vivero()

    aspersor = random.randint(0,255)
    alcance = random.randint(0,255)
    
            
            """if aspersor % 2 == 0: #Si el aspersor es par 
                vivero.set_medicionespar(indice,alcance)
                if alcance < 4 or alcance > 7: #Si esta fuera del rando determinado
                    vivero.set_cantpar(indice,vivero.get_cantpar()[indice] + 1)
                else: #Si es impar
                    vivero.set_medicionesimpar(indice,alcance)
                    if alcance < 6 or alcance > 15: #si esta fuera del rango determinado
                        vivero.set_cantimpar(indice,vivero.getimpar()[indice] + 1)"""
        
        encender_led(aspersor)
        sleep(0.5)
        apagar_led(aspersor)
        sleep(0.5)

    print("Resultados finales:")
    print("Mediciones de aspersores pares:", vivero.get_medicionespar())
    print("Alarmas de aspersores pares:", vivero.get_cantpar())
    print("Mediciones de aspersores impares:", vivero.get_medicionesimpar())
    print("Alarmas de aspersores impares:", vivero.get_cantimpar())

if __name__ == "__main__":
    main()
