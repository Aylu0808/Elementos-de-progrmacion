"""Un fabricante de repuestos para tractores ha descubierto que ciertos artículos identificados por los
números de catálogo 12121 al 18081; 30012 al 45565 y 67000 al 68000 son defectuosos. Se desea
confeccionar un programa al que informándole el número de catálogo indique si el artículo es o no
defectuoso. Los artículos del catálogo van desde el 1200 al 90000. Si se ingresa otro número informar
“FUERA DE CATALOGO”."""

n_articulo = int(input("Ingrese el numero de articulo:"))

if(12121 < n_articulo < 18081 or 30012 < n_articulo < 45565 or 67000 < n_articulo < 68000):
    print("El articulo es defectuoso")
elif(n_articulo < 1200 or 90000 < n_articulo):
    print("El articulo no esta en el catalogo")
else:
    print("El articulo no es defectuoso")