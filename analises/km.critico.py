import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("base/processed/acidentes_staging.csv")


km_counts = df["km"].value_counts().head(20)

plt.figure(figsize=(12,6))
km_counts.plot(kind="bar")
plt.title("Top 20 KM com Mais Acidentes")
plt.xlabel("KM")
plt.ylabel("Total")
plt.tight_layout()
plt.show()
