""" Ingresar un numero entero positivo y determinar su factorial """

nro = int(input("Ingrese un numero entero: "))

if(nro < 0):
    print("El numero ingresado no es un entero o no es postivo")
else:
    fac = 1
    
for i in range(1, nro + 1):
        fac *= i
        
print("El factorial es:",fac)
