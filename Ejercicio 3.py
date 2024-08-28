#Se ingresa la distancia en metros y convertirla a centímetros y pulgadas. 1 metro es igual a 100
#centímetros y 39.37 pulgadas aproximadamente. 

U = float(input("Ingrese la distancia en metros: "))
CENT = U * 100
PUL = U * 39.37
print("Los",U,"m ingresados son:",CENT,"cm y",PUL,"pulgadas")