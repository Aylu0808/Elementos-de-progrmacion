#Ingresar 3 valores reales y:
#Si los dos primeros son mayores al tercero informar “MAYORES AL TERCERO”.
#Si los tres son iguales informar “TRES IGUALES.
#Si alguno de los dos primeros es menor al tercero informar “ALGUNO ES MENOR”

nro_1 = float(input("Ingrese el primer numero: "))
nro_2 = float(input("Ingrese el segundo numero: "))
nro_3 = float(input("Ingrese el tercer numero: "))
   
if(nro_1 == nro_2 == nro_3):
    print("Los tres numeros son iguales")

elif(nro_1 > nro_3 and nro_2 > nro_3):
    print("Los dos primeros numeros son mayores al tercero")
else:
    print("Alguno de los dos primeros numeros es menor al tercero")
