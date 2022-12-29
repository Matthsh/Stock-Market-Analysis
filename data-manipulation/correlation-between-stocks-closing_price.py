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

# Adicione a coluna 'company_name' ao DataFrame de retornos diários
tech_rets['company_name'] = df['company_name']


# Crie um novo DataFrame usando o método pivot_table
pivoted_rets = pd.pivot_table(tech_rets, index='Date', columns='company_name', values='closing_prices')

pivoted_rets = pivoted_rets.drop(pivoted_rets.index[0])

# Exibe os primeiros valores do novo DataFrame
print(pivoted_rets.head())

# Set up our figure by naming it returns_fig, call PairPLot on the DataFrame
return_fig = sns.PairGrid(pivoted_rets)

# Using map_upper we can specify what the upper triangle will look like.
return_fig.map_upper(plt.scatter, color='purple')

# We can also define the lower triangle in the figure, inclufing the plot type (kde) 
# or the color map (BluePurple)
return_fig.map_lower(sns.kdeplot, cmap='cool_d')

# Finally we'll define the diagonal as a series of histogram plots of the daily return
return_fig.map_diag(plt.hist, bins=30)

plt.show()