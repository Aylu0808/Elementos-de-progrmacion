"""Se ingresan números hasta uno negativo. Hallar el promedio de los números
múltiplos de 5 y de 3 pero no de 100. """

nro1 = 0
mul5 = 0
mul3 = 0
cinco = 0
tres = 0
P_5 = 0
P_3 = 0

while(nro1 >= 0):
    
    nro1 = int(input("Ingrese un numero: "))
    
    if(nro1 % 5 == 0):
        mul5 = nro1 + mul5
        cinco = cinco + 1
        P_5 = mul5 / cinco
    elif(nro1 % 3 == 0 and nro1 % 100 != 0):
        mul3 = nro1 + mul3
        tres = tres + 1
        P_3 = mul3 / tres
        
print("El promedio de los multiplos de 3 son",P_3)
print("El promedio de los multiplos de 5 son",P_5)
