import pandas as pd
import matplotlib.pyplot as plt

Stocks = pd.read_csv("./data/Stocks.csv", index_col="Date")

# Agrupa os dados por empresa
grouped = Stocks.groupby("company_name")

company_list = ["APPLE", "GOOGLE", "MICROSOFT", "AMAZON"]
ma_day = [10, 20, 50]

for ma in ma_day:
    for company in company_list:
        column_name = f"MA for {ma} days"
        Stocks[column_name] = Stocks['Adj Close'].rolling(ma).mean()
        

fig, axes = plt.subplots(nrows=2, ncols=2)
fig.set_figheight(10)
fig.set_figwidth(15)

Stocks.loc[Stocks["company_name"] == "APPLE", ['Adj Close', 'MA for 10 days', 'MA for 20 days', 'MA for 50 days']].plot(ax=axes[0,0])
axes[0,0].set_title('APPLE')

Stocks.loc[Stocks["company_name"] == "GOOGLE", ['Adj Close', 'MA for 10 days', 'MA for 20 days', 'MA for 50 days']].plot(ax=axes[0,1])
axes[0,1].set_title('GOOGLE')

Stocks.loc[Stocks["company_name"] == "MICROSOFT", ['Adj Close', 'MA for 10 days', 'MA for 20 days', 'MA for 50 days']].plot(ax=axes[1,0])
axes[1,0].set_title('MICROSOFT')

Stocks.loc[Stocks["company_name"] == "AMAZON", ['Adj Close', 'MA for 10 days', 'MA for 20 days', 'MA for 50 days']].plot(ax=axes[1,1])
axes[1,1].set_title('AMAZON')

fig.tight_layout()
plt.show()