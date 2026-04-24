#Objetivo:  Código que faz a consolidação de todos os arquivos ".xlsx" dentro de uma pasta e os consolida em um CSV
#Descrição: Código feito usando apenas o Pandas e fazendo uma consolidação completa para dentro de um único arquivo
#Falhas:    Por conta de fazer tudo sem a utilização do DuckDB por exemplo, faz com que
#           não tenha como validar caso o passado tenha sido alterado, apenas descobrindo a inclusão de novos arquivos

import os #Usado para entrar dentro da pasta principal
import pandas as pd #Usado para fazer a criação dos DataFrames
from dotenv import load_dotenv #Usado para carregar as variáveis de ambiente
load_dotenv() #Carrega as variáveis de ambiente
PASTA_ORIGEM  = os.getenv("PASTA_ORIGEM")   # Pasta com os arquivos .xlsx
ARQUIVO_SAIDA = os.getenv("ARQUIVO_SAIDA")  # Caminho do CSV consolidado


lista_dfs = [] #Lista vazia usada para armazenar todos os DF's que forem criados

#Loop feito para criar cada DF's e armazenar dentro da Lista
for (caminho, pasta, arquivos) in os.walk(PASTA_ORIGEM):
    for nome_arq in arquivos:
        if nome_arq.endswith('.xlsx'):
            path = os.path.join(caminho, nome_arq) #Cria o caminho completo do arquivo
            df = pd.read_excel(path) #Cria um DataFrame com o arquivo encontrado, caso seja um ".xlsx"
            lista_dfs.append(df) #Adiciona o DataFrame criado na Lista de DF's

full = pd.concat(lista_dfs) #Faz a concatenação de todas as DF's criadas
df_full = pd.DataFrame(full) #Cria um DataFrame com todas as DF's
df_full.to_csv(ARQUIVO_SAIDA,index=False) #Lança o CSV convertido

print(f'✅ Consolidado com sucesso! {len(lista_dfs)} arquivo(s) processado(s).')