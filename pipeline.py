from etl import pipeline_calcular_kpi_de_vendas_consolidado

pasta_arquivos = 'data'
formato_de_saida: list = ['csv', 'parquet']

pipeline_calcular_kpi_de_vendas_consolidado(pasta_arquivos, formato_de_saida)

