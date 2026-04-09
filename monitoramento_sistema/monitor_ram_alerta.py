import psutil
import time
import os

limite = float(input("Digite o limite de uso da RAM (%): "))

try:
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        memoria = psutil.virtual_memory()
        usada_mb = memoria.used / (1024 ** 2)
        livre_mb = memoria.available / (1024 ** 2)

        print("===== MONITOR DE RAM COM ALERTA =====")
        print(f"Uso atual: {memoria.percent}%")
        print(f"RAM usada: {usada_mb:.2f} MB")
        print(f"RAM livre: {livre_mb:.2f} MB")

        if memoria.percent > limite:
            print("ALERTA: uso de RAM acima do limite!")

        time.sleep(2)

except KeyboardInterrupt:
    print("\nMonitor encerrado pelo usuário.")