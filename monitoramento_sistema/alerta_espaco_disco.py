import psutil

limite = float(input("Digite o limite mínimo de espaço livre (%): "))

print("===== PARTIÇÕES CRÍTICAS =====")

for particao in psutil.disk_partitions():
    try:
        uso = psutil.disk_usage(particao.mountpoint)
        livre_percentual = 100 - uso.percent

        if livre_percentual < limite:
            livre_gb = uso.free / (1024 ** 3)
            print("-" * 50)
            print(f"Dispositivo: {particao.device}")
            print(f"Montagem: {particao.mountpoint}")
            print(f"Espaço livre: {livre_percentual:.2f}%")
            print(f"Livre em GB: {livre_gb:.2f} GB")
    except PermissionError:
        pass