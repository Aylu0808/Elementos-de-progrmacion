"""Ejercicio 6_ Un negocio vende distintos artículos identificados por un código, según se muestra:
 código 1; 10; 100: 90 pesos la unidad. YA
 código 2; 22; 222: 700 pesos la unidad. La caja de 10 unidades vale 650 pesos.
 código 3; 33: 300 pesos la unidad. Si la compra es por más de 10 unidades se hace un
descuento del 10% sobre el total de la compra. YA
 código 4; 44: 100 peso la unidad. YA
Confeccionar un programa que ingrese como dato el código de un artículo y la cantidad a comprar y se
informe el importe de la compra, con las siguientes leyendas:
CODIGO ARTÍCULO xxxxx CANTIDAD xxxx IMPORTE A PAGAR $ xxxx.xx"""

codigo = int(input("Ingrese el codigo del articulo: "))
cantidad = int(input("Ingrese la cantidad que va a comprar: "))

if(codigo == 1 or codigo == 10 or codigo == 100):
    Total = cantidad * 90
    print("CODIGO ARTÍCULO: ",codigo,"CANTIDAD: ",cantidad, "IMPORTE A PAGAR: $", Total)
elif(codigo == 2 or codigo == 22 or codigo == 222):
    if(cantidad == 10):
        Total = 650
        print("CODIGO ARTÍCULO: ",codigo,"CANTIDAD: ",cantidad, "IMPORTE A PAGAR: $", Total)
    else:
        Total = cantidad * 700
        print("CODIGO ARTÍCULO: ",codigo,"CANTIDAD: ",cantidad, "IMPORTE A PAGAR: $", Total)
elif(codigo == 4 or codigo == 44):
    Total = cantidad * 100
    print("CODIGO ARTÍCULO: ",codigo,"CANTIDAD: ",cantidad, "IMPORTE A PAGAR: $", Total)
elif(codigo == 3 or codigo == 33):
    if(cantidad > 10):
        Total = cantidad * 300
        Descuento = Total * 0.10
        Final = Total - Descuento
        print("CODIGO ARTÍCULO: ",codigo,"CANTIDAD: ",cantidad, "IMPORTE A PAGAR: $",Final)
    else:
        Total = cantidad * 300
        print("CODIGO ARTÍCULO:",codigo,"CANTIDAD:",cantidad, "IMPORTE A PAGAR: $", Total)
