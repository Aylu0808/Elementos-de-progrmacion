"""En un experimento de laboratorio se toman tiempos entre reacciones, de
comienzo de la reacción (hora, minutos, segundos) y de fin de la reacción (hora,
minutos, segundos) durante el cada día. El ingreso de datos termina con el ingreso
de hora de comienzo negativa.
Determinar el tiempo entre las reacciones para cada par de valores (hora, minutos,
segundos).
Para el cálculo de dicho tiempo se sugiere usar:
a. FUNCIÓN DE CONVERTIR TIEMPO (hora, minuto, segundo) a segundos
b. FUNCIÓN RESTA
c. FUNCIÓN DIVISIÓN """

###############################FUNCIONES###############################
def TIEMPO(h,m,s):
    result = h * 3600 + m * 60 + s
    return result

def RESTA():
    resta = tiempo_f - tiempo_i
    return resta

def DIVISION(segundos):
    horas = segundos // 3600
    return horas
###############################PROGRAMA###############################

segundos = 0
segundos_r = 0
minutos = 0
segundos_f = 0

h_i = int(input("Ingrese la hora de inicio: "))
if h_i < 0:
    print("No se ingreso nada")
            
while h_i > 0:
    
    m_i = int(input("Ingrese los minutos de inicio: "))
    s_i = int(input("Ingrese los segundos de inicio: "))
        
    h_f = int(input("Ingrese la hora final: "))
    m_f = int(input("Ingrese los minutos final: "))
    s_f = int(input("Ingrese los segundos final: "))
        
    tiempo_i = TIEMPO(h_i,m_i,s_i)
    tiempo_f = TIEMPO(h_f,m_f,s_f)
        
    resta = RESTA()
        
    tiempo = DIVISION(resta)
    segundos_r = tiempo % 3600
    segundos_f =segundos_r % 60
        
    print("El tiempo entre horas: ",tiempo,segundos_r,segundos_f)
        
    h_i = int(input("Ingrese la hora de inicio: "))
