import pandas as pd
import sys
import os

def clean_excel(file_path):
    print(f"\n--- Processing: {file_path} ---")

    # 1️⃣ Verificar existencia
    if not os.path.exists(file_path):
        print("File does not exist. Skipping.")
        return

    # 2️⃣ Verificar que no esté vacío
    if os.path.getsize(file_path) == 0:
        print("File is empty. Skipping.")
        return

    # 3️⃣ Intentar leer el archivo con engine explícito
    try:
        df = pd.read_excel(file_path, engine="openpyxl")
    except Exception as e:
        print(f"Could not read file. Skipping. Error: {e}")
        return

    # 4️⃣ Validar columnas requeridas
    required_columns = ["SUC", "HC"]
    missing = [col for col in required_columns if col not in df.columns]

    if missing:
        print(f"Missing required columns {missing}. Skipping.")
        return

    # 5️⃣ Mantener solo columnas necesarias
    df_clean = df[["SUC", "HC"]]

    # 6️⃣ Sobrescribir el archivo
    try:
        df_clean.to_excel(file_path, index=False, engine="openpyxl")
        print("File cleaned successfully.")
    except Exception as e:
        print(f"Error writing file: {e}")



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No file path provided.")
        sys.exit(0)

    file_path = sys.argv[1]
    clean_excel(file_path)
