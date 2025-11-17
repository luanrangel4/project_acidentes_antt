import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("base/processed/acidentes_staging.csv")

df["hora"] = pd.to_datetime(df["data_hora"]).dt.hour
ac_hora = df["hora"].value_counts().sort_index()

plt.figure(figsize=(12,6))
ac_hora.plot(kind="bar")
plt.title("Distribuição de Acidentes por Hora do Dia")
plt.xlabel("Hora")
plt.ylabel("Total")
plt.tight_layout()
plt.show()
