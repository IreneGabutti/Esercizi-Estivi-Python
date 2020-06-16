#___Gabutti Irene___
#Scrivete una funzione di nome tronca che prenda una lista, la modifichi togliendo
#il primo e l’ultimo elemento, e restituisca None.

def tronca(lista):
    del lista[0]
    del lista[-1]
    
    print(lista)

t = [1,2,3,4,5,6]
tronca(t)
