import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("base/processed/acidentes_staging.csv")

top_conc = (
df["concessionaria"]
    .value_counts()
    .head(10)
)

plt.figure(figsize=(12,6))
top_conc.plot(kind="bar")
plt.title("Top 10 Concessionárias por Volume de Acidentes")
plt.xlabel("Concessionária")
plt.ylabel("Total de Acidentes")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
