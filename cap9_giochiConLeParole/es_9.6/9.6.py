#___Gabutti Irene___
#Scrivete una funzione di nome alfabetica che restituisca True se le lettere di una
#parola compaiono in ordine alfabetico (le doppie valgono).


def alfabetica(nomeFile):
    nomeFile = open(nomeFile)
    verificato = True
    
    for riga in nomeFile:
        parola = riga.strip()
        precedente = parola[0]
        verificato = True
        for i in parola:
            if i < precedente:
                verificato = False
            precedente = i
        if(verificato):
            print(parola)
  
alfabetica("word.txt")

