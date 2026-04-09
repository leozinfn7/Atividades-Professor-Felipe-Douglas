import psutil
import time
import os

print("Monitorando rede... Pressione Ctrl+C para sair.")

try:
    io_anterior = psutil.net_io_counters()

    while True:
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")

        io_atual = psutil.net_io_counters()

        download = io_atual.bytes_recv - io_anterior.bytes_recv
        upload = io_atual.bytes_sent - io_anterior.bytes_sent

        print("===== TRÁFEGO DE REDE =====")
        print(f"Download: {download / 1024:.2f} kB/s")
        print(f"Upload: {upload / 1024:.2f} kB/s")

        io_anterior = io_atual

except KeyboardInterrupt:
    print("\nMonitor encerrado.")