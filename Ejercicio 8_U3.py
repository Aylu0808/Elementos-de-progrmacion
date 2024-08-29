""""Ejercicio 8_ Ingresar dos números el mes y el año un mes y muestre en pantalla la cantidad de días que tiene
ese mes. Considera el caso especial de febrero y si el año es bisiesto (tiene 29 días)."""

año = int(input("Ingrese el año: "))
mes = int(input("Ingrese el mes: "))

if(año % 4 == 0 and año % 100 != 0 or año % 400 == 0 and mes == 2):
    print("El mes tiene 29 dias")
else:
    print("El mes tiene 28 dias")

if(mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8
         or mes == 10 or mes == 12 and mes != 2):
    print("El mes tiene 31 dias")
else:
    if(mes != 2):
        print("El mes tiene 30 dias")
