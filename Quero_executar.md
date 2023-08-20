# Configurando e Executando o Projeto

## Passo 1: Clonar o Repositório

Antes de tudo, clone o repositório em seu computador utilizando o seguinte comando: git clone "url"

## Passo 2: Preparar o Ambiente

1. Instale o Python em sua máquina (minha versão foi a 3.11.4).
2. Instale o Virtualenv no prompt: pip install virtualenv

3. Crie um ambiente virtual dentro da pasta do repositório: python3 -m venv venv

4. Ative o ambiente virtual: venv\Scripts\activate


## Passo 3: Instalar Pacotes do Projeto

Dentro da pasta do repositório, abra o prompt e execute: pip install -r requirements.txt


## Passo 4: Configurar o Diretório Local

1. Acesse o arquivo `funções/diretorio_local.py`.
2. Encontre a declaração da variável `diretorio_local`.
3. Insira o caminho completo para o diretório do repositório entre os parênteses com barras "/".

## Passo 5: Executar os Notebooks

- Abra cada um dos 4 arquivos `.ipynb` (notebooks) sequencialmente.
- Execute as células de código em ordem.

## Resultados e Arquivos Gerados

Ao longo das execuções, diversos arquivos serão gerados em pastas específicas:

- Tabelas
- Gráficos_Seres_Temporais
- Gráficos_salvos
- Arquivos-extraidos
- Gráficos_Machine_Learning

Além disso, um arquivo completo chamado "combustiveis.csv" será gerado.

Agora você está pronto para explorar o projeto. Boa leitura!