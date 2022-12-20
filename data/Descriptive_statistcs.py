import pandas as pd
import matplotlib.pyplot as plt

Stocks = pd.read_csv("Stocks.csv", index_col="Date")

# Agrupa os dados por empresa
grouped = Stocks.groupby("company_name")

# Aplica o método describe() em cada grupo
for name, group in grouped:
    print(f"Estatísticas descritivas para a empresa {name}:")
    print(group.describe())
    print()