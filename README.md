PROJETO ETL – ACIDENTES EM RODOVIAS CONCEDIDAS (ANTT)
📌 Introdução

Este projeto implementa um pipeline de ETL (Extract, Transform, Load) para processar dados de acidentes em rodovias concedidas, disponibilizados pelo portal de Dados Abertos da ANTT.

Objetivos principais:

Centralizar todos os arquivos CSV das concessionárias em uma única base tabular.

Padronizar estruturas, nomes de colunas e formatos de data/hora.

Construir um Modelo Dimensional contendo:

Tabela fato de acidentes

Dimensões: Tempo, Veículo, Classificação, Concessionária e Tipo de Acidente

Preparar os dados para consumo em ferramentas como Power BI, Metabase, pandas, Spark, etc.

Benefícios da solução:

Organização clara em camadas (etl/, modelos/, utils/)

Modularidade → cada etapa é separada e de fácil manutenção

CSV como armazenamento final → fácil integração com qualquer SGBD

Comentários estratégicos no código explicando decisões de modelagem

📂 Estrutura de Pastas
project_acidentes_antt/
│   main.py
│   requirements.txt
│   README.md
│
├── base/
│   ├── raw/          # Arquivos originais da ANTT
│   ├── processed/    # Staging + Data Warehouse em CSV
│
├── etl/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── modelos/
│   ├── dim_tempo.py
│   ├── dim_veiculo.py
│   ├── dim_classificacao.py
│   ├── dim_concessionaria.py
│   ├── dim_tipo_acidente.py
│   └── dim_fato_acidentes.py
│
├── utils/
│   ├── io.py
│   ├── helpers.py
│   └── logging_utils.py
│
└── analises/          # gráficos e análises exploratórias

🗂 Descrição das Pastas
📁 base/raw

Contém os arquivos CSV originais da ANTT (um por concessionária).

📁 base/processed

Contém os arquivos finais do ETL:

acidentes_staging.csv – base consolidada e padronizada

dim_tempo.csv

dim_veiculo.csv

dim_classificacao.csv

dim_concessionaria.csv

dim_tipo_acidente.csv

fato_acidentes.csv

⚙️ Camada ETL
🔹 etl/extract.py – Extração

Varre base/raw/

Lê todos os CSVs independente da concessionária

Acrescenta coluna concessionaria

Concatena tudo em um único DataFrame

🔹 etl/transform.py – Transformação

Principais ajustes aplicados:

Normalização de nomes das colunas

Conversão:

data → datetime

horario → time

km → numérico

Criação de data_hora

Padronização e correção de ruídos textuais

Classificação granular dos acidentes:

Saída de pista

Choques (infraestrutura / objeto fixo / objeto móvel / veículo parado...)

Atropelamentos

Tombamento / capotamento

Infraestrutura viária

Incidentais, etc.

Resultado final salvo como acidentes_staging.csv.

🔹 etl/load.py – Carga

Salva os arquivos transformados na pasta base/processed.

🧱 Modelagem Dimensional

O DW segue um modelo estrela com 1 fato e 5 dimensões.

⭐ Fato: FATO_ACIDENTES

Contém as métricas e atributos do acidente:

Chaves das dimensões

Concessionária, trecho, sentido, km

Quantidades de veículos envolvidos

Severidade (ilesos, feridos, mortos)

🧩 Dimensões:
DIM_TEMPO

Derivada de data_hora.
Inclui: ano, mês, dia, trimestre, dia da semana, hora.

DIM_VEICULO

Lista padronizada de tipos de veículos.

DIM_CLASSIFICACAO

Inclui:

tipo_de_ocorrencia

tipo_de_acidente

atributos de severidade (feridos, mortos)

DIM_CONCESSIONARIA

Padroniza os nomes das concessionárias.

DIM_TIPO_ACIDENTE

Taxonomia criada a partir do classificador desenvolvido.

🚀 Fluxo do ETL
Extract → Transform → Load → Modelagem → DW Pronto

Extract

Lê todos os CSVs de base/raw

Transform

Padroniza

Limpa

Normaliza

Enriquecimento (classificação avançada)

Load

Salva staging e DW

Modelagem Dimensional

Criação das 5 dimensões

Criação da tabela fato

Salvamento final em base/processed

▶️ Como Executar
1) Instalar dependências
pip install -r requirements.txt

2) Colocar arquivos originais

Salvar todos os CSVs da ANTT em:

base/raw/

3) Rodar o ETL completo
python main.py

4) Arquivos gerados em:
base/processed/

📊 Análises e Predições

O projeto também inclui:

📌 Análise descritiva

Evolução temporal

Tipos de acidente

Severidade

Hotspots por km

Comparação entre concessionárias

📌 Análise inferencial

Associação de variáveis (Qui-Quadrado)

Diferença de severidade (ANOVA)

Correlação entre fatores e gravidade

📌 Modelos preditivos (Tarefa 3)

Algoritmos comparados:

Logistic Regression

Random Forest

Gradient Boosting

Com métricas:

Acurácia

Precisão

Recall

✅ Status do Projeto

✔️ ETL completo
✔️ Modelagem dimensional
✔️ Classificação avançada de acidentes
✔️ Gráficos de análise exploratória
✔️ Predição inicial com Random Forest / GBM