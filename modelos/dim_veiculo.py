# A dimensão Veículo é estática e baseada nos tipos de veículos presentes no dataset.
# Criamos essa dimensão para permitir expansão futura (ex.: atributos adicionais,
# agrupamentos ou hierarquias de tipos veiculares).
# O modelo é simples porque cada tipo é apenas um indicador, não um relacionamento direto.

import pandas as pd

def create_dim_veiculo():
    tipos = [
        "automovel", "bicicleta", "caminhao", "moto", "onibus",
        "outros", "tracao_animal", "transporte_de_cargas_especiais",
        "trator_maquinas", "utilitarios"
    ]

    dim = pd.DataFrame({"tipo_veiculo": tipos})
    dim["sk_veiculo"] = dim.index + 1
    return dim



import pandas as pd

def create_dim_veiculo():
    tipos = [
        "automovel",
        "bicicleta",
        "caminhao",
        "moto",
        "onibus",
        "outros",
        "tracao_animal",
        "transporte_de_cargas_especiais",
        "trator_maquinas",
        "utilitarios"
    ]

    dim = pd.DataFrame({"tipo_veiculo": tipos})
    dim["sk_veiculo"] = dim.index + 1
    return dim
