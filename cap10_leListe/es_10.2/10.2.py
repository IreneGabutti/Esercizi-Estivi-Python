#___Gabutti Irene___
#Scrivete una funzione di nome somma_cumulata che prenda una lista di numeri
#e restituisca la somma cumulata, cioè una nuova lista dove l’i-esimo elemento è la somma dei primi
#i + 1 elementi della lista di origine

def somma_cumulata(lista):
    listaSomme = []
    conto = 0
    
    for i in lista:
        conto = conto + i
        listaSomme.append(conto) 
    
    print(lista)
    print(listaSomme)

t = [1,2,3,4,5,6]
somma_cumulata(t)
