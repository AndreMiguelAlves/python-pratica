import random

secreto = random.randint(1, 10)
tentativas = 3
lista_num = []

print("---Jogo de adivinhação---")

while tentativas > 0:
    guess = int(input("Adivinha o número de 1 a 10: "))
    
    
    if guess < 1 or guess > 10:
        print("Erro! Escolhe um número entre 1 e 10.")
        continue

    
    if guess in lista_num:
        print(f"Atenção! Já tentaste o {guess}. Não gastes tentativas!")
        continue 

    
    lista_num.append(guess)

   
    if guess == secreto:
        print("Parabéns. Acertaste!")
        break

    
    tentativas -= 1
    
    if tentativas == 0:
        print(f"Perdeste. O número era o {secreto}")
    elif guess < secreto:       
        print(f"O número secreto é MAIOR. Tens {tentativas} tentativas")
    else: 
        print(f"O número secreto é MENOR. Tens {tentativas} tentativas")

print(f"Os teus palpites foram: {lista_num}")