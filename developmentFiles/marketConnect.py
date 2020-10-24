import yfinance as yf   #idk if thats allowed
import matplotlib.pyplot as plt

apple = yf.Ticker('AAPL')
print(apple.info)
data = yf.download(apple.ticker, start='2019-01-01', end='2020-09-01')
data.Close.plot()
plt.show()