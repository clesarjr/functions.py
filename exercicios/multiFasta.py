#exercicio

arquivo = open("MultiFasta")

linhas = arquivo.readlines()
#dicionário
fastas = {}

for linha in linhas:

    if linha[0] == ">":
        seqAtual = linha[1:].strip()
        fastas[seqAtual] = ""
    else:
        fastas[seqAtual] = fastas[seqAtual] + linha.strip()

print(fastas) 


