#Confeccionar un programa que solicite el ingreso del valor del radio (r) de un círculo y con dicho valor
#calcule la superficie del círculo, la longitud de la circunferencia (perímetro) y el volumen de la esfera.
# Superficie = pir2, perimetro = 2pir y volumen = 4/3pir3

RADIO = float(input("Ingrese el valor del del radio del circulo en cm:"))

SUP = 3.14 * RADIO * 2
VOLUMEN = 4 / 3 *(3.14 * RADIO * 3)

print("El perimetro es de: ",SUP,"cm, la superficie es de: ",SUP,"cm² y el volumen es de:",VOLUMEN,"cm³")
