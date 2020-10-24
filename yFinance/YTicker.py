import yfinance as yf

def get_stock(wkn):
    wkn = yf.Ticker(wkn)
    return wkn

