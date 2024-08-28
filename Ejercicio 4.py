"""Ejercicio 4_ Confeccionar un programa que permita convertir grados sexagesimales a radianes y viceversa, según
el valor de un código que se ingresa junto al valor. Si código = 1 se ingresan grados, si es 2 se ingresan
radianes."""

codigo = int(input("Ingrese 1 para poder ingresar un numero grados sexagesimales o ingrese 2 para radianes: " ))

PI = 3.141592653589793

if(codigo == 1):
    valor = int(input("Ingrese el valor del numero: "))
    radian = valor * (PI/180)
    print(valor,"equivalen a",radian,"radianes")
else:
    valor = int(input("Ingrese el valor del numero: "))
    grados = valor * (180/PI)
    print(valor,"equivalen a",grados,"°")