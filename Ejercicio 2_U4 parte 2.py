"""Confeccionar un programa que calcule e informe las potencias de 2 cuyo resultado
sea menor que 600(1, 2, 4, 8, etc. ) 
 """

potencia = 0
nro = 0

while(potencia < 600):
    
    potencia = 2 ** nro
    
    if(potencia < 600):
        print("La potencia de 2 a la",nro,"es: ",potencia)
        nro = nro + 1 
    
