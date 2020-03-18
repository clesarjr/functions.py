#map
#realiza uma operação com vários valores

def potenciacao(x):
    return x**2

listaValor = [1, 2, 4, 7, 9, 15]

listaPotencia = map(potenciacao, listaValor)

for x in listaPotencia:
    print(x)