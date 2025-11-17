import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("base/processed/acidentes_staging.csv")

plt.figure(figsize=(12,6))
df["tipo_de_acidente"].value_counts().plot(kind="bar")
plt.title("Quantidade de Acidentes por Tipo")
plt.xlabel("Tipo de Acidente")
plt.ylabel("Total")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
