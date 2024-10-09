"""Se ingresan ternas de valores enteros. Determinar:
a-) El promedio de cada terna. FUNCION PROMEDIO
b-) El menor valor de cada terna. FUNCION MENOR.
El ingreso finaliza con una terna nula. """

#FUNCIONES
def PROMEDIO():
    prom = (a + b +c)/3
    return prom

def MENOR():
    if a < b:
        menor = a
        if menor < c:
            menor_M = menor
        else:
            menor_M = c
    else:
        menor = b
        if menor < c:
            menor_M = menor
        else:
            menor_M = c
    return menor_M

#PROGRAMA PRINCIPAL
b= 0
c = 0

a = int(input("Ingrese el primer valor de la terna: "))
if a == 0:
    print("Se ingreso una terna nula")
else:
    b = int(input("Ingrese el segundo valor de la terna: "))
    if b == 0:
        print("Se ingreso una terna nula")
    else:
        c = int(input("Ingrese el tercer valor de la terna: "))
        if c == 0:
            print("Se ingreso una terna nula")

while a != 0 or b != 0 or c != 0:

    promedio = PROMEDIO()

    menor = MENOR()

    print("El promedio es de: %.2f"%promedio)
    print("El menor numero es: ",menor)

    a = int(input("Ingrese el primer valor de la terna: "))
    if a == 0:
        print("Se ingreso una terna nula")
    else:
        b = int(input("Ingrese el segundo valor de la terna: "))
        if b == 0:
            print("Se ingreso una terna nula")
        else:
            c = int(input("Ingrese el tercer valor de la terna: "))
            if c == 0:
                print("Se ingreso una terna nula")


