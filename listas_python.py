


#EJERCICIO PRACTICO EN PYTHON


"""
1. CAPTURAR UNA LISTA
2. MOSTRAR UNA LISTA
3. AGREGAR UN ELEMENTO A LA LISTA
4. ELIMINAR UN ELEMENTO DE LA LISTA
5. MODIFICAR UN ELEMENTO DE LA LISTA
6. SALIR
"""


def capturar():
    global lista
    lista = []
    n = int(input("Cuantos elemetos va a tener tu lista \n"))

    for i in range(0,n):
        print("Ingresa el elemento del indice", i)
        elemento = input()
        lista.insert(i, elemento )

def mostrar():
    print(lista)

def agregar():
    elemnto = input("Ingresa un elemento que desees agregar \n")

    indice = int(input("Ingrese el indice donde deseas agregarlo \n"))

    longuitud = int(len(lista))
    if(indice >longuitud or indice < 0):
        print("El indice debe estar entre 0 y", longuitud)
    else:
        lista.insert(indice,elemnto)
        print("Elemento Agregado")

#~DEFINIENDO LA FUNCION ELIMINAR

def eliminar():
    indice = int(input("Ingrese el indice del Elemento que desea eliminar"))

    longuitud = int(len(lista))
    if (indice > longuitud or indice < 0):
        print("El indice debe estar entre 0 y", longuitud-1)
    else:
        del lista[indice]
        print("Elemento Eliminado")

#LA FUNCION MODIFICAR

def modificar():
    indice = int(input("Ingrese el indice del Elemento que desea Modificar \n"))

    elemento = input("Ingrese el Nuevo valor de Elemento \n")
    longuitud = int(len(lista))
    if (indice > longuitud or indice < 0):
        print("El indice debe estar entre 0 y", longuitud - 1)
    else:
        lista[indice] = elemento
        print("Elemento Modificado")


#LA FUNCION PRINCIPAL
#holas mundo

def principal():
    opcion = "1"

    while(opcion != 6):
        print("1. CAPTURAR UNA LISTA")
        print("2. MOSTRAR UNA LISTA")
        print("3. AGREGAR UN ELEMENTO A LA LISTA")
        print("4. ELIMINAR UN ELEMENTO DE LA LISTA")
        print("5. MODIFICAR UN ELEMENTO DE LA LISTA")
        print("6. SALIR")

        opcion = int(input("Que deseas hacer \n"))
        if(opcion == 1):
            capturar()
        elif(opcion == 2):
            mostrar()
        elif (opcion == 3):
            agregar()
        elif (opcion == 4):
            eliminar()
        elif (opcion == 5):
            modificar()
        elif (opcion == 6):
            print("Programa Terminado")
        else:
            print("Opcion Incorrecta")



#~LLAMANDO A LA FUNCION PRINCIPAL

principal()





