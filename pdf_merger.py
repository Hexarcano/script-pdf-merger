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

nombre = sanitizar(input("Nombre para cada archivo. Default: grupo: "), "grupo")
final_dir = sanitizar(input("Nombre para el directorio final. Default: merged: "), "merged")

items = [p for p in glob.glob("*.pdf")]

os.makedirs(f"{final_dir}/", exist_ok=True)

merger = PdfWriter()

for item in items:
    merger.append(item)

merger.write(f"{final_dir}/{nombre}.pdf")