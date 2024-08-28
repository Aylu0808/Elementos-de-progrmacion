"""Ejercicio 9_Categoría de edad: Escribe un programa que tome la edad de una persona como entrada y muestre
en pantalla a qué categoría pertenece:
 Menor de 18 años: Joven
 Entre 18 y 65 años: Adulto
 Mayor de 65 años: Adulto mayor"""

edad = int(input("Ingrese la edad de la persona: "))

if(edad <= 18):
    print("La persona pertenece al grupo de los jovenes")
elif(18 < edad <= 65):
    print("La persona pertenece al grupo de los adultos")
else:
    print("La persona pertence al grupo de los adultos mayores")