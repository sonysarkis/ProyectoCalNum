# Archivo: require.py

import os

# Lista de paquetes a instalar
packages = [
    "numpy",
    "scipy",
    "sympy",
    "pandas",
    "matplotlib"
]

# Iterar sobre la lista de paquetes e instalar cada uno
for package in packages:
    os.system(f"pip install {package}")
