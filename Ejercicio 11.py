"""Cargar por teclado N números enteros positivos, uno a uno. Se deberá
establecer qué número es el mayor de los números pares y el menor de los
números impares. Por ejemplo, en una secuencia de números: 8, 15, 9, 2, 27, 18, 0;
el mayor de los pares sería el número 18 y el menor de los impares el número 9. """

N = int(input("¿Cuántos números desea ingresar? "))

mayor_par = 0  
menor_impar = 1000000  

pares = False
impares = False

for x in range(0,N):
    numero = int(input("Ingresa un número entero positivo: "))
    if numero % 2 == 0:
        pares = True
        if numero > mayor_par:
            mayor_par = numero
    else: 
        impares = True
        if numero < menor_impar:
            menor_impar = numero

if pares:
    print("El mayor de los números pares es: ",mayor_par)
else:
    print("No hay numeros pares")

if impares:
    print("El menor de los números impares es: ",menor_impar)
else:
    print("No hay numeros impares")
