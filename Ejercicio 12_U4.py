"""Se ingresan N números distintos. Determinar los 2 números mayores."""

nro = int(input("Cuantos numeros va a ingresar: "))

mayor1 = 0
mayor2 = 0

for x in range (0,nro):
    nros = int(input("Ingrese un numero: "))
    if nros > mayor1 :
        mayor2 = mayor1
        mayor1 = nros
    elif nros > mayor2:
        mayor2 = nros

print("Los dos numeros mas grandes son",mayor1,"y",mayor2)
