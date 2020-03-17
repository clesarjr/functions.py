#exercicio

nomeArq = input("Digite o nome do arquivo que você deseja abrir: ")
arquivo = open(nomeArq)

linhas = arquivo.readlines()

for linha in linhas:
    print(linha.strip())

arquivo.close