import patoolib
import os
from tqdm.auto import tqdm

# O diretório onde os arquivos do repositório clonado estão
Diretorio_local = "C:/Users/jacks/OneDrive/Projetos/combustiveis_automotivos"

dest_dir = f"{Diretorio_local}/arquivos-extraidos/"

rar_files = [f"{Diretorio_local}/Combustíveis Automotivos-2012-a-2022.rar"]

for rar_file in rar_files:
    if not os.path.isfile(rar_file):
        print(f"Arquivo não encontrado: {rar_file}")

try:
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for rar_file in tqdm(rar_files, desc="Extraindo arquivos"):
        patoolib.extract_archive(rar_file, outdir=dest_dir)

    csv_files = [file for file in os.listdir(dest_dir) if file.endswith(".csv")]

except Exception as e:
    print("Erro ao ler os arquivos:", e)
