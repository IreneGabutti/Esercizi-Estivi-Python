#___Gabutti Irene___
#Applicate la memoizzazione alla funzione di Ackermann dell’Esercizio 6.2 e provate
#a vedere se questa tecnica rende possibile il calcolo della funzione con argomenti più grandi


memoria = {}

def ackermann(m, n):

    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)

    if (m, n) in memoria:
        return memoria[m, n]
    else:
        memoria[m, n] = ackermann(m-1, ackermann(m, n-1))
        return memoria[m, n]


print(ackermann(3, 4))
print(ackermann(3, 6))