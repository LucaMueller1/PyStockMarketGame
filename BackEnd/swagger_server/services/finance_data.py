import yfinance as yf
import alpha_vantage
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

ts = TimeSeries(key='YOUR_API_KEY', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
data['open'].plot()
plt.title('Intraday Times Series for the MSFT stock (1 min)')
plt.show()


"""
stocks = "ADS.DE ALV.DE"
for stock in stocks:
    stock = yf.Ticker(stock)
    print(stock.info)
    print(stock.history("2d"))
    print("-------------")

#ALV.DE BAS.DE BAYN.DE BEI.DE BMW.DE CON.DE 1COV.DE DAI.DE DHER.DE DKB.DE DB1.DE DPW.DE DTE.DE DWNI.DE EOAN.DE FRE.DE FME.DE HEI.DE HEN3.DE IFX.DELIN.DE MRK.DE MTX.DE MUV2.DE RWE.DE SAP.DE SIE.DE VOW3.DE VNA.DE
"""