# O objetivo é entender qual foi o retorno diário da ação, ou seja, qual foi a variação do preço da ação 
# ao longo do tempo. Esse é um indicador importante para avaliar o risco de uma ação e para tomar decisões de investimento.

# Para calcular o retorno diário, podemos usar a função "pct_change" do pandas. Ela nos permite calcular a 
# variação percentual do preço da ação em relação ao dia anterior. Assim, se a ação fechou em 10 reais no dia 1 e em 12 reais no dia 2, 
# o retorno diário seria de 20%.

# É importante lembrar que o retorno diário é apenas uma das métricas que podemos usar para avaliar o risco de uma ação. 
# Outras métricas comuns incluem o retorno anual, a volatilidade e o beta. Todas essas métricas nos ajudam a entender como a ação 
# se comporta em relação ao mercado e ao risco em geral. Assistant

import pandas as pd
import matplotlib.pyplot as plt


Stocks = pd.read_csv("./data/Stocks.csv", index_col="Date")

def calc_daily_return(df):
    df['Daily Return'] = df['Adj Close'].pct_change()
    return df

# We'll use pct_change to find the percent change for each day
Stocks = Stocks.groupby('company_name').apply(calc_daily_return)


# Then we'll plot the daily return percentage
fig, axes = plt.subplots(nrows=2, ncols=2)
fig.set_figheight(10)
fig.set_figwidth(15)

Stocks.loc[Stocks["company_name"] == "APPLE", ['Daily Return']].plot(ax=axes[0,0], legend=True, linestyle='--', marker='o')
axes[0,0].set_title('APPLE')

Stocks.loc[Stocks["company_name"] == "GOOGLE", ['Daily Return']].plot(ax=axes[0,1], legend=True, linestyle='--', marker='o')
axes[0,1].set_title('GOOGLE')

Stocks.loc[Stocks["company_name"] == "MICROSOFT", ['Daily Return']].plot(ax=axes[1,0], legend=True, linestyle='--', marker='o')
axes[1,0].set_title('MICROSOFT')

Stocks.loc[Stocks["company_name"] == "AMAZON", ['Daily Return']].plot(ax=axes[1,1], legend=True, linestyle='--', marker='o')
axes[1,1].set_title('AMAZON')

fig.tight_layout()
plt.show()