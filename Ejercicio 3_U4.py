""" Sumar los primeros N números naturales pares"""

SUM = 0

nro_1 = int(input("Cuantos numeros va a ingresar :"))

for N in range(0, nro_1):
    NRO_2 = int(input("Ingrese un numero: "))
    if(NRO_2 % 2 == 0):
        SUM = SUM + NRO_2

print("El resultado de la suma es de: ",SUM)
