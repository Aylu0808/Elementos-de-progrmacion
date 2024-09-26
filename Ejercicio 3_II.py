"""Un laboratorio de especialidades medicinales que produce cierto jarabe tiene
dos tipos de envases Tipo ‘Á’ de 240 mililitros, y Tipo ‘B’ de 160 mililitros.
Cuyos costos unitarios de cada envase son del Tipo ‘A’ $20 y del Tipo ‘B’ es $15.
El laboratorio tiene varias líneas de producción, y de cada una de ellas se
conoce:
 Nro. línea de producción (entero positivo de 4 cifras)
 Cantidad de mililitros producidos(entero mayor que cero)
 Tipo de envase a utilizar ( ‘A’ o ‘B’)
Esta información termina con Nro. línea de producción cero.
CONTROLAR O VALIDAR TODA LA INFORMACION INGRESADA SEGÚN LOS
PARAMETROS INDICADOS
Se pide informar:
a- Por cada línea de producción: Nro. de línea, cantidad de envases
necesarios y costo total de los envases.
b- Cantidad de líneas que usaron más de 200 envases.
c- Número de la línea que uso más envases de tipo ‘B’. (suponer único)
d- Porcentajes de envases utilizados de cada tipo"""

nro_p = 0
ml = 0
envase_total = 0
envase = ""
ml_envase = 0
costo = 0
costo_total = 0
lineas = 0
maxenvase_total = 0
linea_tipoB = 0
lineas = 0
total_B = 0
total_A = 0
total_lineas = 0
total_envases = 0
porcentaje_B = 0
porcentaje_A = 0

nro_p = int(input("Ingrese el numero de linea de produccion: "))
while (1000 > nro_p or 9999 < nro_p) and nro_p != 0:
    nro_p = int(input("ERROR!! Ingrese un numero de linea correcto: "))

while nro_p != 0:

    ml = int(input("Ingrese la cantidad de mililitros: "))
    while 0 >= ml:
        ml = int(input("ERROR!! Ingrese una cantidad valida de mililitros: "))

    envase = input("Ingrese el tipo de envase: ").upper()
    while envase != 'A' and envase != 'B':
        envase = input("ERROR!! Ingrese un envase valido: ").upper()

    if envase == 'A':
        ml_envase = 240
        costo = 20

    if envase == 'B':
        ml_envase = 160
        costo = 15
    
    envase_total = ml // ml_envase
    costo_total = envase_total * costo

    print("Línea:",nro_p, "se necesitan",envase_total,"y el costo total es:",costo_total)

    if envase_total > 200:
        lineas = lineas + 1

    if envase == 'B':
        total_B = envase_total
        if envase_total > maxenvase_total:
            maxenvase_total = envase_total
            linea_tipoB = nro_p
    else:
        total_A = envase_total

    total_lineas = total_lineas + 1

    
    nro_p = int(input("Ingrese el numero de linea de produccion: "))
    while (1000 > nro_p or 9999 < nro_p) and nro_p != 0:
        nro_p = int(input("ERROR!! Ingrese un numero de linea correcto: "))

print("Cantidad de líneas que usaron más de 200 envases: ",lineas)

if total_B != 0:
    print("Número de la línea que usó más envases de tipo 'B': ",linea_tipoB)

total_envases = total_A + total_B

if total_envases > 0:

    porcentaje_A = (total_A / total_envases) * 100
    porcentaje_B = (total_B / total_envases) * 100

    print("Porcentaje de envases de tipo 'A': ",porcentaje_A)
    print("Porcentaje de envases de tipo 'B': ",porcentaje_B)
else:
    print("No se utilizaron envases.")
