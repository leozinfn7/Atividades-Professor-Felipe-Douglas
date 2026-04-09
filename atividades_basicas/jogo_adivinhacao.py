import random

numero_secreto = random.randint(1, 100)
tentativas = 0

print("Tente adivinhar o número entre 1 e 100.")

while True:
    chute = int(input("Digite seu palpite: "))
    tentativas += 1

    if chute == numero_secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativa(s).")
        break
    elif chute < numero_secreto:
        print("O número secreto é maior.")
    else:
        print("O número secreto é menor.")