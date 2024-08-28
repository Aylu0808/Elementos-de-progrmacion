""" Ejercicio 5_ Se conoce las dos notas correspondiente a una materia de un estudiante y se pide que se indique si
ha promocionado ( ambas notas mayores o iguales a 7), reprobado (ambas o alguna menor que 4) ,
cursado( ambas o alguna de ellas menor a 7 y mayor o igual a 4)"""

nota_1 = float(input("Ingrese la primera nota: "))
nota_2 = float(input("Ingrese la segunda nota: "))

if(nota_1 >= 7 and nota_2 >= 7):
    print("El alumno ha promocionado la materia")
elif(4 <= nota_1 < 7 or 4 <= nota_2 < 7):
    print("El alumno ha cursado la materia")
else:
    print("El alumno ha reprobado la materia")