"""Confeccionar un programa que solicite el ingreso de un valor entero N < 12 y luego
una lista de N números reales sobre la cual debe calcular:
a. el promedio de los positivos.
b. el promedio de los negativos.
c. la cantidad de ceros.
Si el valor ingresado N es mayor que 12 informar 'VALOR EXCEDIDO” y si es menor
o igual a 0 informar “CANTIDAD INVALIDA”. """


nro_1 = int(input("Ingrese un numero entero menor a 12: "))

positivos = 0
negativos = 0
cantidad = 0
cantidad_n = 0
ceros = 0
P_P = 0
P_N = 0

if(0 < nro_1 < 12):
    for x in range(0,nro_1):
        lista = int(input("Ingrese un numero: "))
        if(lista > 0):
            positivos = positivos + lista
            cantidad = cantidad + 1
            P_P = positivos/cantidad
            P_P = round(P_P,2)
        else:
            negativos = negativos + lista
            cantidad_n = cantidad_n + 1
            P_N = negativos / cantidad_n
            P_N = round(P_N,2)
        if(lista == 0):
            ceros = ceros + 1

elif(nro_1 > 12):
    print("VALOR EXCEDIDO")
else:
    print("CANTIDAD INVALIDA")

print("El promedio de los positivos es de: ",P_P)
print("El promedio de los negativos es de: ",P_N)
