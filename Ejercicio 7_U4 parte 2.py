"""Se ingresan números, siendo N <=80. Termina cuando N es negativo. Se pide
desarrollar un programa que aparezca en pantalla la misma cantidad de asteriscos
que el número ingresado. Si se ingresa un numero N>80 emitir un mensaje de error
y si se ingresa el número cero, en pantalla tienen que aparecer la palabra “CERO”. """

NRO = 0

while NRO >= 0:
    
    N = int(input("Ingrese un numero: "))
    
    if 0 <= N <= 80:
        for x in range (0, N):
            print("*")
    elif N > 80:
        print("ERROR")
        
    if(N == 0):
        print("CERO")
        
    if 0 > N:
        NRO = -1
        
        
print("Ingreso un numero negativo")
