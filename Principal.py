import random
import machine
import time
from vivero import Vivero
import pines as pin
                
def main():
    
    vivero = Vivero()# Crear una instancia de la clase Vivero
    
    print("Simulación del sistema de riego iniciada...\n")
    
    hora_actual = time.localtime()# Obtener la hora actual del sistema
    
    alcance = random.randint(0, 255)# Generar un valor aleatorio para el alcance
    
    # Obtener los bits de sincronismo S1 y S2 del valor `alcance`
    s1 = (alcance >> 1) & 0b1  # Bit 1
    s2 = alcance & 0b1         # Bit 0
    
    x = 0 # Variable para controlar el bucle principal
    while x == 0:
        
        if s1 != s2: # Si los bits de sincronismo son diferentes
            aspersor = random.randint(0, 255)  # Generar un valor aleatorio para el aspersor
            
            # Registrar medición en el vivero
            if 0b00000001 <= aspersor <= 0b00001000:  # Verifica que el aspersor sea válido
                vivero.cant_mediciones[aspersor - 1] += 1  # Incrementa el contador del aspersor
                vivero.cant_medicioneshora[hora_actual[3] - 1] += 1  # Incrementa el contador para la hora

                if (aspersor & 0b00000001) == 0:  # Si el aspersor es par
                    if 0b00000100 <= alcance <= 0b00000111:  # Alcance válido para pares
                        vivero.acum_promediopar += alcance  # Suma al acumulador de pares
                        vivero.cont_pares += 1  # Incrementa el contador de pares válidos
                    else:
                        vivero.cont_alarmaspar += 1  # Incrementa el contador de alarmas de pares
                        print(f"ALARMA: Aspersor",aspersor,"fuera de rango (alcance:", alcance, ") a las",hora_actual[3])
                else:  # Si el aspersor es impar
                    if 0b00000110 <= alcance <= 0b00001111:  # Alcance válido para impares
                        vivero.acum_promedioimpar += alcance  # Suma al acumulador de impares
                        vivero.cont_impares += 1  # Incrementa el contador de impares válidos
                    else:
                        vivero.cont_alarmasimpar += 1  # Incrementa el contador de alarmas de impares
                        print(f"ALARMA: Aspersor",aspersor,"fuera de rango (alcance:", alcance, ") a las",hora_actual[3])
                    
            # Determinar cuál aspersor está activo y mostrarlo en el display de 7 segmentos
            if aspersor == 0b00000001:  # Aspersor 1
                pin.SieteSegmentos(1, 0, 0, 1, 1, 1, 1)
                pin.led_1.value(1)
                time.sleep(2)
                pin.SieteSegmentos(1,1,1,1,1,1,1)
            elif aspersor == 0b00000010:  # Aspersor 2
                pin.SieteSegmentos(0, 0, 1, 0, 0, 1, 0)
                pin.led_2.value(1)
                time.sleep(2)
                pin.SieteSegmentos(1,1,1,1,1,1,1)
            elif aspersor == 0b00000011:  # Aspersor 3
                pin.SieteSegmentos(0, 0, 0, 0, 1, 1, 0)
                pin.led_3.value(1)
                time.sleep(2)
                pin.SieteSegmentos(1,1,1,1,1,1,1)
            elif aspersor == 0b00000100:  # Aspersor 4
                pin.SieteSegmentos(1, 0, 0, 1, 1, 0, 0)
                pin.led_4.value(1)
                time.sleep(2)
                pin.SieteSegmentos(1,1,1,1,1,1,1)
            elif aspersor == 0b00000101:  # Aspersor 5
                pin.SieteSegmentos(0, 1, 0, 0, 1, 0, 0)
                pin.led_5.value(1)
                time.sleep(2)
                pin.SieteSegmentos(1,1,1,1,1,1,1)
            elif aspersor == 0b00000110:  # Aspersor 6
                pin.SieteSegmentos(0, 1, 0, 0, 0, 0, 0)
                pin.led_6.value(1)
                time.sleep(2)
                pin.SieteSegmentos(1,1,1,1,1,1,1)
            elif aspersor == 0b00000111:  # Aspersor 7
                pin.SieteSegmentos(0, 0, 0, 1, 1, 1, 1)
                pin.led_7.value(1)
                time.sleep(2)
                pin.SieteSegmentos(1,1,1,1,1,1,1)
            elif aspersor == 0b00001000: # Aspersor 8
                pin.SieteSegmentos(0,0,0,0,0,0,0)
                pin.led_8.value(1)
                time.sleep(2)
                pin.SieteSegmentos(1,1,1,1,1,1,1)
                
            # Restablecer el display a un estado inactivo
            pin.SieteSegmentos(1,1,1,1,1,1,1)
            time.sleep(4)
            pin.apagar_led()
            
        # Si el aspersor es igual a 0, finalizamos la simulación
            if aspersor == 0:
                print("Finalizó el proceso debido a aspersor igual a 0.")
                pin.led_9.value(1)
                x = 1  # Salir del bucle
        else: # Si los bits de sincronismo son iguales, generar nuevos valores
            time.sleep(2)
            print("Sincronismo S1 igual a S2, intentando con nuevos valores.")
            
        # Actualizar los valores aleatorios para la siguiente iteración
        alcance = random.randint(0, 255)
        s1 = (alcance >> 1) & 0b1
        s2 = alcance & 0b1
        
    promedio_par = vivero.acum_promediopar / (vivero.cont_pares or 1)
    promedio_impar = vivero.acum_promedioimpar / (vivero.cont_impares or 1)
        
    print("Resultados:")
    print(f"Alarmas en aspersores pares:",vivero.cont_alarmaspar)
    print(f"Alarmas en aspersores impares:",vivero.cont_alarmasimpar)
    print(f"Mediciones por aspersor:",vivero.cant_mediciones)
    print(f"Mediciones por hora:",vivero.cant_medicioneshora)
    print(f"Alcance promedio de los pares:",promedio_par)
    print(f"Alcance promedio de los impares:",promedio_impar)
    
    # Reporte de aspersores defectuosos
    print("\nAspersores defectuosos:")
    for i in range(8):
        if vivero.cant_mediciones[i] == 0:  # Sin mediciones
            print(f"Aspersor {i + 1}: Sin mediciones o con medciones igual a cero")

    
if __name__ == "__main__":
    main()
