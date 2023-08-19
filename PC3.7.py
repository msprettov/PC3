#PC3 
#Mauro Pretto 
#Módulos y paquetes 
#7) 
import random

def generar_lista():
    lista = []
    for i in range(20):
        lista.append(random.randint(0, 100))
    return lista

def mostrar_lista(lista):
    print(lista)

def ordenar_lista(lista):
    lista.sort()
    print(lista) 



