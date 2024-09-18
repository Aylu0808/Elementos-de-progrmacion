"Encontrar el factorial de un número dado usando while "

nro = int(input("Ingrese un numero: "))

factorial = 1
contador = 1

while contador <= nro:
    factorial = contador * factorial
    contador = contador + 1

print("El factorial de ",nro,"es: ",factorial)
