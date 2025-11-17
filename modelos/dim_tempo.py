# A dimensão Tempo é criada de forma derivada (não depende do fornecedor dos dados).
# Isso garante consistência temporal, elimina ambiguidade entre formatações
# e permite granularização (hora, dia, mês, trimestre) para análises históricas.

def create_dim_tempo(df):
    dim = (
        df[["data_hora"]]
        .dropna()
        .drop_duplicates()
        .assign(
            data=lambda x: x["data_hora"].dt.date,
            hora=lambda x: x["data_hora"].dt.hour,
            minuto=lambda x: x["data_hora"].dt.minute,
            ano=lambda x: x["data_hora"].dt.year,
            mes=lambda x: x["data_hora"].dt.month,
            dia=lambda x: x["data_hora"].dt.day,
            dia_semana=lambda x: x["data_hora"].dt.day_name(),
            trimestre=lambda x: x["data_hora"].dt.quarter
        )
    )

    dim["sk_tempo"] = dim.reset_index().index + 1
    return dim
