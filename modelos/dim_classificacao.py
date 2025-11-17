# A dimensão Classificação associa (tipo_de_ocorrencia + tipo_de_acidente)
# ao surrogate key sk_classificacao.
# Isso desacopla o fato da variação textual e normaliza categorias que podem mudar
# ao longo dos anos ou entre concessionárias diferentes.
# Mantemos combinação única para garantir que dois tipos iguais não
# sejam contabilizados como categorias distintas.

import pandas as pd

def create_dim_classificacao(df):
    dim = (
        df[["tipo_de_ocorrencia", "tipo_de_acidente_norm"]]
        .drop_duplicates()
        .rename(columns={"tipo_de_acidente_norm": "tipo_de_acidente"})
        .reset_index(drop=True)
    )

    dim["sk_classificacao"] = dim.index + 1
    return dim



def create_dim_classificacao(df):
    dim = (
        df[["tipo_de_ocorrencia", "tipo_de_acidente"]]
        .drop_duplicates()
        .reset_index(drop=True)
    )
    dim["sk_classificacao"] = dim.index + 1
    return dim
