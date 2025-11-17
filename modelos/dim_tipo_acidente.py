# A dimensão Tipo de Acidente consolida a classificação normalizada gerada pelo pipeline.
# Essa dim é crítica porque reduz >300 descrições textuais para um conjunto curto e confiável.
# A normalização protege o DW contra ruídos, grafias e inconsistências entre concessionárias.


import pandas as pd

def create_dim_tipo_acidente(df):
    dim = (
        df[["tipo_de_acidente_norm"]]
        .drop_duplicates()
        .rename(columns={"tipo_de_acidente_norm": "categoria"})
        .reset_index(drop=True)
    )
    dim["sk_tipo_acidente"] = dim.index + 1
    return dim
