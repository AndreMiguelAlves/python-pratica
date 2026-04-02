estacoes = [
    {"nome": "Marquês", "linha": "amarela"},
    {"nome": "Alameda", "linha": "verde"},
    {"nome": "Saldanha", "linha": "azul"},
]

def pesquisar_estacao(lista, nome):
    for estacao in lista:
        if estacao["nome"] == nome:
            print(f"A Estação {nome} é a linha {estacao['linha']}")
            break
    else:
        print(f"A estação {nome} não está na lista")

nome = input("Qual a estação? ")
pesquisar_estacao(estacoes, nome)