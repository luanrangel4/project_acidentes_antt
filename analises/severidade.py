import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("base/processed/acidentes_staging.csv")

cols = ["mortos", "gravemente_feridos", "moderadamente_feridos", "levemente_feridos"]
sev = df[cols].sum()

plt.figure(figsize=(10,6))
sev.plot(kind="bar")
plt.title("Severidade Total dos Acidentes")
plt.ylabel("Quantidade de Vítimas")
plt.tight_layout()
plt.show()