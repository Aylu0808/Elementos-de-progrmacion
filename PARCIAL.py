#########################################################################################################################################################################
def CargarDatos_I(CP,CI,VC,N): #Funcion de carga de datos inciales
    for x in range(0,N):
        CP[x] = ValidaciondeRango(1000,9999,"Ingrese el codigo del producto: ")
        CI[x] = Validacion(0,"Ingrese la cantidad del producto(kilos): ")
        VC[x] = Validacion(0,"Ingrese el valor de compra por kilo: ")

def Validacion(valor,texto): #Funcion para validar con un solo valor
    num = int(input(texto))
    while num <= valor:
        num = int(input("ERROR! Ingrese un valor valido:"))
    return num

def ValidaciondeRango(I,F,texto): #Funcion para validar el codigo del producto
    num = int(input(texto))
    while (num < I or num > F) and num != 0:
        num = int(input("ERROR! Ingrese un valor valido: "))
    return num

def Validacion_L(A,B,C,texto): #Funcion para validar con string
    valor = input(texto).upper()
    while valor != A and valor != B and valor != C:
        valor = input("ERROR! Ingrese una letra valida:").upper()
    return valor

def busquedad(Lista,DatoABuscar): #Funcion para buscar en una lista
    POSI = -1   
    I = 0       
    while POSI == -1 and I < len(Lista):
        if Lista[I] == DatoABuscar:
            POSI = I   
        else:
            I+=1   
    return POSI

def MostrarDatos(L1, L2): #Mostrar datos finales
    print("%20s%s" % ("","CANTIDAD EN EXISTENCIA TOTAL"))
    print("%13s%s" % ("","CODIGO PRODUCTO"),"%8s%s" % ("", "CANTIDAD TOTAL(kilos)"))
    for i in range(len(L1)):
        print("%22d\t%22d" % (L1[i], L2[i]))

def MINIMO(A,B,C):
    if A <= B and A <= C:
        minimo = "LUNES"
    elif B <= A and B <= C:
        minimo = "MIERCOLES"
    else:
        minimo = "VIERNES"
    return minimo

def MAXIMO(lista,lista_2):
    max = 0
    codigo = 0
    for x in range(len(lista)):
        if lista[x] > max:
            max = lista[x]
            codigo = lista_2[x]
    return codigo

def no_recepcionados(lista_2,lista,A):

    for x in range(0,A):
        if lista[x] == 0:
            print("Prodcutos que no fueron recepcionados: ",lista_2[x])

def main():
    #CARGA DE PRODUCTOS DEL DEPOSITO
    N = Validacion(0,"Ingrese la cantidad de productos en existencia: ") 

    PRODUCTO= [0]*N 
    CANTIDAD = [0]*N
    PRECIO = [0]*N
    RECEPCIONES =[0]*N #Cuenta las recepciones por producto

    CargarDatos_I(PRODUCTO,CANTIDAD,PRECIO,N)

    #CARGA DE PRODUCTOS NUEVOS EN EL MES
    CODIGO = ValidaciondeRango(1000,9999,"Ingrese el codigo del producto a recepcionar: ")

    C = 0
    G = 0
    O = 0
    LUNES = 0
    MIERCOLES = 0
    VIERNES = 0
    COMPRA = 0
    TOTAL = 0

    while CODIGO != 0:

        POS = 0
        POS = busquedad(PRODUCTO,CODIGO)

        if POS >= 0:
            CANTIDAD_I = Validacion(0,"Ingrese la cantidad del producto: ")

            ZONA_T = Validacion_L("C","G","O","Ingrese la letra de la zona de procedencia: ").upper()
            if ZONA_T == "C":
                C += 1
            if ZONA_T == "G":
                G += 1
            if ZONA_T == "O":
                O += 1

            DIA = Validacion_L("LUNES","MIERCOLES","VIERNES","Ingrese el dia de recepcion: ").upper()
            if DIA == "LUNES":
                LUNES += 1
                COMPRA = PRECIO[POS] * 1.05 #calcula con incremento para el lunes
            else:
                COMPRA = PRECIO[POS] #sin incremento para los otros dias
                if DIA == "MIERCOLES":
                    MIERCOLES += 1
                if DIA == "VIERNES":
                    VIERNES += 1

            CANTIDAD[POS] += CANTIDAD_I #suma la cantidad existente con la ingresada
            TOTAL = CANTIDAD_I * COMPRA
            print("Importe pagado por la recepcion: ",TOTAL)

            RECEPCIONES[POS] +=1 #cuenta la recepcion por producto

        else:
            print("No se encontro el codigo del producto solicitado")

        CODIGO = ValidaciondeRango(1000,9999,"Ingrese el codigo del producto: ")

    print("Se recepciono de CABA",C,"de GBA",G,"y de otros",O)

    MostrarDatos(PRODUCTO,CANTIDAD)

    MIN = MINIMO(LUNES,MIERCOLES,VIERNES) #funcion minimo para encontrar el dia que tuvo menos recepciones
    print("El dia de la semana con menor cantidad fue el",MIN)

    if MAXIMO(RECEPCIONES,PRODUCTO) != -1:  # Verificar que se haya encontrado un producto
        print("Código del producto de máxima cantidad de veces recepcionado:", MAXIMO(RECEPCIONES,PRODUCTO))
    else:
        print("No se han recepcionado productos.")

    no_recepcionados(PRODUCTO,RECEPCIONES,N)


if __name__ == "__main__":
    main()
