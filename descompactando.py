import os
import patoolib
import pandas as pd
from tqdm.auto import tqdm

def descompactando():
    Diretorio_local = "C:/Users/jacks/OneDrive/Projetos/combustiveis_automotivos"
    rar_file = f"{Diretorio_local}/Combustíveis Automotivos-2012-a-2022.rar"

    dest_dir = f"{Diretorio_local}/arquivos-extraidos/"

    if not os.path.isfile(rar_file):
        print(f"Arquivo não encontrado: {rar_file}")
    else:
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        patoolib.extract_archive(rar_file, outdir=dest_dir)

        csv_files = [file for file in os.listdir(dest_dir) if file.endswith(".csv")]

        csv_paths = [os.path.join(dest_dir, file) for file in csv_files]

        print(f"{len(csv_files)} arquivos CSV extraídos e listados:")
        print(csv_paths)

    dataframes = []

    encodings = ['utf-8', 'ISO-8859-1', 'latin-1']

    for csv_path in tqdm(csv_paths, desc="Lendo e processando arquivos CSV"):
        try:
            df = None
            for encoding in encodings:
                try:
                    df = pd.read_csv(csv_path, sep=';', encoding=encoding, parse_dates=['Data da Coleta'])
                    break
                except Exception as e:
                    print(f"Tentando codificação {encoding} para o arquivo {csv_path} - Erro: {e}")

            if df is None:
                print(f"Não foi possível ler o arquivo {csv_path} com as codificações disponíveis.")
                continue

            df = df.drop([
                'Revenda', 'CNPJ da Revenda', 'Nome da Rua', 'Numero Rua',
                'Complemento', 'Bairro', 'Cep', 'Valor de Compra'
            ], axis=1)

            df = df.dropna(axis=0)

            df['Unidade de Medida'] = df['Unidade de Medida'].str.replace('R$', '').str.replace('/', '').str.replace(' ', '')
            df['Unidade de Medida'] = df['Unidade de Medida'].str.replace('litro', 'Litro')

            df['Valor de Venda'] = df['Valor de Venda'].str.replace(',', '.').astype(float)

            formato_data = '%d/%m/%Y'
            df['Data da Coleta'] = pd.to_datetime(df['Data da Coleta'], format=formato_data)

            dataframes.append(df)

        except Exception as e:
            print(f"Erro ao ler e processar arquivo {csv_path}: {e}")

    combustiveis_automotivos_df = pd.concat(dataframes, ignore_index=True)
    combustiveis_automotivos_df.to_csv(f"{Diretorio_local}/combustiveis.csv", index=False, encoding='utf-8')

