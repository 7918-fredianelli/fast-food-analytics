# Fast-Food Analytics & Data Pipeline (Snowflake + Python)

Pipeline de dados de ponta a ponta focado em otimização de faturamento e eficiência logística para o setor de fast-food, utilizando **Snowflake (SQL)** para o processo ETL, Levantamento de indicadores e Modelagem de Dados, e **Python (Pandas, Seaborn)** para Análise Exploratória de Dados (EDA).

---

## Visão Geral do Projeto
Este projeto simula um cenário real de Business Intelligence. O objetivo foi gerir dados de pedidos, tratá-los no Snowflake, estruturar regras de negócio através de **Views SQL** e extrair insights estratégicos com visualizações de alta resolução.

---

## Stack Tecnológica
* **Armazenamento & Nuvem:** Snowflake (SQL, Views, Modelagem de Dados)
* **Análise de Dados & Estatística:** Python, Pandas, Matplotlib, Seaborn
* **Controlo de Versões:** Git & GitHub

---

## Estrutura do Repositório
```text
Fast-Food-Analytics/
│
├── data/
│   ├── cleaned_fastfood_data.csv  # Dados tratados prontos para consumo
│   └── raw_fast_food_dataset.csv  # Dados sem tratamento 
│
├── sql/
│   ├── 01_etl_clean_data.sql      # Script de limpeza e tratamento inicial
│   └── 02_create_views.sql        # View analítica com regras de negócio (CASE WHEN)
│
├── src/
│   └── eda_fastfood.py            # Script Python de Análise Exploratória (EDA)
│
├── outputs/
│   ├── faturamento_por_cozinha.png  # Gráfico de faturamento total por categoria
│   └── distribuicao_tempo_entrega.png # Histograma de eficiência logística
│
├── requirements.txt               # Dependências do projeto
└── README.md                      # Documentação oficial do projeto

--

## Principais Etapas e Lógica de Negócio
Camada de Modelagem (Snowflake):

Criação de visões estruturadas utilizando CASE WHEN para segmentar o valor dos pedidos em faixas de mercado (High-Value vs Standard) e monitorizar o desempenho logístico (Delayed vs On-Time).

Análise Exploratória (Python):

Cálculo de métricas cruciais de negócio como Faturamento Total e Ticket Médio (AOV) agrupados por tipo de cozinha.

Geração de gráficos estatísticos (Barras e Histograma com curva KDE) exportados em alta resolução (300 DPI).

--

## Principais Insights Extraídos
Concentração de Receita: Identificação clara das categorias culinárias que lideram o faturamento total da operação.

Comportamento Logístico: Análise da distribuição dos tempos de entrega para detetar gargalos operacionais e padrões de atraso.

--

## Como Executar o Projeto
Como este projeto é um fluxo de ponta a ponta (Cloud + Local), a execução divide-se em duas etapas: Engenharia de Dados (Snowflake) e Análise Exploratória (Python).

1. Camada de Banco de Dados (Snowflake)
Abra a sua worksheet no Snowflake e execute os scripts na ordem numérica para preparar a base de dados:

Limpeza e ETL: Execute o script sql/01_etl_clean_data.sql para tratar os dados brutos e gerar a tabela final.

Criação da View Analítica: Execute o script sql/02_create_views.sql para criar a view VW_ORDER_METRICS com as regras de negócio (CASE WHEN).

2. Análise Local (Python)
No seu terminal, na pasta raiz do projeto, siga os passos:

Clone o repositório:

git clone [https://github.com/](https://github.com/)[SEU_UTILIZADOR]/[NOME_DO_REPOSITORIO].git
cd Fast-Food-Analytics
Instale as dependências:


pip install -r requirements.txt
Execute o script de análise:


python src/eda_fastfood.py

--

## Autor
Desenvolvido por Vinícius Fredeanelle Sucupira de Assis

LinkedIn | Notion Portfolio