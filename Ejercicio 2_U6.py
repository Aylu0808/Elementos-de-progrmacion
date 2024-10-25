""""En un negocio se conoce la lista de precios de sus N productos.
La lista consta de:
 código producto (nro. entero de 3 cifras)
 Descripción del producto
 precio unitario (real)
Se pide:
a-) cargar los datos en listas paralelas (codigo - descripción - precio). FUNCION X
b-) Mostrar los datos ingresados (lista) FUNCION X 
c-) Indicar los productos más caros FUNCION
d-) Determinar el precio promedio FUNCION
f-) Indicar que productos (descripción) están por debajo del precio promedio. FUNCION
g-) Consultar el precio, según el código del producto. FUNCION BUSQUEDA
 Fin de la consulta código de producto cero. """

####################FUNCIONES####################

def Validacion(valor,texto):
    num = int(input(texto))
    while num <= valor:
        num = int(input(texto))
    return num

def ValidacionDeRango(li,ls,texto):
    num = int(input(texto))
    while num < li or num > ls:
        num = input(texto)
    return num

def CargarDatos(c,p,d):
    for x in range(0,len(c)):
        c[x] = ValidacionDeRango(100,999,"Ingrese el codigo del producto: ")
        p[x] = Validacion(0,"Ingrese el precio unitario del producto: ")  
        d[x] = input("Ingrese una descripcion del prodcuto: ")

def MostrarDatos(A,B,C):
    print("------------------------------------------------------------------------")
    print("Los productos cargados son")
    print("------------------------------------------------------------------------")
    print("CODIGO / PRECIO / DESCRIPCION")
    
    for x in range(0,len(A)):
        print("%6d\t%6.2f\t%10s" % (A[x],B[x],C[x]))
        
def precioxd(lista):
    valMax = 0
    for x in range(len(lista)):
        if x == 0 or lista[x] > valMax:
            ValMax = lista[x]
    return valMax

def promedio(SUM,CANT):
    PROM = 0
    PROM = SUM/ CANT
    return PROM

def suma(lista):
    result = 0
    for x in range(len(lista)):
        result += lista[x]
    return result

def ListaPrecio(LI,LD,prom):
    print("ARTICULOS CON PRECIO MENOR AL PRECIO PROMEDIO $")
    for x in range(len(LI)):
        if LD[x] < promedio:
            print(LI[x])
            
def busquedad(lista, valorBuscado):
    pos = -1
    i = 0
    while pos == -1 and i < len(lista):
        if lista[i] == valorBuscado:
            pos = i
        else:
            i += 1
    return pos
    
####################PROGRAMA PRINCIPAL####################
            
def main():
    N = Validacion(0,"Ingrese la cantidad de productos que desea registrar: ")
    
    CODIGO = [0]*N
    PRECIO = [0]*N
    DESCRIPCION = [0]*N
    prom = 0
    c = 0
    
    CargarDatos(CODIGO,PRECIO,DESCRIPCION)
    MostrarDatos(CODIGO,PRECIO,DESCRIPCION)
    
    precioMaximo = precioxd(PRECIO)
    print("El precio maximo es $",precioMaximo)
    print("los productods mas caros son: ")
    for x in range(len(PRECIO)):
        if PRECIO[x] == precioMaximo:
            print(CODIGO[x])
    
    c = suma(PRECIO)
    prom = promedio(c,len(PRECIO))
    print("El promedio de los precios es de $",prom)
    
    #consulta de precios
    auxCodigo = int(input("Ingrese el codigo a consultar: "))
    while auxCodigo != 0:
        posi = busquedad(CODIGO,auxCodigo)
        if posi == -1:
            print("EL PRODUCTO CONSULTADO NO EXISTE")
        else:
            print("EL PRECIO DEL ARTICULO",auxCodigo, "es", PRECIO[posi])
    auxCodigo = int(input("Ingrese el codigo a consultar: "))
            
            
            
if _name_ == "_main_":
    main()
