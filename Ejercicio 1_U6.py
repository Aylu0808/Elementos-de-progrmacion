"""Se dispone de una lista de 10 valores enteros
Se pide:
a-) Cargar los datos en una lista llamada LA
b-) Copiar LA en LB
c-) Sumar los elementos de la lista LA
d-) Valor promedio de la lista LA
e-) Cantidad de ceros contenidos en la lista LA
f-) Generar una lista LC correspondiente a la suma de LA y LB.
g-) Copiar LA en orden inverso en otra lista llamado LD.
h-) Posiciones de elementos pares de la lista LA."""

def ingresaMayorA(valor):
    num=int(input("Ingrese un valor "))
    while num<=valor:
        num=int(input("Ingrese un valor "))
    return num

def cargarLista(li,ce):
    for i in range(ce):
        li[i]=int(input("Ingrese un valor "))

def copiarLista(origen,destino):
    for i in range(len(origen)):
        destino[i]=origen[i]
        
def sumaLista(lista):
    resu=0
    for i in range(len(lista)):
        resu+=lista[i]
    return resu

def promedio(suma,cant):
    return suma/cant

def contarEnLista(lista,valor):
    resu=0
    for i in range(len(lista)):
        if lista[i]==valor:
            resu+=1
    return resu

def copiaInvertida(origen,destino):    
    for i in range(len(origen)):
        destino[i]=origen[len(origen)-1-i]
        

def main():
    N=ingresaMayorA(0)
    
    LA=[0]*N
    LB=[0]*N
    LC=[0]*N
    LD=[0]*N
    
    #a
    cargarLista(LA,N)
    print(LA)
    #b
    copiarLista(LA,LB)
    print(LB)
    #c
    resultado=sumaLista(LA)
    print("La suma de los elementos de la lista A->",resultado)
    #d
    print("El valor promedio de la lista A->",promedio(resultado,len(LA)))
    #e
    print("La cantidad de ceros en la lista A->",contarEnLista(LA,0))
    #f
    for i in range(len(LA)):
        LC[i]=LA[i]+LB[i]
    print(LC)
    #g
    copiaInvertida(LA,LD)
    print(LD)
    #h
    for i in range(len(LA)):
        if LA[i]%2==0:
            print(i)
            
            
if __name__=="__main__":
    main()
