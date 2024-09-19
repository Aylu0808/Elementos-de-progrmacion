"""Ingresar un número en base 10 y convertirlo a binario."""

nro = int(input("Ingrese un numero en base 10:"))

binario = ""
contador = 0

while nro > 0:
    
    resto = nro % 2
    binario = str(resto) + binario
    nro = nro // 2
    contador = contador + 1
    
print("El numero ",nro,"en binario es: ",binario)
    
