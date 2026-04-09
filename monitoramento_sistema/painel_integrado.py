import psutil
import time
import os

print("Painel integrado iniciado... Ctrl+C para sair.")

try:
    rede_anterior = psutil.net_io_counters()

    while True:
        os.system("cls" if os.name == "nt" else "clear")

        memoria = psutil.virtual_memory()
        cpu = psutil.cpu_percent(interval=1)

        particao_principal = psutil.disk_partitions()[0]
        disco = psutil.disk_usage(particao_principal.mountpoint)

        rede_atual = psutil.net_io_counters()
        download = (rede_atual.bytes_recv - rede_anterior.bytes_recv) / 1024
        upload = (rede_atual.bytes_sent - rede_anterior.bytes_sent) / 1024
        rede_anterior = rede_atual

        print("========== PAINEL DE MONITORAMENTO ==========")
        print(f"RAM usada: {memoria.percent}% ({memoria.used / (1024 ** 2):.2f} MB)")
        print(f"CPU total: {cpu}%")
        print(f"Espaço livre ({particao_principal.mountpoint}): {disco.free / (1024 ** 3):.2f} GB")
        print(f"Download: {download:.2f} kB/s")
        print(f"Upload: {upload:.2f} kB/s")
        print("=============================================")

        time.sleep(1)

except KeyboardInterrupt:
    print("\nPainel encerrado.")