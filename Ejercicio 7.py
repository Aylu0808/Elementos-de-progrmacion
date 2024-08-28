"""Ejercicio 7_Ingresar un número como y determine si es divisible por 3 y 5, por ninguno de ellos, o por ambos."""

nro = int(input("Ingrese un numero: "))

if(nro % 3 == 0 and nro % 5 == 0):
    print("El numero es divisible por 3 y por 5")
elif(nro % 3 != 0 and nro % 5 != 0):
    print("El numero  no es divisible por ninguno  de los numeros")
else:
    print("El numero es divisible por alguno  de los numeros")