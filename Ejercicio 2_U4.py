""" Se ingresan 10 números enteros. Determinar el promedio de los números positivos
ingresados."""

SUM = 0

for IDL in range(1, 11):
    nro = int(input("Ingrese un numero: "))
    SUM = SUM + nro
    
P = SUM / 10
print("El promedio es de: ", P)
    
