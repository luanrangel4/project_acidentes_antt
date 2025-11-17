import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("base/processed/acidentes_staging.csv")

df["hora"] = pd.to_datetime(df["data_hora"]).dt.hour
sev_por_hora = df.groupby("hora")["mortos"].sum()

plt.figure(figsize=(12,6))
sev_por_hora.plot(kind="line", marker="o")
plt.title("Óbitos por Hora do Dia")
plt.ylabel("Total de Mortes")
plt.grid(True)
plt.tight_layout()
plt.show()
