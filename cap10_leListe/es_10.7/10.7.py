#___Gabutti Irene___
#Scrivete una funzione di nome ha_duplicati che richieda una lista e restituisca
#True se contiene elementi che compaiono più di una volta. Non deve modificare la lista di origine

def ha_duplicati(lista):
    for i in range(len(lista)-1):
        if lista[i] == lista[i+1]:
            return True
    return False

s = input("Inserisci gli elementi della tua lista separati da una virgola\n")
t = s.split(',')

print(ha_duplicati(t))