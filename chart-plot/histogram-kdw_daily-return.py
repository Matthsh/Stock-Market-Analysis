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
Stocks = Stocks.groupby('company_name').apply(calc_daily_return)

# Create a list of the four companies we want to analyze
company_list = ['APPLE', 'GOOGLE', 'MICROSOFT', 'AMAZON']

# Set the figure size and create the subplots
plt.figure(figsize=(12, 9))

# Loop through each company and plot the histogram and KDE plot of the daily returns
for i, company in enumerate(company_list, 1):
    plt.subplot(2, 2, i)
    sns.distplot(Stocks.loc[Stocks['company_name'] == company, 'Daily Return'], bins=50, kde=True, kde_kws={'bw': 0.5})
    plt.xlabel('Daily Return')
    plt.ylabel('Density')
    plt.title(f'{company}')
    
plt.tight_layout()
plt.show()
