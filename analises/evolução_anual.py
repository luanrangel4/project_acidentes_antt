import pandas as pd
import matplotlib.pyplot as plt

# Carregar staging
df = pd.read_csv("base/processed/acidentes_staging.csv")

# Criar coluna ano
df["ano"] = pd.to_datetime(df["data_hora"]).dt.year

# Agrupar por ano
evolucao_anual = df.groupby("ano").size()

# Plot
plt.figure(figsize=(12,6))
plt.plot(evolucao_anual.index, evolucao_anual.values, marker="o", linewidth=2)
plt.title("Evolução Anual dos Acidentes", fontsize=14)
plt.xlabel("Ano", fontsize=12)
plt.ylabel("Total de Acidentes", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()
plt.show()
