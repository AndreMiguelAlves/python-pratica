precos = {"pastel": 1.50, "água": 1.00, "café": 1.20, "bolo": 2.90}
nomes_comprados = []
precos_comprados = []

def calcular_media(lista):
    if len(lista) == 0: return 0
    return sum(lista) / len(lista)

while True:
    nome = input("Produto (ou 'sair'): ").lower().strip()
    
    if nome == "sair":
        break
        
    if nome in precos:
        
        nomes_comprados.append(nome)
        
        precos_comprados.append(precos[nome])
        print(f"{nome.capitalize()} adicionado!")
    else:
        print("Não temos esse produto.")


if len(nomes_comprados) > 0:
    print("\n---------- RECIBO ----------")
    #
    for n in nomes_comprados:
        print(f"Produto: {n.capitalize()}")
    
    print("----------------------------")
    total = sum(precos_comprados)
    media = calcular_media(precos_comprados)
    
    print(f"TOTAL: {total:.2f}€")
    print(f"MÉDIA POR PRODUTO: {media:.2f}€")
else:
    print("Nenhuma compra efetuada.")
