prestacao = float(input("Valor da prestação: "))
taxa = float(input("Taxa (%): "))
dias = int(input("Dias de atraso: "))

nova = prestacao + (prestacao * taxa * dias) / 100
print("Nova prestação:", nova)
