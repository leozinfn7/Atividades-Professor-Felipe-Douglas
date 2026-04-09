import psutil

particoes = psutil.disk_partitions()

print("===== DISPOSITIVOS DE ARMAZENAMENTO =====")

for i, particao in enumerate(particoes):
    print(f"{i} - {particao.device} | {particao.mountpoint}")

indice = int(input("Escolha o número de uma partição: "))

if 0 <= indice < len(particoes):
    particao = particoes[indice]

    try:
        uso = psutil.disk_usage(particao.mountpoint)

        print("\n===== DETALHES DA PARTIÇÃO =====")
        print(f"Dispositivo: {particao.device}")
        print(f"Ponto de montagem: {particao.mountpoint}")
        print(f"Sistema de arquivos: {particao.fstype}")
        print(f"Total: {uso.total / (1024 ** 3):.2f} GB")
        print(f"Usado: {uso.used / (1024 ** 3):.2f} GB")
        print(f"Livre: {uso.free / (1024 ** 3):.2f} GB")
        print(f"Uso: {uso.percent}%")
    except PermissionError:
        print("Sem permissão para acessar essa partição.")
else:
    print("Índice inválido.")

# Exemplos de outros dispositivos de entrada/saída:
# teclado, mouse, monitor, impressora, scanner, webcam, microfone.