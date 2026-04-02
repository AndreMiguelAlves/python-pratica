def faturacao(lista):
    total = 0
    # 1. Somar todos os elementos
    for valor in lista:
        total += valor

    # 2. Calcular a média arredondada
    media = round(total / len(lista), 2)
    
    # 3. Encontrar o valor máximo vendido
    maior_valor = max(lista)

    # 4. Devolver a "encomenda" com os 3 resultados na ordem certa
    return total, media, maior_valor

# Dados de teste
vendas = [1.20, 1.10, 1.50]

# Capturar os 3 resultados em 3 variáveis distintas
vendas_totais, media_total, valor_maximo = faturacao(vendas) 

# Apresentação final ao utilizador
print(f"As vendas totais do dia foram: {vendas_totais:.2f}€")   #:.2f  = arredondar 2 casas décimais
print(f"A média de gasto por cliente foi: {media_total:.2f}€")
print(f"A maior venda individual foi: {valor_maximo:.2f}€")