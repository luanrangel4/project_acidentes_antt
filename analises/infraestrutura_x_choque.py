import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("base/processed/acidentes_staging.csv")

infra = df[df["tipo_de_acidente_norm"].str.contains("Infraestrutura", na=False)]
top_infra = infra["concessionaria"].value_counts().head(10)

plt.figure(figsize=(12,6))
top_infra.plot(kind="bar")
plt.title("Choques com Infraestrutura por Concessionária")
plt.ylabel("Total")
plt.tight_layout()
plt.show()
