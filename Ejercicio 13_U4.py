"""Un negocio comercializa N productos.
Se cada uno se conoce el código del producto y el precio.
Determinar:
A-) El código de producto más caro.
B-) el precio más barato
NOTA: se considera único """

FLAG = 0

N = int(input("Cuantos productos comercializa:"))

if N > 0:

    for x in range(0,N):
        
        codigo = int(input("Ingrese el numero del codigo: "))
        precio = int(input("Ingrese el costo del producto: "))
        
        if FLAG == 0:
            barato = precio
            caro = precio
            c_caro = codigo
            FLAG = 1
            
        if caro < precio:
            caro = precio
            c_caro = codigo
        else:
            if barato > precio:
                barato = precio
                    
    print("El codigo del producto mas caro es: ", c_caro)
    print("El precio mas barato es: ",barato)
else:
    print("LA CANTIDAD INGRESADA NO ES VALIDA")
