#___Gabutti Irene___
#1: Scrivere una funzione di nome 'evita' che richieda una parola e una stringa di lettere e verificarne la presenza all'interno della parola
#2: Scrivere una funzione di nome 'evita' che richieda una stringa di lettere e poi stampare il numero di parole che non ne contengono alcuna
def evitaConParola(vietate, parola):
    verificato = True
    for lettera in parola:
        for i in vietate:
            if lettera == i:
                verificato = False
                break
    if verificato:
        print(f"La parola {parola} non contiene alcuna lettera vietata {vietate}")
    elif verificato == False:
        print(f"La parola {parola} contiene le lettere vietate {vietate}")


def evitaConFile(vietate, nomeFile):
    nomeFile = open(nomeFile)
    verificato = True
    contaParolaVerificate = 0
    for riga in nomeFile:
        parola = riga.strip()
        verificato = True
        for lettera in parola:
            for i in vietate:
                if lettera == i:
                    verificato = False
        if(verificato):
            print(parola)
            contaParolaVerificate = contaParolaVerificate + 1
   
    print(f"Le parole che non contengono le lettere {vietate} sono {contaParolaVerificate}")

#per prima funzione
print("Scrivere una funzione di nome 'evita' che richieda una parola e una stringa di lettere e verificarne la presenza all'interno della parola")
lettereVietate = input("Inserisci le lettere vietate: ")
parola = input("Inserisci la parola: ")
print(parola + " " + lettereVietate)
evitaConParola(lettereVietate, parola)

#per seconda funzione
print("Scrivere una funzione di nome 'evita' che richieda una stringa di lettere e poi stampare il numero di parole che non ne contengono alcuna")
wordVietate = input("Inserisci le lettere vietate: ")
evitaConFile(wordVietate, "word.txt")









    
        




