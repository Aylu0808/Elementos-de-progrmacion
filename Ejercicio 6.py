#Se ingresa un numero entero positivo de 3 cifras. Descomponerlo en unidad, decena y centena

num = int(input("Ingrese un numero de 3 cifras: "))

if 100 <= num <= 999:
    cen = num // 100
    decena = (num % 100) // 10
    unidad = num % 10

    print("Las centenas son ",cen,"las decenas son ",decena,"y las unidades son ",unidad)
else:
    print("Ingrese un numero de 3 cifras")
