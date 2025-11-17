"""
===============================================================================
LOAD MODULE — Pipeline de Acidentes ANTT
-------------------------------------------------------------------------------

Este módulo implementa a etapa de **Carga (L)** do pipeline ETL.

Sua função é persistir dados já transformados em uma área de staging limpa,
garantindo que todo o processamento posterior (modelagem dimensional,
validações, geração de fatos/dimensões etc.) utilize uma base padronizada
e previamente tratada.

Principais responsabilidades:
- Gravar o DataFrame resultante da etapa de transformação em arquivo CSV.
- Garantir rastreabilidade e reprodutibilidade do pipeline por meio do staging.
- Centralizar lógica de persistência utilizando o utilitário `save_csv`.

Decisões técnicas aplicadas:
- Armazenamento em `base/processed/` para separar dados brutos, processados e dimensionais.
- Uso de um módulo utilitário (`utils.io.save_csv`) para manter consistência
  no padrão de escrita de arquivos.
- A função retorna o próprio DataFrame para permitir encadeamento do pipeline.
"""


from utils.io import save_csv

def load_staging(df, path="base/processed/acidentes_staging.csv"):
    save_csv(df, path)
    return df
