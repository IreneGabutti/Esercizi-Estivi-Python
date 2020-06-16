#___Gabutti Irene___
#Scrivete una funzione di nome ordinata che prenda una lista come parametro e
#restituisca True se la lista è ordinata in senso crescente, False altrimenti. Esempio

def ordinata(lista):
    return lista == sorted(lista)

t1 = [1,2,2,3,4,5]
t2 = ['c', 'b', 'a']

print(ordinata(t1))
print(ordinata(t2))
