""" Se realizó un concurso de tiro al blanco. Existen 5 participantes y cada uno de ellos
efectúa 3 disparos, registrándose las coordenadas X-Y de cada disparo. Determinar:
a. Cuantos disparos se efectuaron en cada cuadrante por cada participante
b. Cuantos disparos se efectuaron en total en el centro.
c. Determinar la distancia al origen de cada punto
 NOTA: no considere disparos sobre los ejes   """

C_1 = 0
C_2 = 0
C_3 = 0
C_4 = 0
TEEC = 0

for p in range(0,5):
    participantes = str(input("Ingrese al participante: "))
    for d in range(0,3):
        X = int(input("Ingrese las coordenadas X del disparo:"))
        Y = int(input("Ingrese las coordenadas Y del disparo:"))
        if(-1 < X < 1 and -1 < Y < 1):
            TEEC = TEEC + 1
        if(0 < X < 10 and 0 < Y < 10):
            C_1 = C_1 + 1
        elif(-10 < X < 0 and 0 < Y < 10):
            C_2 = C_2 + 1
        elif(-10 < X < 0 and -10 < Y < 0):
            C_3 = C_3 +1
        else:
            C_4 = C_4 + 1
        
        distancia = ((0-X)**2 + (0-Y)**2)**0.5
        distancia = round(distancia, 2)
        
        print("Ls distancia ",d+1,"es de:",distancia,"cm")    
    print(participantes,"realizo ",C_1,"al cuadrante 1,",C_2,"al cuadrante 2",C_3,"al cuadrantw 3,",C_4,"al cuadrante 4 y ",TEEC,"tiros al centro")
