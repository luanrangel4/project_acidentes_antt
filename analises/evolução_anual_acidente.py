import pandas as pd
import matplotlib.pyplot as plt

# Carregar staging
df = pd.read_csv("base/processed/acidentes_staging.csv")

# Converter data
df["data"] = pd.to_datetime(df["data"], errors="coerce")
df = df.dropna(subset=["data"])
df["ano"] = df["data"].dt.year

# Selecionar TOP tipos de acidente para não poluir o gráfico
top_tipos = df["tipo_de_acidente_norm"].value_counts().head(6).index
df_top = df[df["tipo_de_acidente_norm"].isin(top_tipos)]

# Agregar por ano e tipo
evolucao = (
    df_top.groupby(["ano", "tipo_de_acidente_norm"])
    .size()
    .reset_index(name="total")
)

# Plot
plt.figure(figsize=(14,8))

for tipo in top_tipos:
    dados = evolucao[evolucao["tipo_de_acidente_norm"] == tipo]
    plt.plot(dados["ano"], dados["total"], marker="o", label=tipo)

plt.title("Evolução Anual dos Acidentes por Tipo (Top 6)")
plt.xlabel("Ano")
plt.ylabel("Total de Acidentes")
plt.legend(title="Tipo de Acidente")
plt.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()
plt.show()
