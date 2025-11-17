"""
===============================================================================
TRANSFORM MODULE — Pipeline de Acidentes ANTT
-------------------------------------------------------------------------------

Este módulo implementa a etapa de **Transformação (T)** do pipeline ETL.

Responsabilidades principais:
- Padronização dos nomes das colunas (snake_case, ASCII, sem acentos).
- Conversão segura de datas e horários, criando o campo referencial `data_hora`.
- Normalização textual dos tipos de acidentes, incluindo:
    ✓ Correção de resíduos/truncamentos oriundos dos CSVs da ANTT.
    ✓ Classificação granular por meio do algoritmo de categorização.
- Construção de um conjunto de dados limpo, consistente e pronto
  para a modelagem dimensional (fato e dimensões).

===============================================================================
"""



import pandas as pd
from utils.helpers import (
    normalize_columns,
    corrigir_residuos,
    normalizar_tipo_acidente
)

def transform_acidentes(df):

    df = normalize_columns(df)

    
    df["data"] = pd.to_datetime(df["data"], format="%d/%m/%Y", errors="coerce")

    df["horario"] = df["horario"].astype(str).str.strip()
    df["horario"] = pd.to_datetime(
        df["horario"], format="%H:%M:%S", errors="coerce"
    ).dt.time
    df["data_hora"] = pd.to_datetime(
        df["data"].dt.strftime("%Y-%m-%d") + " " + df["horario"].astype(str),
        errors="coerce"
    )
    df = df.dropna(subset=["data_hora"])

 
    df["tipo_de_acidente"] = (
        df["tipo_de_acidente"]
        .astype(str)
        .apply(corrigir_residuos)  
    )

    df["tipo_de_acidente_norm"] = df["tipo_de_acidente"].apply(
        normalizar_tipo_acidente  
    )

    return df
