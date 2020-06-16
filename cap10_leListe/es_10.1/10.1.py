#___Gabutti Irene___
#Scrivete una funzione di nome somma_nidificata che prenda una lista di liste di
#numeri interi e sommi gli elementi di tutte le liste nidificate

def somma_nidificata(lista):
    conto = 0
    for i in lista:
        #utilizzo un'apposita funzione di python per sommare gli elementi della lista nidificata
        conto += sum(i)
    print(conto)


t = [[1,2], [3], [5,6,7]]
somma_nidificata(t)
