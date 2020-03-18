#zip
#trabalha com duas ou mais listas

lista1 = [1, 2, 3, 4]
lista2 = ["mouse", "keydboard", "headset", "CPU"]
lista3 = ["R$ 150,00", "R$ 200,00", "R$ 350,00", "R$ 1500,00"]

for numero, nome, valor in zip(lista1, lista2, lista3):
    print(numero, nome, valor)