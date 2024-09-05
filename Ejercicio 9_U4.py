"""Se ingresa N y N números naturales. Determinar:
a-) La cantidad de valores múltiplos de 3.
b-) La suma de los valores que se ingresaron en orden par.
c-) El promedio de los números múltiplos de 5 pero no múltiplos de 3"""

N = int(input("Cuantos numeros va a ingresar?: "))

multiplos = 0
pares = 0
SUM = 0
cant = 0
P = 0

for x in range(0,N):
    
    numeros = int(input("Ingrese el numero: "))
    
    if(numeros % 3 == 0 and numeros % 5 != 0):
        multiplos = multiplos + 1
    if(numeros % 2 == 0):
        pares = pares + numeros
    if(numeros % 5 == 0 and numeros % 3 != 0):
        cant = cant + 1
        SUM = SUM + numeros
        P = SUM / cant
        
print("La cantidad de multiplos de 3 es de: ",multiplos)
print("La suma de los numeros pares es de: ", pares)
print("El promnedio de los multiplos de 5 es de: ", P)
