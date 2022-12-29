# Correlação é uma medida da associação entre duas variáveis. Ela indica se duas 
# variáveis estão relacionadas de alguma forma e, se estiverem, em que intensidade.

# Uma correlação pode ser positiva, o que significa que as duas variáveis tendem a 
# se mover na mesma direção: quando uma variável aumenta, a outra também tende a 
# aumentar; quando uma variável diminui, a outra também tende a diminuir. 
# Por exemplo, existe uma correlação positiva entre o salário e o nível de 
# educação, pois pessoas com níveis mais elevados de educação tendem a ganhar mais 
# do que aquelas com níveis mais baixos de educação.

# Uma correlação também pode ser negativa, o que significa que as duas variáveis 
# tendem a se mover em direções opostas: quando uma variável aumenta, a outra 
# tende a diminuir; quando uma variável diminui, a outra tende a aumentar. Por 
# exemplo, existe uma correlação negativa entre o consumo de álcool e a 
# performance acadêmica, pois pessoas que consomem mais álcool tendem a ter 
# uma performance acadêmica pior do que aquelas que consomem menos álcool.

# A correlação entre duas variáveis é medida por um coeficiente de correlação, 
# que pode assumir valores entre -1 e 1. Se o coeficiente de correlação for -1, 
# significa que existe uma correlação negativa perfeita entre as duas variáveis; 
# se for 1, significa que existe uma correlação positiva perfeita; se for 0, 
# significa que não há correlação entre as variáveis.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Lê o arquivo CSV usando o método read_csv do pandas
df = pd.read_csv('./data/Stocks.csv', index_col='Date', parse_dates=True)

# Selecione a coluna 'Adj Close' do DataFrame
closing_prices = df['Adj Close']

tech_rets = pd.DataFrame()

# Calcule os retornos diários usando o método pct_change do pandas
tech_rets['daily_return'] = closing_prices.pct_change()

# Adicione a coluna 'company_name' ao DataFrame de retornos diários
tech_rets['company_name'] = df['company_name']


# Crie um novo DataFrame usando o método pivot_table
pivoted_rets = pd.pivot_table(tech_rets, index='Date', columns='company_name', values='daily_return')

pivoted_rets = pivoted_rets.drop(pivoted_rets.index[0])

# Exibe os primeiros valores do novo DataFrame
print(pivoted_rets.head())

sns.pairplot(pivoted_rets, kind='reg')

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
plt.show()