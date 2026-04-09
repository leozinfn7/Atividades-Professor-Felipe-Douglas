import psutil
import platform

try:
    import cpuinfo
except ImportError:
    cpuinfo = None

print("===== INFORMAÇÕES DO PROCESSADOR =====")

print(f"Sistema: {platform.system()} {platform.release()}")
print(f"Arquitetura: {platform.machine()}")
print(f"Núcleos físicos: {psutil.cpu_count(logical=False)}")
print(f"Núcleos lógicos: {psutil.cpu_count(logical=True)}")

freq = psutil.cpu_freq()
if freq:
    print(f"Frequência atual: {freq.current:.2f} MHz")
    print(f"Frequência mínima: {freq.min:.2f} MHz")
    print(f"Frequência máxima: {freq.max:.2f} MHz")

if cpuinfo:
    info = cpuinfo.get_cpu_info()
    print(f"Modelo da CPU: {info.get('brand_raw', 'Não disponível')}")
else:
    print("Modelo da CPU: biblioteca py-cpuinfo não instalada.")

print("Número de série: geralmente não é possível obter de forma portátil pelo Python.")