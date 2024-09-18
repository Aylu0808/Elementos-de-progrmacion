"""Dado un conjunto de números y dos valores A y B. 
Hallar la sumatoria de todos los números que siendo múltiplos de A, sean menores que B. 
El ingreso de números finaliza cuando se ingresa un número igual a cero.
Informar dicha sumatoria y la cantidad de números ingresados"""

A = int(input("Ingresa el valor de A: "))
B = int(input("Ingresa el valor de B: "))

sumatoria = 0
cantidad = 0


numero = int(input("Ingresa un número (o 0 para finalizar): "))

while numero != 0:

    if numero % A == 0 and numero < B:
        sumatoria = sumatoria + numero

    cantidad = cantidad + 1

    numero = int(input("Ingresa otro número: "))

print("El resultado de la sumatoria es: ",sumatoria)
print("La cantidad de números ingresados es: ",cantidad)
