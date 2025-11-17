import pandas as pd
from utils.helpers import normalizar_tipo_acidente

df = pd.read_csv("base/processed/acidentes_staging.csv")


df["raw_norm"] = df["tipo_de_acidente"].astype(str).str.lower()

df["tipo_norm"] = df["tipo_de_acidente"].apply(normalizar_tipo_acidente)


trans = df[df["tipo_norm"] == "Colisão Traseira"]

print("===== TOTAL CLASSIFICADOS COMO COLISÃO TRANSVERSAL =====")
print(len(trans))

print("\n===== VALORES ORIGINAIS ENCONTRADOS =====")
for v in sorted(trans["tipo_de_acidente"].unique()):
    print("-", v)
