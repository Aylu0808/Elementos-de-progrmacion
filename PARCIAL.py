def CargarDatos_I(CP,CI,VC,N): #Funcion de carga de datos inciales
    nuevo = 0
    for x in range(0,N):
        codigo_V = True
        while codigo_V: #mientras el codigo del producto sea valido entra en el while
            nuevo = ValidaciondeRango(1000,9999,"Ingrese el codigo del producto: ")
            if x > 0 and nuevo == CP[x-1]+1: #verifica si el nuevo codigo es correlativo
                print("ERROR! El codigo no puede ser correlativo.")
            elif x == 0 or nuevo > CP[x-1]: #Si x es igual al 0 o si numero es mas grande que el numero anterior 
                CP[x] = nuevo
                CI[x] = Validacion(0,"Ingrese la cantidad del producto(kilos): ")
                VC[x] = Validacion(0,"Ingrese el valor de compra por kilo: ")
                codigo_V = False #Sale del while

def Validacion(valor,texto): #Funcion para validar un valor minimo
    num = int(input(texto))
    while num <= valor:
        num = int(input("ERROR! Ingrese un valor valido:"))
    return num

def ValidaciondeRango(I,F,texto): #Funcion para validar un rango especifico
    num = int(input(texto)) 
    while (num < I or num > F) and num != 0:
        num = int(input("ERROR! Ingrese un valor valido: "))
    return num

def Validacion_L(A,B,C,texto): #Funcion para validar una entrada de texto especifica
    valor = input(texto).upper() #solicita la letra y la covierte en mayuscula
    while valor != A and valor != B and valor != C:
        valor = input("ERROR! Ingrese una letra valida:").upper()# Convierte la la letra en mayuscula
    return valor

def busquedad(Lista,DatoABuscar): #Funcion para buscar en una lista
    POSI = -1  #posicion como no encontrada
    I = 0       #indice
    while POSI == -1 and I < len(Lista): #se ejecuta mientras no se encuentre el dato y siga dentro del tamaño 
        if Lista[I] == DatoABuscar:
            POSI = I #Guarda posicion   
        else:
            I+=1 #Si no es igual incrementa el indice
    return POSI

def MostrarDatos(L1, L2): #Funcion para mostrar datos finales
    print("%20s%s" % ("","CANTIDAD EN EXISTENCIA TOTAL"))
    print("%13s%s" % ("","CODIGO PRODUCTO"),"%8s%s" % ("", "CANTIDAD TOTAL(kilos)"))
    for i in range(len(L1)):
        print("%22d\t%22d" % (L1[i], L2[i]))

def MINIMO(A,B,C): #Funcion para econtrar el minimo entre tres valores
    if A == B and A == C:
        if B == C:
            minimo = "IGUALES"
    else:
        if A <= B and A <= C:
            minimo = "LUNES"
        elif B <= A and B <= C:
            minimo = "MIERCOLES"
        else:
            minimo = "VIERNES"
    return minimo

def MAXIMO(lista,lista_2): #Funcion para encontrar el producto maximo
    max = 0 #guarda el codigo
    recep = False #Flag para verificar si hay mas codigos iguales
    for x in range(len(lista)): #si se encontro se actualiza el maximo
        if lista[x] > max:
            max = lista[x]
            recep = True #Indica que hay al menos un codigo
            print("El producto mas veces recepcionado fue:",lista_2[x])
        elif lista[x] == max: #Si hay otro codigo igual 
            print("El otro codigo con la misma cantidad de recepciones fue:",lista_2[x])

def no_recepcionados(lista_2,lista,A): #Funcion que muestra los prductos no recepcionados
    for x in range(0,A):
        if lista[x] == 0: #Verifica que no sea 0
            print("Prodcutos que no fueron recepcionados: ",lista_2[x])

def main():
    #CARGA DE PRODUCTOS DEL DEPOSITO
    N = Validacion(0,"Ingrese la cantidad de productos en existencia: ") 

    PRODUCTO= [0]*N 
    CANTIDAD = [0]*N
    PRECIO = [0]*N
    RECEPCIONES =[0]*N #Cuenta las recepciones por producto

    CargarDatos_I(PRODUCTO,CANTIDAD,PRECIO,N) #Llama a la funcion para la carga inicial

    C = 0
    G = 0
    O = 0
    LUNES = 0
    MIERCOLES = 0
    VIERNES = 0
    COMPRA = 0
    TOTAL = 0

    CODIGO = ValidaciondeRango(1000,9999,"Ingrese el codigo del producto a recepcionar: ")
                                   
    while CODIGO != 0: #Mientras el codigo no sea 0 ingresa al while

        POS = 0
        POS = busquedad(PRODUCTO,CODIGO) #Busca el codigo del producto en la lista

        if POS >= 0: #Si se encontro el producto
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
                COMPRA = PRECIO[POS] * 1.05 #Calcula con incremento para el lunes
            else:
                COMPRA = PRECIO[POS] #sin incremento para los otros dias
                if DIA == "MIERCOLES":
                    MIERCOLES += 1
                if DIA == "VIERNES":
                    VIERNES += 1

            CANTIDAD[POS] += CANTIDAD_I #suma la cantidad existente con la ingresada
            TOTAL = CANTIDAD_I * COMPRA #Calcula el total de cada recepcion
            print("Importe pagado por la recepcion: ",TOTAL)

            RECEPCIONES[POS] +=1 #Incrementa la recepcion por producto

        else:
            print("No se encontro el codigo del producto solicitado")

        CODIGO = ValidaciondeRango(1000,9999,"Ingrese el codigo del producto: ")

    print("\n")
    MostrarDatos(PRODUCTO,CANTIDAD) #Muentra los datos finales

    print("Se recepciono de CABA",C,"de GBA",G,"y de otros",O)

    MIN = MINIMO(LUNES,MIERCOLES,VIERNES) #funcion minimo para encontrar el dia que tuvo menos recepciones
    if MIN == "IGUALES": #Si es igual a la palabra iguales
        print("Todos los dias tuvieron la misma cantidad de recepciones")
    else:
        print("El dia de la semana con menor cantidad de recepciones fue el",MIN)

    MAXIMO(RECEPCIONES,PRODUCTO) #Calcula y encuentra los producto/s con mayor recepcion

    no_recepcionados(PRODUCTO,RECEPCIONES,N) #Muestra los productos no recepcionados

if __name__ == "__main__":
    main()
