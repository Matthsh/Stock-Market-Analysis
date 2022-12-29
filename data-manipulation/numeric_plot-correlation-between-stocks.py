import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Lê o arquivo CSV usando o método read_csv do pandas
df = pd.read_csv('./data/Stocks.csv', index_col='Date', parse_dates=True)

# Selecione a coluna 'Adj Close' do DataFrame
closing_prices = df['Adj Close']

tech_rets = pd.DataFrame()

# Calcule os retornos diários usando o método pct_change do pandas
tech_rets['closing_prices'] = closing_prices
tech_rets['daily_return'] = closing_prices.pct_change()

# Adicione a coluna 'company_name' ao DataFrame de retornos diários
tech_rets['company_name'] = df['company_name']


# Crie um novo DataFrame usando o método pivot_table
closing_df = pd.pivot_table(tech_rets, index='Date', columns='company_name', values='closing_prices')
tech_rets = pd.pivot_table(tech_rets, index='Date', columns='company_name', values='daily_return')


tech_rets = tech_rets.drop(tech_rets.index[0])



plt.figure(figsize=(12, 10))

plt.subplot(2, 2, 1)
sns.heatmap(tech_rets.corr(), annot=True, cmap='summer')
plt.title('Correlation of stock return')

plt.subplot(2, 2, 2)
sns.heatmap(closing_df.corr(), annot=True, cmap='summer')
plt.title('Correlation of stock closing price')

plt.show()
plt.show()