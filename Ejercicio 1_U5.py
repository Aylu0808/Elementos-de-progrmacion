"""Se ingresan longitudes es cm., hasta que se ingrese una longitud igual a 0. Realizar
una FUNCIÓN que convierta dicha medida en pulgadas. 1 pulgada = 2.54 cm"""

###############################FUNCIONES###############################
def CONVERSION():
    
    pulgadas = medida / 2.54
    
    return pulgadas           


result = 0

medida = int(input("Ingrese una longitud: "))
while medida < 0:
    medida = int(input("Ingrese una longitud valida: "))
    
if medida == 0:
    print("No se ingresaron medidas")
else:
    while medida != 0:
        
        result = CONVERSION()
        
        print("La conversion dio: %.2f"%result,"pulgadas")
        
        medida = int(input("Ingrese una longitud: "))
        while medida < 0:
            medida = int(input("Ingrese una longitud valida: "))
    print("Se termino el ingreso")
