import psutil
import os

try:
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        uso_nucleos = psutil.cpu_percent(interval=1, percpu=True)
        uso_total = sum(uso_nucleos) / len(uso_nucleos)

        print("===== MONITOR DE CPU =====")
        print(f"CPU Total: {uso_total:.2f}%")

        for i, uso in enumerate(uso_nucleos):
            print(f"Núcleo {i}: {uso}%")

except KeyboardInterrupt:
    print("\nMonitor encerrado.")