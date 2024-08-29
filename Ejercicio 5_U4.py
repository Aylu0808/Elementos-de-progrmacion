""" Realizar las tablas de multiplicar de los todos los números del 1 al 10.  """

RESULT = 0

for nro in range(1,11):
    for x in range(0,11):
        RESULT = x * nro
        print(nro,"x",x,":",RESULT)
    print('---------------------------------')
