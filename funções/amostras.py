import pandas as pd
import random


def gerar_amostra(tamanho_amostra: int):
    Diretorio_local = "C:/Users/jacks/OneDrive/Projetos/combustiveis_automotivos"
    arquivo_csv = f"{Diretorio_local}/combustiveis.csv"

    percent = tamanho_amostra / 100

    encodings_to_try = ["utf-8", "latin-1", "ISO-8859-1"]
    combustiveis_automotivos_df = None

    for encoding in encodings_to_try:
        try:
            combustiveis_automotivos_df = pd.read_csv(arquivo_csv, encoding=encoding)
            break
        except UnicodeDecodeError:
            pass

    if combustiveis_automotivos_df is None:
        raise ValueError("Não foi possível ler o arquivo CSV com nenhum dos encodings.")
    
    random.seed(42)
    sample_size = int(len(combustiveis_automotivos_df) * percent)
    reduced_df = combustiveis_automotivos_df.sample(
        n=sample_size,
    )

    reduced_df['Data da Coleta'] = pd.to_datetime(reduced_df['Data da Coleta'], format='%d/%m/%Y')
    reduced_df = reduced_df.set_index("Data da Coleta")

    return reduced_df
