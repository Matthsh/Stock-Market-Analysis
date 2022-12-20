import pandas as pd
import matplotlib.pyplot as plt

Stocks = pd.read_csv("./Data/Stocks.csv", index_col="Date")

# Agrupa os dados por empresa
grouped = Stocks.groupby("company_name")

# Configura o tamanho da figura e os espaçamentos entre os subplots
plt.figure(figsize=(15, 10))
plt.subplots_adjust(top=1.25, bottom=1.2)

# Itera sobre os grupos e plota os dados de cada empresa em um subplot separado
for i, (name, group) in enumerate(grouped, 1):
    plt.subplot(2, 2, i)
    group['Adj Close'].plot()
    plt.ylabel('Adj Close')
    plt.xlabel('Date')
    plt.title(f"Closing Price of {name}")
    
plt.tight_layout()
plt.show()