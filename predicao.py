# ============================================
# PREVER CLASSIFICAÇÃO DE ACIDENTES
# Comparação: Logistic Regression, Random Forest, Gradient Boosting
# ============================================

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt


# ==============================
# 1) Carrega a base
# ==============================
df = pd.read_csv("base/processed/acidentes_staging.csv")


# ==============================
# 2) Corrige colunas numéricas
# ==============================

def fix_numeric_cols(df):
    for col in df.columns:
        if df[col].dtype == "object":

            # 👉 detecta números no formato BR (ex: 843,6)
            if df[col].astype(str).str.contains(r"\d+,\d+", regex=True).any():

                df[col] = (
                    df[col]
                    .astype(str)
                    .str.replace(".", "", regex=False)   # remove milhar
                    .str.replace(",", ".", regex=False) # vírgula → ponto
                )

                df[col] = pd.to_numeric(df[col], errors="coerce")

    return df

df = fix_numeric_cols(df)

# km pode ter null → substitui temporariamente por -1
if "km" in df.columns:
    df["km"] = df["km"].fillna(-1)


# ==============================
# 3) Engenharia de atributos
# ==============================
df["ano"] = pd.to_datetime(df["data_hora"]).dt.year
df["mes"] = pd.to_datetime(df["data_hora"]).dt.month
df["hora"] = pd.to_datetime(df["data_hora"]).dt.hour


# ==============================
# 4) Seleção das features
# ==============================
features = ["ano", "mes", "hora", "km", "concessionaria"]
target = "tipo_de_acidente_norm"

df = df[features + [target]].dropna()
X = df[features]
y = df[target]


# ==============================
# 5) Pré-processamento
# ==============================
colunas_cat = ["concessionaria"]
colunas_num = ["ano", "mes", "hora", "km"]

preprocessador = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), colunas_cat),
        ("num", "passthrough", colunas_num)
    ]
)



modelos = {
    "Logistic Regression": LogisticRegression(max_iter=500),
    "Random Forest": RandomForestClassifier(n_estimators=200),
    "Gradient Boosting": GradientBoostingClassifier()
}



X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


resultados = []

for nome, modelo in modelos.items():

    pipe = Pipeline(steps=[
        ("prep", preprocessador),
        ("model", modelo)
    ])

    pipe.fit(X_train, y_train)
    preds = pipe.predict(X_test)

    resultados.append({
        "Modelo": nome,
        "Acurácia": accuracy_score(y_test, preds),
        "Precisão (macro)": precision_score(y_test, preds, average="macro", zero_division=0),
        "Recall (macro)": recall_score(y_test, preds, average="macro", zero_division=0)
    })

df_resultados = pd.DataFrame(resultados)
print("\n===== RESULTADOS =====")
print(df_resultados)



plt.figure(figsize=(10,5))
plt.bar(df_resultados["Modelo"], df_resultados["Acurácia"])
plt.title("Comparação de Acurácia entre Modelos")
plt.ylabel("Acurácia")
plt.ylim(0, 1)
plt.show()
