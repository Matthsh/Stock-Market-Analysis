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

# Lê os dados do arquivo CSV e armazena em um DataFrame
stocks_df = pd.read_csv("./data/Stocks.csv")

# Seleciona as colunas de interesse
tech_stocks_df = stocks_df[['Date', 'Adj Close']].copy()

# Renomeia as colunas para facilitar o acesso posterior
tech_stocks_df.columns = ['date', 'adj_close']

# Calcula as variações percentuais dos preços de fechamento ajustados
tech_stocks_df.loc[:, 'return'] = tech_stocks_df['adj_close'].pct_change()

# Exibe os primeiros registros do DataFrame
tech_stocks_df.head()
