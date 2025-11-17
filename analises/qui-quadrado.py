import scipy.stats as stats

import pandas as pd
df = pd.read_csv("base/processed/acidentes_staging.csv")
cont = pd.crosstab(df["tipo_de_acidente_norm"], df["hora"])
chi2, p, dof, exp = stats.chi2_contingency(cont)

print("p-value:", p)
    