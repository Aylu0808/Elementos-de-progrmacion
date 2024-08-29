""" Se ingresa un Nro. y se informa la tabla de multiplicar del 1 al 10. """

RESULT = 0

nro = int(input("Ingrese un numero: "))

for x in range(0,11):
    RESULT = x * nro
    print("2 x",x,":",RESULT)
