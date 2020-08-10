#___Gabutti Irene___
#Se avete svolto l’Esercizio 10.7, avete già una funzione di nome ha_duplicati
# richiede come parametro una lista e restituisce True se ci sono oggetti ripetuti all’interno della lista.



def has_duplicates(t):
    d = {}
    for x in t:
        if x in d:
            return True
        d[x] = True
    return False


def has_duplicates2(t):
    return len(set(t)) < len(t)


if __name__ == '__main__':
    t = [1, 2, 3]
    print(has_duplicates(t))
    t.append(2)
    print(has_duplicates(t))

    t = [1, 2, 3]
    print(has_duplicates2(t))
    t.append(2)
    print(has_duplicates2(t))