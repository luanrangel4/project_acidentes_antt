"""
===============================================================================
MAIN PIPELINE — ETL e Modelagem Dimensional de Acidentes ANTT
-------------------------------------------------------------------------------

Este script orquestra toda a execução do pipeline, coordenando as etapas:

1. EXTRAÇÃO
   - Leitura de múltiplos arquivos CSV da ANTT.
   - Tratamento de inconsistências de encoding, delimitadores e linhas quebradas.

2. TRANSFORMAÇÃO
   - Padronização e saneamento de colunas.
   - Conversão robusta de datas e horários.
   - Correção de resíduos textuais e classificação granular
     dos tipos de acidentes.

3. CARGA EM STAGING
   - Armazena a base unificada e tratada para auditoria
     e reprocessamento eficiente.

4. MODELO DIMENSIONAL
   - Criação das dimensões: Tempo, Classificação, Veículo,
     Concessionária e Tipo de Acidente.
   - Construção da tabela fato consolidada e referenciada
     por chaves substitutas (surrogate keys).

5. EXPORT FINAL
   - Geração dos arquivos finais que compõem o Data Warehouse
     em formato CSV estruturado.


===============================================================================
"""






from etl.extract import extract_acidentes
from etl.transform import transform_acidentes
from etl.load import load_staging

from modelos.dim_tempo import create_dim_tempo
from modelos.dim_classificacao import create_dim_classificacao
from modelos.dim_veiculo import create_dim_veiculo
from modelos.dim_fato_acidentes import create_fato_acidentes
from modelos.dim_concessionaria import create_dim_concessionaria
from modelos.dim_tipo_acidente import create_dim_tipo_acidente

from utils.io import save_csv


def run():

    df = extract_acidentes("base/raw/*.csv")

    
    df = transform_acidentes(df)

    load_staging(df)

   
    dim_tempo = create_dim_tempo(df)
    dim_classificacao = create_dim_classificacao(df)
    dim_veiculo = create_dim_veiculo()
    dim_concessionaria = create_dim_concessionaria(df)
    dim_tipo = create_dim_tipo_acidente(df)

    fato = create_fato_acidentes(
    df,
    dim_tempo,
    dim_classificacao,
    dim_concessionaria,
    dim_tipo
)
   
    if "sentido" in fato.columns:
        fato["sentido"] = fato["sentido"].fillna("Não informado")

   
    save_csv(dim_tempo, "base/dimensional/dim_tempo.csv")
    save_csv(dim_classificacao, "base/dimensional/dim_classificacao.csv")
    save_csv(dim_veiculo, "base/dimensional/dim_veiculo.csv")
    save_csv(dim_concessionaria, "base/dimensional/dim_concessionaria.csv")
    save_csv(dim_tipo, "base/dimensional/dim_tipo_acidente.csv")
    save_csv(fato, "base/dimensional/fato_acidentes.csv")

    print("Pipeline concluído com sucesso!")


if __name__ == "__main__":
    run()
