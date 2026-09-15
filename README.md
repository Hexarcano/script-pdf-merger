# Script para unir archivos PDF

Este script de python sirve para unir distintos archivos en formato PDF en uno sólo.

Se recomienda crear un entorno virtual de Python

```python -m venv .venv```

Desde terminal ir a ./.venv/Scripts/ y ejecutar el scipt adecuado al sistema operativo y herramienta

## Consideraciones

No se considera el funcionamiento correcto con versiones de Python inferiores a las siguientes.

- Python 3.14.7 o superior
- pip 26.2.1

No se considera el funcionamiento correcto con versiones inferiores de las siguientes librerías.

- pypdf-6.18.1 
- cryptography

## Instalación de paquetes

Los paquetes en se instalan con [pip](www.https://pypi.org/project/pip/) (gestor de paquetes por defecto) o [uv](https://docs.astral.sh/uv/) (inslatación aparte)

```pip install <paquete>```

### Ejemplo:

- ```pip install pypdf```

- ```pip install cryptography```

## Ejecutar 

Ejecutar el comando

```py ./pdf_merger.py```
