#lambda
#permite criar um função na linha de código da operação (útil quando a função é utilizada 1x dentro de outra função)

listaValor = [1, 2, 4, 7, 9, 15]

listaPotencia = map(lambda x: x**2, listaValor)

for x in listaPotencia:
    print(x)