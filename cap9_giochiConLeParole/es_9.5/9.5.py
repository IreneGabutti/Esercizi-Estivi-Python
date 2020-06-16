#___Gabutti Irene___
#Scrivete una funzione di nome usa_tutte che richieda una parola e una stringa di
#lettere richieste e che restituisca True se la parola utilizza tutte le lettere richieste almeno una volta.

#UGUALE A QUELLO PRECEDENTE

def usa_tutte(lettere, parola):
    verificato = True

    for lettera in parola:
        if lettera not in lettere:
            verificato = False
        else:
            verificato = True
        #verificato = True
    if verificato:
        print(f"La parola {parola} contiene tutte le lettere {lettere}")
    elif verificato == False:
        print(f"La parola {parola} non contiene tutte le lettere {lettere}")


lettere = input("Inserisci una stringa di lettere: ")
parola = input("Inserisci la parola: ")
print(parola + " " + lettere)
usa_tutte(lettere, parola)











    
        




