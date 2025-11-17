# A dimensão Concessionária é derivada do nome dos arquivos.
# Essa abordagem mantém rastreabilidade por operador e evita dependência
# de informações inconsistentes dentro dos CSVs.



import pandas as pd

def create_dim_concessionaria(df):
    
    dim = df[["concessionaria"]].drop_duplicates().copy()

  
    dim["id_concessionaria"] = dim.reset_index().index + 1

    return dim
