#filter
#função que filtra elementos de uma lista, com base em outra função definida

def pares(x):
    if(x % 2 == 0):
        return x

def impares(x):
    if(x % 2 != 0):
        return x

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

listaPar = filter(pares, lista)
listaImpar = filter(impares, lista)

print(list(listaPar))
print(list(listaImpar))