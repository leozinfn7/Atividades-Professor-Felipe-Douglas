n = int(input("Quantos números você deseja digitar? "))

while n <= 0:
    n = int(input("Digite um valor maior que 0: "))

numeros = []

for _ in range(n):
    valor = float(input("Digite um número: "))
    numeros.append(valor)

print("Maior número:", max(numeros))
print("Menor número:", min(numeros))
print("Média:", sum(numeros) / len(numeros))