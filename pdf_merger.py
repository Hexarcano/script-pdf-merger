from pypdf import PdfWriter
import glob
import os
import re

def sanitizar(cadena, fallback="grupo"):
    result = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", cadena).strip(" .")
    if not result or result.upper() in {"CON","PRN","AUX","NUL","COM1","COM2","COM3",
        "COM4","COM5","COM6","COM7","COM8","COM9","LPT1","LPT2","LPT3","LPT4",
        "LPT5","LPT6","LPT7","LPT8","LPT9"}:
        return fallback
    return result

nombre = sanitizar(input("Nombre para cada archivo. Default: grupo-<indice>: "), "grupo")
final_dir = sanitizar(input("Nombre para el directorio final. Default: merged: "), "merged")

items = [p for p in glob.glob("**/*.pdf") if os.path.normpath(final_dir) not in os.path.normpath(p).split(os.sep)]

if (len(items) < 10):
    print("No hay elementos suficientes para separar en 5 grupos")
    exit()

items_per_section = len(items) // 5
fragments = [items[i:i + items_per_section] for i in range(0, len(items), items_per_section)]

os.makedirs(f"{final_dir}/", exist_ok=True)

for index, fragment in enumerate(fragments):
    merger = PdfWriter()
    for item in fragment:
        merger.append(item)
    merger.write(f"{final_dir}/{nombre}-{index}.pdf")
