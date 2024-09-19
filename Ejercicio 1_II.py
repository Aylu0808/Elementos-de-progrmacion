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
c- Ventas totales del día.  """

factura = 0
importe = 0
recargo = 0
codigo = ""
precio = 0

sum_M = 0
sum_T = 0
sum_C = 0

CANT = 0
mayor = 0
final = 0

flag = 0

factura = int(input("Ingrese el numero de factura: "))
while (factura < 1000 or factura > 9999) and factura != 0:
    factura = int(input("ERROR!! Ingrese el numero de la factura: "))

while factura != 0:

             
    importe = float(input("Ingrese el importe: "))
    while importe < 0:
        importe = input("ERROR!! Ingrese el importe: ")
            
    codigo = str(input("Ingrese el codigo de pago: ")).upper()
    while codigo != 'M' and codigo != 'T' and codigo != 'C':
        codigo = input("ERROR!! Ingrese el codigo de pago: ")
                    
    if(codigo == 'M'):
        precio = importe * 0.70
        sum_M = sum_M + precio
        CANT = CANT + 1
    if(codigo == 'C'):
        precio = importe * 0.90
        sum_C = sum_C + precio
        CANT = CANT + 1
    if(codigo == 'T'):
        recargo = importe * 0.15
        precio = recargo + importe
        sum_T = sum_T + precio
        CANT = CANT + 1
        
    if flag == 0:
            mayor = precio
            final = factura
            flag = 1
    else:
        if mayor < precio:
            final = factura
            mayor = precio     
        
                        
    factura = int(input("Ingrese el numero de factura: "))
    while (factura < 1000 or factura > 9999) and factura != 0:
        factura = int(input("ERROR!! Ingrese el numero de la factura: "))
                        
if flag == 0:
    print("No se ingresaron facturas")
else:
    print("El total recaudado en mutual es: ",sum_M)
    print("El total recaudado en efectivo es: ",sum_C)
    print("El total recaudado en tarjeta es: ",sum_T)

    print("Las ventas totales del dia fueron: ",CANT)

    print("El mayor importe encontrado es: ", final)
                     
