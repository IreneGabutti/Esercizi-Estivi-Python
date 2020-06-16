#___Gabutti Irene___
#Due parole sono anagrammi se potete ottenerle riordinando le lettere di cui sono
#composte. Scrivete una funzione di nome anagramma che riceva due stringhe e restituisca True se sono anagrammi.

def anagramma(parola1,parola2):
    return sorted(parola1) == sorted(parola2)

print(anagramma("esterno", "ortense"))

