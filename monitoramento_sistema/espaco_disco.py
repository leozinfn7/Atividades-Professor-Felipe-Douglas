import psutil

print("===== PARTIÇÕES DO DISCO =====")

for particao in psutil.disk_partitions():
    try:
        uso = psutil.disk_usage(particao.mountpoint)

        total_gb = uso.total / (1024 ** 3)
        usado_gb = uso.used / (1024 ** 3)
        livre_gb = uso.free / (1024 ** 3)

        print("-" * 50)
        print(f"Dispositivo: {particao.device}")
        print(f"Ponto de montagem: {particao.mountpoint}")
        print(f"Total: {total_gb:.2f} GB")
        print(f"Usado: {usado_gb:.2f} GB")
        print(f"Livre: {livre_gb:.2f} GB")
        print(f"Porcentagem usada: {uso.percent}%")
    except PermissionError:
        print(f"Sem permissão para acessar: {particao.mountpoint}")