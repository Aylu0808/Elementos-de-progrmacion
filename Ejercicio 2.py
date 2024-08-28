#Ingresar el valor de la hora y la cantidad de horas trabajadas por un empleado. Calcular su sueldo
#tomando en cuenta que recibe un premio de $5000 si trabajo más de 50 horas y, además, si trabajó
#más de 150 horas se le otorgan $10000 adicionales

P_horas = float(input("Ingrese el valor de la hora: "))
C_horas = float(input("Ingrese la cantidad de horas del empleado: "))

sueldo = P_horas * C_horas

if(50 <= C_horas < 150):
    sueldo_total = sueldo + 5000
    print("El sueldo total es de $",sueldo_total)
elif(C_horas >= 150):
    sueldo_total1 = sueldo + 15000
    print("El sueldo total es de $",sueldo_total1)
else:
    print("El sueldo total es de $",sueldo)