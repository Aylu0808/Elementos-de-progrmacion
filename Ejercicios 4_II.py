"""Un programa de TV realiza un concurso donde los televidentes deben llamar diciendo
cual es la altura del Aconcagua.
Por cada llamada recibida se conoce:
 DNI del concursante ( entero de 8 cifras)
 Zona de donde llama ( ‘C’ (Capital) – ‘G’ (Gran Bs. As) – ‘R’(Resto del país))
 Respuesta del participante (entero mayor a 1000)
Esta información termina con DNI cero o negativo
CONTROLAR O VALIDAR TODA LA INFORMACION INGRESADA SEGÚN LOS
PARAMETROS INDICADOS
Sabiendo que la altura del Aconcagua es de 6962 metros, se pide informar:
a- Porcentaje de respuestas correctas.
b- Cantidad de respuestas equivocadas en menos de 100 metros.(de más o de
menos)
c- DNI del televidente que dijo la mayor altura incorrecta. (suponer único)
d- Cantidad de llamadas de cada zona."""

DNI = 0
dni_mayor = 0
res_final = 0
zona = ""
respuesta =0 
aconcagua = 6962
correcta = 0
equivocadas = 0
incorrecta = 0
capital = 0
GB = 0
resto = 0
flag = 0
total_llamadas = 0
porcentaje = 0

DNI = int(input("DNI del participante: "))
while DNI < 10000000 and DNI > 99999999:
    DNI = int(input("ERROR!! Ingrese un DNI valido: "))

while DNI > 0:

    zona = input("Ingrese la zona donde vive: ")
    while zona != "C" and zona != "G" and zona != "R":
        zona = input("ERROR!!Ingrese una zona valida: ")

    if zona == "C":
        capital = capital + 1
    if zona == "G":
        GB = GB + 1
    if zona == "R":
        resto = resto + 1

    respuesta = int(input("Ingresar la repuesta: "))
    while respuesta < 1000:
        respuesta = int(input("ERROR!! Ingresar una respuesta valida: "))

    total_llamadas = total_llamadas + 1

    if respuesta == 6962:
        correcta = correcta + 1
    else:
        if 7062 >= respuesta >= 6862:
            equivocadas = equivocadas + 1
        else:
            incorrecta = incorrecta + 1
    
        if flag == 0:
            dni_mayor = DNI
            res_final = respuesta
            flag = 1
        else:
            if res_final < respuesta:
                dni_mayor = DNI
                res_final = respuesta
    
    DNI = int(input("DNI del participante: "))
    while DNI < 10000000 and DNI > 99999999:
        DNI = int(input("ERROR!! Ingrese un DNI valido: "))

if total_llamadas > 0:
    porcentaje = (correcta / total_llamadas) * 100 
else:
    porcentaje = 0

print("--- Resultados del concurso ---")
print("El porcentaje de respuestas correctas es: ",porcentaje)
print("La cantidad de respuestas equivacadas en 100m es: ",equivocadas)

print("De capital hubo ",capital,"llamdas de Gran Bs. As ",GB,"y del resto ",resto)

if dni_mayor != 0:
    print("El dni del participante que dijo la mayor altura incorrecta es: ",dni_mayor)
else:
    print("No hubo respuestas incorrectas")
