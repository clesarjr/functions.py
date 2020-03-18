#reduce
#trabalha com uma lista retornando apenas um valor da mesma

from functools import reduce

def soma(x, y):
    return x+y

lista = [1, 3, 5, 7, 9]

soma = reduce(soma, lista)

print(soma)


