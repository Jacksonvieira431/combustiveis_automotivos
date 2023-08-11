import pandas as pd
import random


def gerar_amostra(porcentagem):
    Diretorio_local = "C:/Users/jacks/OneDrive/Projetos/combustiveis_automotivos"
    arquivo_csv = f"{Diretorio_local}/combustiveis.csv"

    resultado_percent = float(porcentagem) / 100.0

    encodings_to_try = ["utf-8", "latin-1", "ISO-8859-1"]
    combustiveis_automotivos_df = None  # Inicializa a variável

    for encoding in encodings_to_try:
        try:
            combustiveis_automotivos_df = pd.read_csv(arquivo_csv, encoding=encoding)
            break  # Sair do loop se o encoding funcionar
        except UnicodeDecodeError:
            pass

    if combustiveis_automotivos_df is None:
        raise ValueError("Não foi possível ler o arquivo CSV com nenhum dos encodings.")

    random.seed(42)
    sample_size = int(len(combustiveis_automotivos_df) * resultado_percent)
    reduced_df = combustiveis_automotivos_df.sample(n=sample_size)

    return reduced_df.to_csv(index=False)
