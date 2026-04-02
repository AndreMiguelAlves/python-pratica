import random

secreto = random.randint(1, 10)
tentativas = 3
lista_num = []

print("---Jogo de adivinhação---")

while tentativas > 0:
    guess = int(input("Adivinha o número de 1 a 10: "))
    
    # FILTRO 1: O número está no intervalo correto?
    if guess < 1 or guess > 10:
        print("Erro! Escolhe um número entre 1 e 10.")
        continue

    # 1. VERIFICAR SE É REPETIDO
    if guess in lista_num:
        print(f"Atenção! Já tentaste o {guess}. Não gastes tentativas!")
        continue # O 'continue' faz o robô saltar para o início do while sem ler o resto!

    # 2. SE NÃO FOR REPETIDO, GUARDAMOS NA LISTA
    lista_num.append(guess)

    # 3. VERIFICAR SE ACERTOU
    if guess == secreto:
        print("Parabéns. Acertaste!")
        break

    # 4. TIRAR VIDA E DAR PISTAS
    tentativas -= 1
    
    if tentativas == 0:
        print(f"Perdeste. O número era o {secreto}")
    elif guess < secreto:       
        print(f"O número secreto é MAIOR. Tens {tentativas} tentativas")
    else: 
        print(f"O número secreto é MENOR. Tens {tentativas} tentativas")

print(f"Os teus palpites foram: {lista_num}")