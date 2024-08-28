#Una fábrica comercializa N equipos, conociendo el costo de la materia prima, el costo de armado,
#costo de flete, de cada equipo y además al costo total se agrega un 200% para su venta. Hallar la
#facturación resultante total

EQUIPOS = int(input("Ingrese la cantidad de quipos que se comercializan: "))
CMP = float(input("Ingrese el costo de la materia prima: "))
CA = float(input("Ingrese el costo del armado: "))
CF = float(input("Ingrese el costo del flete: "))
CE = float(input("Ingrese el costo del equipo: "))

CT = (CMP+CA+CF+CE)*EQUIPOS

CTV = CT*2

print("El costo de la facturacion total es de: ", CTV)
