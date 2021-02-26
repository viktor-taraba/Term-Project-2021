import yfinance as yf
from datetime import date, datetime
import pandas as pd 

start_date = date(2000, 2, 1)
end_date = date(2021, 2, 24)

names_list = ['^GSPC', '000001.SS', '^KS11', '^N225']
graph_names = ['SP500', 'SSE Composite Index', 'KOSPI', 'Nikkei225']
index_list = []

for i in range(len(names_list)):
	tickerSymbol = names_list[i]
	tickerData = yf.Ticker(tickerSymbol)

	df = tickerData.history(period='1d', start=start_date, end=end_date).dropna()
	df.drop(['Stock Splits', 'Dividends'], axis='columns', inplace=True)
	df = pd.DataFrame(data = df)
	df.index = pd.to_datetime(df.index)
	df["Date"] = df.index

	df["Percent change"] = df["Close"].pct_change(periods=1)

	index_list.append(df)
