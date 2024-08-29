"""Realizar un programa que:
a. Muestre todos los números primos entre 1 y 100. (Un nro. es primo cuando es
divisible solamente por 1 y por sí mismo)
b. Contar y mostrar la cantidad de primos encontrados. """

SUM = 0

for nro in range(1, 101):
    es_primo = True
    for x in range(2, int(nro**0.5) + 1):
        if nro % x == 0:
            es_primo = False
    if es_primo and nro> 1:
        SUM = SUM +1
        print("Numero primo: ",nro)

print("Hay",SUM,"numeros primos")
