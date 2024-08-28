#Una pizzería vende empanadas por unidad o por docena, la docena cuesta $10000 pero si se compra
#individualmente se cobra $1000 la unidad. Si se compran más empanadas que no se agrupen en
#docenas las adicionales se cobran como por unidad. Indicar el precio total a abonar.

p_docena = 10000
p_unidad = 1000

TOTAL = int(input("Ingrese la cantidad de empanadas que desea comprar: "))

docenas = TOTAL // 12
unidades = TOTAL % 12

P_TOTAL = (docenas * p_docena) + (unidades * p_unidad)

print("El precio total es: ", P_TOTAL)
