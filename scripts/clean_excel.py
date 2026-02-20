import pandas as pd
import sys

# Ruta del archivo que se pasa como argumento
file_path = sys.argv[1]

# Leer archivo
df = pd.read_excel(file_path)

# Validar que existan las columnas necesarias
required_columns = ["SUC", "HC"]

missing = [col for col in required_columns if col not in df.columns]

if missing:
    raise ValueError(f"Faltan columnas requeridas: {missing}")

# Seleccionar solo columnas deseadas
df_clean = df[["SUC", "HC"]]

# Sobrescribir el mismo archivo
df_clean.to_excel(file_path, index=False)

print("Archivo limpiado correctamente.")
