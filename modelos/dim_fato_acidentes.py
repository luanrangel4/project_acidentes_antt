# A tabela fato consolida todas as chaves de dimensão mais os indicadores numéricos.
# O modelo segue boas práticas de Data Warehouse:
#   - surrogate keys garantem estabilidade mesmo se o dado original mudar
#   - métrica numérica é mantida no fato para agregações
#   - atributos descritivos permanecem nas dimensões

def create_fato_acidentes(df, dim_tempo, dim_classificacao, dim_conc, dim_tipo):

   
    df = df.merge(
        dim_tipo,
        left_on="tipo_de_acidente_norm",
        right_on="categoria",
        how="left"
    )

    fato = df.merge(
        dim_tempo[["data_hora", "sk_tempo"]],
        on="data_hora", how="left"
    )

    fato = fato.merge(
        dim_classificacao,
        on=["tipo_de_ocorrencia", "tipo_de_acidente"],
        how="left"
    )

    fato = fato.merge(
        dim_conc,
        on="concessionaria",
        how="left"
    )

    dimensoes = [
        "sk_tempo",
        "sk_classificacao",
        "sk_tipo_acidente",
        "id_concessionaria",
        "trecho",
        "sentido",
        "km"
    ]

    metrics = [
        "automovel", "bicicleta", "caminhao", "moto", "onibus", "outros",
        "tracao_animal", "transporte_de_cargas_especiais",
        "trator_maquinas", "utilitarios",
        "ilesos", "levemente_feridos", "moderadamente_feridos",
        "gravemente_feridos", "mortos"
    ]

    selected = [c for c in dimensoes + metrics if c in fato.columns]

    return fato[selected]
