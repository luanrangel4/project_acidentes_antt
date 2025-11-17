"""
===============================================================================
EXTRACT MODULE — Pipeline de Acidentes ANTT
-------------------------------------------------------------------------------

Este módulo é responsável pela etapa de **Extração (E)** do pipeline ETL,
consolidando todos os arquivos CSV de acidentes das concessionárias.

Principais responsabilidades:
- Ler automaticamente todos os arquivos CSV dentro de um diretório (via glob)
- Tratar diferenças de encoding, separadores e linhas corrompidas
- Padronizar a identificação da concessionária com base no nome do arquivo
- Retornar um único DataFrame consolidado para uso nas próximas etapas (Transform/Load)

Decisões técnicas aplicadas:
- Uso de 'latin1' devido a inconsistências de acentuação nos dados originais.
- Uso do engine='python' por ser mais tolerante a erros de formatação.
- on_bad_lines='skip' para evitar quebra do fluxo por linhas defeituosas.
- Nome do arquivo convertido para a coluna 'concessionaria' para rastreabilidade.

Este módulo garante que a base de acidentes chegue íntegra e padronizada
para a próxima etapa de transformação.

===============================================================================
"""

import pandas as pd
import glob
import os

def extract_acidentes(path):
    arquivos = glob.glob(path)
    print(f"Encontrados {len(arquivos)} arquivos de acidentes.")

    dfs = []
    for arq in arquivos:
        try:
            df = pd.read_csv(
                arq,
                sep=";",
                encoding="latin1",
                engine="python",
                on_bad_lines="skip"
            )

           
            nome = os.path.basename(arq)  
            nome = nome.replace(".csv", "")
            nome = nome.replace("demostrativo_acidentes_", "")
            nome = nome.upper()

            df["concessionaria"] = nome  
            dfs.append(df)

        except Exception as e:
            print(f"❌ Erro ao ler {arq}: {e}")

    return pd.concat(dfs, ignore_index=True)
