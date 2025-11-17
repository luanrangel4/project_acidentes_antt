import pandas as pd
from pathlib import Path

def load_csv(path, sep=";", encoding="latin1"):
    return pd.read_csv(path, sep=sep, encoding=encoding, low_memory=False)

def save_csv(df, path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
