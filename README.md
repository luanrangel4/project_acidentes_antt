PROJETO ETL – ACIDENTES EM RODOVIAS CONCEDIDAS ANTT
INTRODUÇÃO

Este projeto tem como objetivo construir um pipeline de ETL (Extract, Transform, Load) para os dados de acidentes em rodovias concedidas disponíveis no portal de dados abertos da ANTT.

A solução foi desenhada para:

centralizar os arquivos .csv de todas as concessionárias em uma única base tabular;

padronizar tipos, formatos de data/hora e nomes de colunas;

modelar um pequeno Data Warehouse com:

uma tabela fato de acidentes, e

dimensões de Tempo, Veículo e Classificação;

facilitar o consumo dos dados por ferramentas como Power BI, Metabase ou notebooks de análise.

Dentre os benefícios da estrutura adotada:

organização em camadas (etl/, modelos/, utils/), facilitando manutenção e extensão do projeto;

separação clara entre extração, transformação, carga e modelagem dimensional;

uso de pandas para manipulação dos dados e CSV como formato final de entrega (facilmente migrável para qualquer SGBD);

comentários em pontos-chave do código para destacar decisões de modelagem e possíveis melhorias.

ESTRUTURA DE PASTAS

A estrutura básica do projeto foi organizada da seguinte forma:

project_acidentes_antt/
  main.py
  requirements.txt

  base/
    raw/         -> arquivos CSV originais baixados do portal da ANTT
    processed/   -> arquivos CSV processados (staging e DW)

  etl/
    extract.py   -> rotinas de extração/ingestão dos CSVs da pasta base/raw
    transform.py -> rotinas de padronização e enriquecimento (staging)
    load.py      -> rotinas para salvar os dados transformados em base/processed

  modelos/
    dim_tempo.py          -> criação da dimensão Tempo
    dim_veiculo.py        -> criação da dimensão Veículo
    dim_classificacao.py  -> criação da dimensão Classificação
    dim_fato_acidentes.py -> criação da tabela Fato Acidentes

  utils/
    io.py          -> funções auxiliares de leitura/escrita de arquivos
    logging_utils.py -> funções de log e mensagens de execução
    helpers.py     -> funções genéricas de apoio (ex: limpeza de campos)

  docs/
    README_ETL.md  -> documentação do projeto (este arquivo, sugerido)

Descrição das pastas principais

base/raw

Contém os arquivos .csv exatamente como disponibilizados pela ANTT, geralmente um arquivo por concessionária.

base/processed

Armazena os arquivos intermediários e finais:

acidentes_staging.csv – base unificada e padronizada (camada de staging).

dim_tempo.csv, dim_veiculo.csv, dim_classificacao.csv – dimensões.

fato_acidentes.csv – tabela fato.

etl/

Camada responsável pelo fluxo ETL:

extract.py
Responsável por localizar todos os CSVs na pasta base/raw, ler os arquivos (mantendo o schema fornecido pela ANTT) e concatenar em um DataFrame único.

transform.py
Responsável por aplicar as transformações necessárias:

conversão de tipos (datas, horários, numéricos);

criação da coluna data_hora a partir de data + horario;

padronização de nomes de colunas;

tratamento de valores nulos/inconsistentes.

load.py
Responsável por gravar os resultados (staging e dimensões/fato) em base/processed.

modelos/

Camada de modelagem dimensional:

dim_tempo.py
A partir da coluna data_hora da staging, gera uma dimensão Tempo com chaves substitutas e atributos como:

data_id (chave da dimensão),

data, ano, mes, dia, dia_da_semana, hora, etc.

dim_veiculo.py
Constrói a dimensão Veículo a partir das categorias de veículos do CSV original:

automovel, bicicleta, caminhao, moto, onibus, outros,
tracao_animal, transporte_de_cargas_especiais, trator_maquinas, utilitarios.

Cada tipo de veículo torna-se um registro de dimensão, com um identificador (id_veiculo) e a descrição (tipo_veiculo).

dim_classificacao.py
Cria a dimensão Classificação com base nos campos:

tipo_de_ocorrencia (ex: com vítima / sem vítima),

tipo_de_acidente (ex: colisão traseira, saída de pista, etc.),

e campos de severidade: ilesos, levemente_feridos, moderadamente_feridos, gravemente_feridos, mortos.

Nesta dimensão podemos armazenar não só a classificação textual, mas também indicadores de severidade (por exemplo, um índice ou categoria de gravidade).

dim_fato_acidentes.py
Constrói a tabela FatoAcidentes, integrando:

as chaves das dimensões (Tempo, Veículo, Classificação),

atributos de contexto (concessionária, rodovia/trecho, sentido, km),

métricas (quantidade de veículos por tipo, feridos, mortos, etc.).

utils/

Contém funções auxiliares reutilizáveis, por exemplo:

leitura e escrita de CSV com tratamento de encoding;

criação de diretórios, se não existirem;

funções de log (print_info, print_error, etc.);

funções genéricas de limpeza de texto/números.

FLUXO GERAL DO ETL

O fluxo do projeto pode ser descrito em três grandes etapas:

Extract (etl/extract.py)

varre a pasta base/raw/;

identifica todos os arquivos .csv de acidentes (por concessionária);

lê e concatena todos em um DataFrame, mantendo os campos originais:

concessionaria, data, horario, n_da_ocorrencia,
tipo_de_ocorrencia, km, trecho, sentido, tipo_de_acidente,
automovel, bicicleta, caminhao, moto, onibus, outros,
tracao_animal, transporte_de_cargas_especiais, trator_maquinas,
utilitarios, ilesos, levemente_feridos,
moderadamente_feridos, gravemente_feridos, mortos.

Transform (etl/transform.py)
Principais transformações:

Conversão de data (DD/MM/AA) para datetime;

Conversão de horario para time/datetime;

Criação da coluna data_hora (combinação de data + horario);

Conversão de campos numéricos (km, quantidades de veículos, feridos, mortos);

Limpeza de espaços, caracteres especiais e padronização de trecho e sentido;

Padronização do nome das colunas para um formato consistente.

Ao final, o DataFrame consolidado é salvo como:

base/processed/acidentes_staging.csv


Load + Modelagem Dimensional (main.py + modelos/)

A partir de acidentes_staging.csv, o script main.py:

carrega a base de staging;

chama create_dim_tempo, create_dim_veiculo, create_dim_classificacao;

chama create_fato_acidentes para montar a tabela fato;

salva todas as dimensões e a fato em base/processed.


PRIMEIROS PASSOS
Instalação das dependências

Na raiz do projeto:

pip install -r requirements.txt


(ou instale manualmente pelo menos pandas e python-dotenv/pathlib se utilizados).

Organização dos arquivos CSV

Baixe os arquivos .csv de acidentes no portal da ANTT.

Salve todos os arquivos na pasta:

base/raw/

Execução do pipeline

Na raiz do projeto, execute:

python main.py


O fluxo esperado é:

main.py chama as funções de extract, transform e load;

os arquivos são lidos, unificados e transformados;

são geradas:

base/processed/acidentes_staging.csv

base/processed/dim_tempo.csv

base/processed/dim_veiculo.csv

base/processed/dim_classificacao.csv

base/processed/fato_acidentes.csv

Esses arquivos podem então ser utilizados em ferramentas de análise ou carregados em um banco relacional/analítico.