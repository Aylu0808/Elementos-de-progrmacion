import machine
import time

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
