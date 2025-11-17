import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("base/processed/acidentes_staging.csv")

top_tipos = df["tipo_de_acidente_norm"].value_counts().head(15)

plt.figure(figsize=(12,6))
top_tipos.plot(kind="bar")
plt.title("Top 15 Tipos de Acidentes")
plt.xlabel("Tipo de Acidente")
plt.ylabel("Total")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
