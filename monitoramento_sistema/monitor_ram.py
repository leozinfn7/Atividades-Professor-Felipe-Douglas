import psutil
import time
import os

while True:
    os.system("cls" if os.name == "nt" else "clear")

    memoria = psutil.virtual_memory()

    total_mb = memoria.total / (1024 ** 2)
    usada_mb = memoria.used / (1024 ** 2)
    livre_mb = memoria.available / (1024 ** 2)

    print("===== MONITOR DE MEMÓRIA RAM =====")
    print(f"RAM Total: {total_mb:.2f} MB")
    print(f"RAM Usada: {usada_mb:.2f} MB")
    print(f"RAM Livre: {livre_mb:.2f} MB")
    print(f"Uso de RAM: {memoria.percent}%")

    time.sleep(2)