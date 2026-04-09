import psutil
import time
from datetime import datetime

print("Registrando uso da CPU em cpu_log.txt... Ctrl+C para sair.")

try:
    while True:
        uso_cpu = psutil.cpu_percent(interval=1)
        agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("cpu_log.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"{agora} - CPU: {uso_cpu}%\n")

        print(f"{agora} - CPU: {uso_cpu}%")
        time.sleep(4)

except KeyboardInterrupt:
    print("\nLogger encerrado.")