#___Gabutti Irene___
#Scrivete una funzione che legga le parole in words.txt e le inserisca come chiavi
#in un dizionario. I valori non hanno importanza. Usate poi l’operatore in come modo rapido per
#controllare se una stringa è contenuta nel dizionario.


def chiavi(nomeFile):
    #parole = []
    dizionario = {}
    dizionario = open(nomeFile, "r").read()
    print(dizionario)
    
    for key in dizionario:
        print(key)


if __name__ == "__main__":
    chiavi("parole.txt")