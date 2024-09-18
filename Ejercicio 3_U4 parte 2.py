"""Ingresar 3 valores A, B, C que corresponden a los coeficientes de una ecuación de
segundo grado.
Determinar si se obtiene raíces complejas, mediante un mensaje.
El proceso termina con el ingreso de 100 ternas de valores o que se ingrese una terna
de valores nulos """

CONT = 0
raiz = 0
raiz1 = 0
raiz2 = 0

while(CONT <= 99):
    
    A = int(input("Ingrese el coeficiente A: "))
    B = int(input("Ingrese el coeficiente B: "))
    C = int(input("Ingrese el coeficiente C: "))
    
    if(A == 0 and C == 0):
        if(B == 0):
            print("Todos los coeficientes son 0.")
            CONT = 100
    
    if((B**2 - 4*A*C) < 0):
        print("Tiene raices complejas")
        CONT = CONT + 1
    elif((B**2 - 4*A*C) > 0):
        print("Tiene raices reales")
        CONT = CONT + 1
        
if(CONT == 99):
    print("Se llego a las 100 ternas")