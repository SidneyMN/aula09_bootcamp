import pandas as pd
import os
import glob

from utils_log import log_decorator


# Uma funcao de extract que le e consolida json
@log_decorator
def extrair_dados_e_consolidar(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [ pd.read_json(arquivo) for arquivo in arquivos_json ]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total


# uma funcao que transforma
@log_decorator
def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df_novo = df.copy()
    df_novo["Total"] = df_novo["Quantidade"] * df_novo["Venda"]
    return df_novo


# uma funcao que da load em csv ou parquet
@log_decorator
def carregar_dados(df: pd.DataFrame, formato_saida: list):
    """
    parametro que vai ser ou 'csv' ou 'parquet' ou 'os dois'
    """
    for formato in formato_saida:
        if formato == "csv":
            df.to_csv('dados.csv', index=False)
        if formato == "parquet":
            df.to_parquet('dados.parquet', index=False, engine='fastparquet')

@log_decorator
def pipeline_calcular_kpi_de_vendas_consolidado(pasta: str, formato_de_saida: list):
    df_concatenado = extrair_dados_e_consolidar(pasta)
    df_calculado = calcular_kpi_de_total_de_vendas(df_concatenado)
    carregar_dados(df_calculado, formato_de_saida)

