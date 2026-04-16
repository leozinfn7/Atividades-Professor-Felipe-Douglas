raio = float(input("Raio: "))
altura = float(input("Altura: "))

area_base = 3.14 * (raio**2)
area_lateral = 2 * 3.14 * raio * altura
area_total = 2 * area_base + area_lateral

print("Área do cilindro:", area_total)
