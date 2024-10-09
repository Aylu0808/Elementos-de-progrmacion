"""Se ingresan números enteros entre 1 y 10- Función LeeControl
Indicar si cada número es par o impar - Función
Indicar el factorial de cada número - Función
Promedio de los números ingresados - Función
Porcentaje de números pares - Función
LA INFORMACION TERMINA CON NRO IGUAL A CERO """
#####DEFINICIONES#####
def LeeControl():
    nro = int(input("Ingrese un numero del uno al diez: "))
    while nro < 0 or nro > 10:
        nro = int(input("ERROR!!Ingrese un numero del uno al diez: "))
    return nro

def par_impar(numero, par):
    if numero % 2 == 0:
        par += 1
        print("Es par")
    else:
        print("Es impar")
    return par

def factorial(numero):
    facto = 1
    for x in range(1, numero + 1):
        facto *= x
    print("El factorial es de: ", facto)
    return facto

def promedio(total, numero_t):
    prom = numero_t / total
    return prom

def numeros_pares(par, total):
    resultado = (par * 100) / total
    return resultado

#####PROGRAMA PRINCIPAL#####
numero = 1
numero_t = 0
par = 0
total = 0
por = 0

while numero != 0:

    numero = LeeControl()
    if numero != 0:
        numero_t += numero
        total += 1

        par = par_impar(numero, par)

        factorial(numero)
        p = promedio(total, numero_t)
        por = numeros_pares(par, total)

print("El promedio de los números es: %.2f" % p)
print("El porcentaje de números pares es de: %.2f%%" % por)
