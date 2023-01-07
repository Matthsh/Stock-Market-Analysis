# Risco é a medida da incerteza ou da variabilidade de um investimento. 
# Quando investimos em ações, por exemplo, corremos o risco de perder 
# parte dou todo o valor investido, dependendo do desempenho das ações.

# Uma forma de quantificar o risco de um investimento é comparar o retorno 
# esperado com a desvio padrão dos retornos diários. O retorno esperado 
# é a média dos retornos diários, enquanto o desvio padrão é uma medida 
# da variabilidade ou da dispersão dos retornos em relação à média.

# Quanto maior o desvio padrão, maior é a variabilidade dos retornos e, 
# portanto, maior é o risco do investimento. Por outro lado, quanto menor
# o desvio padrão, menor é a variabilidade dos retornos e, portanto, 
# menor é o risco do investimento.

# Dessa forma, comparando o retorno esperado com o desvio padrão dos 
# retornos diários, é possível avaliar quanto valor estamos colocando 
# em risco ao investir em uma determinada ação. Por exemplo, se o retorno 
# esperado for alto, mas o desvio padrão for muito grande, isso pode 
# indicar um alto nível de risco.

# Espero que isso ajude a esclarecer o conceito! Se tiver mais dúvidas, 
# não hesite em perguntar.

# Importar bibliotecas
import pandas as pd
import numpy as np
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
tech_rets = pd.pivot_table(df, index='Date', columns='company_name', values='Adj Close')

# Remova os valores ausentes
rets = tech_rets.dropna()

# Calcule os retornos diários usando o método pct_change do pandas
rets = tech_rets.pct_change()

area = np.pi * 20

plt.figure(figsize=(10, 8))
plt.scatter(rets.mean(), rets.std(), s=area)
plt.xlabel('Expected return')
plt.ylabel('Risk')

for label, x, y in zip(rets.columns, rets.mean(), rets.std()):
    plt.annotate(label, xy=(x, y), xytext=(50, 50), textcoords='offset points', ha='right', va='bottom', 
                 arrowprops=dict(arrowstyle='-', color='blue', connectionstyle='arc3,rad=-0.3'))

plt.show()