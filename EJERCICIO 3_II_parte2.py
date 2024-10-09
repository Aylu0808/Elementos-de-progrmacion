"""En una farmacia por cada venta, se registra.
 Nro. de factura (4 cifras). CONTROLAR
 Importe (mayor que cero). CONTROLAR
 Código que indica la forma de pago. CONTROLAR
Este código puede ser:
'M' si fue efectuada a una mutual, con el 30% de descuento.
'C' si fue venta de contado efectivo, 10% de descuento.
'T' si la venta fue con tarjeta, 15% de recargo.
La información termina con Nro. de factura cero
Por cierre de caja se debe informar:
a- Recaudación por cada forma de pago.
b- Nro. de Factura de mayor importe (se supone único)
c- Ventas totales del día.
UTILIZAR FUNCIONES PARA CONTROLAR LO PEDIDO"""

#####FUNCIONES#####
def FACTURA():
    factura = int(input("Ingrese el numero de factura: "))
    while (factura < 1000 or factura > 9999) and factura != 0:
        factura = int(input("ERROR!! Ingrese el numero de la factura: "))
    return factura

def IMPORTE():
    importe = float(input("Ingrese el importe: "))
    while importe < 0:
        importe = input("ERROR!! Ingrese el importe: ")
    return importe

def CODIGO():
    codigo = str(input("Ingrese el codigo de pago: ")).upper()
    while codigo != 'M' and codigo != 'T' and codigo != 'C':
        codigo = input("ERROR!! Ingrese el codigo de pago: ")
    return codigo

precio = 0
sum_M = 0
sum_C = 0
sum_T = 0
CANT = 0
c = 0
i = 0
f = 1
flag = 0


while f != 0:

    f = FACTURA()
    if f != 0:
        i = IMPORTE()
        c = CODIGO()

        if(c == 'M'):
            precio = i * 0.70
            sum_M = sum_M + precio
            CANT = CANT + 1
        if(c == 'C'):
            precio = i * 0.90
            sum_C = sum_C + precio
            CANT = CANT + 1
        if(c == 'T'):
            recargo = i * 0.15
            precio = recargo + i
            sum_T = sum_T + precio
            CANT = CANT + 1

        if flag == 0:
                mayor = precio
                final = f
                flag = 1
        else:
            if mayor < precio:
                final = f
                mayor = precio  

if flag == 0:
    print("No se ingresaron facturas")
else:
    print("El total recaudado en mutual es: ",sum_M)
    print("El total recaudado en efectivo es: ",sum_C)
    print("El total recaudado en tarjeta es: ",sum_T)

    print("Las ventas totales del dia fueron: ",CANT)

    print("El mayor importe encontrado es: ", final)
