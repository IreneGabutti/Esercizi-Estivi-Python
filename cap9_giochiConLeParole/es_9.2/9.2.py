#___Gabutti Irene___
#Scrivete una funzione di nome niente_e che restituisca True se una data parola non contiene la lettera “e”.

def niente_e(nomeFile):
    file = open(nomeFile)
    verificato = True
    for riga in file:
        parola = riga.strip()
        if 'e' in parola:
            verificato = False
        else:
            verificato = True
        if verificato:
            print(parola)

file = "word.txt"
niente_e(file)







    
        




