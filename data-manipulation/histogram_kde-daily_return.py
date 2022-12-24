# O histograma é um tipo de gráfico que é usado para 
# visualizar a distribuição de um conjunto de dados. 
# Ele é construído dividindo os dados em "intervalos" ou 
# "bins" e contando quantos valores de dados caem em cada
# bin. O eixo x do histograma representa os bins e o 
# eixo y representa a frequência dos dados.

# Um histograma pode ser construído a partir dos retornos 
# diários de um ativo. Neste caso, o eixo x representaria 
# os intervalos de retorno e o eixo y representaria a 
# frequência dos retornos diários. Isso pode ser útil 
# para entender como os retornos diários estão distribuídos 
# e para fazer previsões sobre os retornos futuros.

# O gráfico de distribuição de kernel (KDE) também pode 
# ser usado para visualizar a distribuição dos retornos 
# diários de um ativo. Ele funciona de maneira semelhante 
# ao histograma, mas é construído a partir de uma função 
# kernel que é usada para suavizar os dados. O KDE é 
# útil quando os dados não seguem uma distribuição 
# normal e pode ser usado para fazer previsões sobre os 
# retornos futuros.

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Read in the stock data and set the index to the 'Date' column
Stocks = pd.read_csv("./data/Stocks.csv", index_col="Date")

# Define a function to calculate the daily returns of a stock
def calc_daily_return(df):
    df['Daily Return'] = df['Adj Close'].pct_change()
    return df

# We'll use pct_change to find the percent change for each day
Stocks = Stocks.groupby('company_name', group_keys=False).apply(calc_daily_return)

# Create a list of the four companies we want to analyze
company_list = ['APPLE', 'GOOGLE', 'MICROSOFT', 'AMAZON']

# Set the figure size and create the subplots
plt.figure(figsize=(12, 9))

# Loop through each company and plot the histogram and KDE plot of the daily returns
for i, company in enumerate(company_list, 1):
    plt.subplot(2, 2, i)
    sns.histplot(data=Stocks.loc[Stocks['company_name'] == company, 'Daily Return'], bins=50, kde=True)
    plt.xlabel('Daily Return')
    plt.ylabel('Density')
    plt.title(f'{company}')
    
plt.tight_layout()
plt.show()
