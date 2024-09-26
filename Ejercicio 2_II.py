"""Se ingresan datos de los empleados de una empresa. Por cada empleado se
ingresa:
 Legajo (entero entre 1000 y 5000) CONTROLAR
 Sueldo básico (float mayor a 1000) CONTROLAR
 Antigüedad en años (mayor o igual a 0) CONTROLAR
 Sexo (‘M' o 'F') CONTROLAR
 Categoría (entero entre 1 a 5) CONTROLAR
Por cada empleado ingresado se debe calcular el sueldo final a abonar sabiendo
que:
Las Categorías 2 y 3 tienen $500 de bonificación.
La Categoría 4 tiene 10% de bonificación.
La Categoría 5 tiene 30% de bonificación.
Si la antigüedad es mayor a 10 años recibe una bonificación del 10% adicional.
Todos los datos ingresados deben ser validados. El ingreso finaliza con un legajo
igual a cero.
Informar:
a- El sueldo a abonar a cada empleado.
b- Cantidad de empleados de más de 10 años de antigüedad.
c- El mayor sueldo y el legajo del empleado que cobra dicho sueldo.
d- Cantidad de hombres y de mujeres"""

#VARIABLES

legajo = 0
sueldo = 0
mayor = 0
empleado = 0
flag = 0
antiguedad = 0
bonificacion = 0
total = 0
CANT = 0
sexo = ""
M = 0
F = 0
categoria = 0

legajo = int(input("Ingrese el numero de legajo: "))
while legajo < 1000 and legajo > 5000:
    legajo = int(input("Ingrese un numero de legajo valido: "))
    
while legajo != 0:
    
    sueldo = float(input("Ingrese el sueldo basico: "))
    while sueldo < 1000:
        sueldo = float(input("ERROR!! Ingrese un sueldo valido: "))
        
    if flag == 0:
        mayor = sueldo
        empleado = legajo
    else:
        if mayor < sueldo:
            empleado = legajo
            mayor = sueldo

    sexo = input("Ingrese el sexo del empleado: ").upper()
    while sexo != "M" and sexo != "F":
        sexo = input("ERROR!! Ingrese un sexo valido: ").upper()
        
    if sexo == "M":
        M = M +1
    else:
        F = F + 1
    
    antiguedad = int(input("Ingrese los años de antiguedad: "))
    while antiguedad < 0:
        antiguedad = int(print("ERROR!!Ingrese de nuevo los años de antiguedad: "))
            
    if antiguedad >= 10:
        bonificacion = sueldo * 0.10
        total = sueldo + bonificacion
        CANT = CANT + 1

        categoria = int(input("Ingrese la categoria del empleado: "))
        while categoria != 1 and categoria != 2 and categoria != 3 and categoria != 4 and categoria != 5:
            categoria = int(input("ERROR!! Ingrese una categoria valida: "))
            
        if categoria == 2 or categoria == 3:
            total = sueldo + 500
            print("El sueldo a abonar es: ",total)
        if categoria == 4:
            bonificacion = sueldo * 0.90
            total = bonificacion + sueldo
            print("El sueldo a abonar es: ",total)
        if categoria == 5:
            bonificacion = sueldo * 0.70
            total = bonificacion + sueldo
            print("El sueldo a abonar es: ",total)
        else:
            categoria = int(input("Ingrese la categoria del empleado: "))
        while categoria < 1 and categoria > 5:
            categoria = int(input("ERROR!! Ingrese una categoria valida: "))
            
        if categoria == 2 or categoria == 3:
            total = sueldo + 500
            print("El sueldo a abonar es: ",total)
        if categoria == 4:
            bonificacion = sueldo * 0.90
            total = bonificacion + sueldo
            print("El sueldo a abonar es: ",total)
        if categoria == 5:
            bonificacion = sueldo * 0.70
            total = bonificacion + sueldo
            print("El sueldo a abonar es: ",total)

    legajo = int(input("Ingrese el numero de legajo: "))
    while legajo < 1000 and legajo > 5000:
        legajo = int(input("Ingrese un numero de legajo valido: "))
        
print("La cantidad total de mujeres es: ",F,"y la cantidad total de hombres es: ",M)
print("El empleado con mayor sueldo es el de: ",mayor,"con un sueldo de: ",empleado)
print("La cantidad de empleados con mas de 10 años de antiguedad es: ",CANT)
