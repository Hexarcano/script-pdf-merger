from pypdf import PdfWriter
from pathlib import Path
from collections import defaultdict
import glob
import os
import re

directorios_pdf = defaultdict(list)

def sanitizar(cadena, fallback="grupo"):
    result = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", cadena).strip(" .")
    if not result or result.upper() in {"CON","PRN","AUX","NUL","COM1","COM2","COM3",
        "COM4","COM5","COM6","COM7","COM8","COM9","LPT1","LPT2","LPT3","LPT4",
        "LPT5","LPT6","LPT7","LPT8","LPT9"}:
        return fallback
    return result

for p in glob.glob("**/*.pdf", recursive=True):
    path = Path(p)
    dir_name = str(path.parent)
    directorios_pdf[dir_name].append(str(path))

final_dir = "final"
os.makedirs(f"{final_dir}/", exist_ok=True)

for directorio, archivos in directorios_pdf.items():
    nombre = directorio + "_2026"
    merger = PdfWriter()
    for item in archivos:
        merger.append(item)

    merger.write(f"{final_dir}/{nombre}.pdf")