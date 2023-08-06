import patoolib
import os

rar_files = ["Combustíveis Automotivos-2004-a-2022-1.rar", "Combustíveis Automotivos-2004-a-2022-2.rar"]

try:
    for rar_file in rar_files:
        patoolib.extract_archive(rar_file)

    # Depois de descompactar todos os arquivos RAR, agora você pode procurar os arquivos CSV
    csv_files = [file for file in os.listdir() if file.endswith(".csv")]

except Exception as e:
    print("Erro ao ler os arquivos:", e)
