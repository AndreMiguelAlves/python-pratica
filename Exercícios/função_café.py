def faturacao(lista):
    total = 0
    
    for valor in lista:
        total += valor

    
    media = round(total / len(lista), 2)
    
    
    maior_valor = max(lista)

    
    return total, media, maior_valor


vendas = [1.20, 1.10, 1.50]


vendas_totais, media_total, valor_maximo = faturacao(vendas) 


print(f"As vendas totais do dia foram: {vendas_totais:.2f}€")   
print(f"A média de gasto por cliente foi: {media_total:.2f}€")
print(f"A maior venda individual foi: {valor_maximo:.2f}€")