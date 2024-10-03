"""Crear una FUNCIÓN llamada MAYOR que devuelva el mayor de dos números. Si
son iguales retorna cero. Indicar el resultado en el programa principal. """

###############################FUNCIONES###############################
def MAYOR():
    if(nro1 == nro2):
        NRO = 0
    elif(nro1 < nro2):
        NRO = nro2
    else:
        NRO = nro1
        
    return NRO

nro1 = int(input("Ingrese el primer valor: "))
nro2 = int(input("Ingrese el segundo valor: "))
while nro1:

    mayor = MAYOR()
    
    print("El numero mayor es:",mayor)
    
    nro1 = int(input("Ingrese el primer valor: "))
    nro2 = int(input("Ingrese el segundo valor: "))
