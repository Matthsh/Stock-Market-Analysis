import yfinance as yf
from datetime import datetime

# Get the stock quote
ticker = yf.Ticker("AAPL")
df = ticker.history(start='2012-01-01', end=datetime.now())


# salva o dataframe em um arquivo csv
df.to_csv('./data/Stocks.csv')

# Show teh data
print(df)