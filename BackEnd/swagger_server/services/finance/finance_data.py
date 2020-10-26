import yfinance as yf
import pandas as pd
import xlrd
import sqlalchemy as sqla
"""

"""

stocks = (
"ADS.DE", "ALV.DE", "BAS.DE", "BAYN.DE", "BEI.DE", "BMW.DE", "CON.DE", "1COV.DE", "DAI.DE", "DHER.DE", "DKB.DE",
"DB1.DE", "DPW.DE", "DTE.DE", "DWNI.DE", "EOAN.DE", "FRE.DE", "FME.DE", "HEI.DE", "HEN3.DE", "IFX.DE", "LIN.DE",
"MRK.DE", "MTX.DE", "MUV2.DE", "RWE.DE", "SAP.DE", "SIE.DE", "VOW3.DE", "VNA.DE")

def get_tradable_values():
    df = pd.read_excel(r'data/traded_companies.xlsx')
    print(df)
    i = 0
    for line in df:
        try:
            stock_info = yf.Ticker(line[0])
            ++i
        except:
            print(line[0], f" 333 error retrieving %s from yfinance")
            ++i
            pd[i]

def get_stock_history(stock: str):
    stock = yf.Ticker(stock)
    print(stock.info)
    print(stock.history("2d"))
    print("-------------")

    for day in stock.history(0):
        print(day)


def __init__(self):
    self.engine = sqla.create_engine('mysql://pybroker:mSWcwbTpuTv4Liwb@pma.tutorialfactory.org/pybroker', echo=True)


get_tradable_values()