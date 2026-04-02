linhas = ["701", "736", "750", "783", "794"]

def linhas_ordenadas(lista):
    lista.sort()
    for linha in lista:
        print(linha)

def linhas_procura(lista,nome):
    if nome in lista:
        print(f"A linha {nome} está na lista")
    else:
        print(f"A linha {nome} não está na lista")

linhas_ordenadas(linhas)

nome = input("Qual a linha pretendida? ")

linhas_procura(linhas,nome)