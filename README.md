Projeto ETL – Acidentes em Rodovias Concedidas (ANTT)

Este projeto implementa um pipeline completo de ETL para consolidar, padronizar e modelar dados de acidentes em rodovias concedidas no Brasil.
O objetivo é transformar arquivos CSV brutos da ANTT em um Data Warehouse analítico, pronto para consumo em BI ou Ciência de Dados.

🚀 Objetivos

Unificar dados de todas as concessionárias em uma única base.

Padronizar datas, horários, tipos de acidentes e classificação.

Criar um DW em modelo estrela com:

Fato Acidentes

Dimensões: Tempo, Veículo, Classificação, Concessionária, Tipo de Acidente

Facilitar análises descritivas, inferenciais e modelagem preditiva.

📂 Estrutura do Projeto
project_acidentes_antt/
│   main.py
│   requirements.txt
│   README.md
│
├── base/
│   ├── raw/            # dados brutos da ANTT
│   └── processed/      # staging + DW
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
└── utils/
    ├── io.py
    ├── helpers.py
    └── logging_utils.py

⚙️ Execução do Pipeline

Instale as dependências:

pip install -r requirements.txt


Coloque os CSVs originais em:

base/raw/


Execute o pipeline:

python main.py


Os resultados aparecem em:

base/processed/

📊 Conteúdos complementares

A documentação completa está organizada em:

docs/ETL.md → detalhes da implementação

docs/MODELAGEM.md → modelagem dimensional

docs/ANALISES.md → análises descritivas e inferenciais

docs/PREDICAO.md → modelos preditivos e métricas

Esses arquivos estão na pasta docs/ para manter o README limpo e profissional.

📝 Status

✔ Pipeline ETL
✔ Classificação avançada dos acidentes
✔ DW em CSV
✔ Análises descritivas
✔ Gráficos
✔ Predição básica
⬜ Dashboard (opcional)
⬜ API (opcional)
