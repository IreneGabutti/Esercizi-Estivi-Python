#___Gabutti Irene___
#Leggete la documentazione del metodo dei dizionari setdefault e usatelo per
#scrivere una versione più concisa di inverti_diz.


def invert_dict(d):
    
    inverse = {}
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)
    return inverse


if __name__ == '__main__':
    d = dict(a=1, b=2, c=3, z=1)
    inverse = invert_dict(d)
    for val in inverse:
        keys = inverse[val]
        print(val, keys)