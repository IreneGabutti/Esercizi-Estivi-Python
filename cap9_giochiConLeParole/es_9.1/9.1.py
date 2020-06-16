#___Gabutti Irene___
#Scrivete un programma che legga il file words.txt 
#e stampi solo le parole composte da più di 20 caratteri (caratteri spaziatori esclusi)


lenghtMax = 20

file = open("word.txt")

for riga in file:
    parola = riga.strip()
    if len(parola) >= lenghtMax:
        print(parola)


