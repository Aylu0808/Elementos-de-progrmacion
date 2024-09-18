""""Cargar por teclado n números enteros positivos, uno a uno. Se deberá establecer
qué número es el mayor de los números pares y el menor de los números impares.
Por ejemplo, en una secuencia de números: 8, 15, 9, 2, 27, 18, 0; el mayor de los
pares sería el número 18 y el menor de los impares el número 9. Usar while"""

mayor_par = 0
menor_impar = 0

numero = 0

while numero = 0:

    n = int(input("Ingrese un numero: "))

    if n < 0:
        numero = -1

    if n % 2 == 0:
        if mayor_par == 0 or n > mayor_par:
            mayor_par = n
        else:
        if menor_impar == 0 or n < menor_impar:
            menor_impar = n

print("El mayor par es: ",mayor_par)
print("El menor impar es: ",menor_impar)
