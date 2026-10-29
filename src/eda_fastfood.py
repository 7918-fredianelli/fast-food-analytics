import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração do estilo visual dos gráficos
sns.set_theme(style="whitegrid")

# Carregar os dados limpos do CSV exportado do Snowflake
df = pd.read_csv('../data/cleaned_fastfood_data.csv')

# Agrupamento do faturamento total por tipo de cozinha e ordenação do maior para o menor
faturamento_cozinha = df.groupby('CUISINE_TYPE')['ORDER_VALUE'].sum().reset_index()
faturamento_cozinha = faturamento_cozinha.sort_values(by='ORDER_VALUE', ascending=False)

print("\nFaturamento Total por Tipo de Cozinha:")
print(faturamento_cozinha)

# 5. Geração do Gráfico de Barras: Faturamento por Tipo de Cozinha
plt.figure(figsize=(10, 6))
sns.barplot(
    data=faturamento_cozinha, 
    x='CUISINE_TYPE', 
    y='ORDER_VALUE', 
    palette='Blues_r'
)
plt.title('Faturamento Total por Tipo de Cozinha', fontsize=14, fontweight='bold')
plt.xlabel('Tipo de Cozinha', fontsize=12)
plt.ylabel('Faturamento Total ($)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('../outputs/faturamento_por_cozinha.png', dpi=300)
plt.show()

# 6. Geração do Histograma: Distribuição do Tempo de Entrega
plt.figure(figsize=(10, 6))
sns.histplot(
    df['DELIVERY_TIME_MINUTES'].dropna(), 
    kde=True, 
    color='orange', 
    bins=20
)
plt.title('Distribuição do Tempo de Entrega (Minutos)', fontsize=14, fontweight='bold')
plt.xlabel('Tempo de Entrega (min)', fontsize=12)
plt.ylabel('Frequência de Pedidos', fontsize=12)
plt.tight_layout()
plt.savefig('../outputs/distribuicao_tempo_entrega.png', dpi=300)
plt.show()

print("\nAnálise concluída com sucesso! Todos os gráficos foram guardados na pasta.")

# 4.1. Análise: Ticket Médio por Tipo de Cozinha
ticket_medio = df.groupby('CUISINE_TYPE')['ORDER_VALUE'].mean().reset_index()
ticket_medio = ticket_medio.sort_values(by='ORDER_VALUE', ascending=False)

print("\nTicket Médio por Tipo de Cozinha:")
print(ticket_medio)