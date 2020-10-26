import yfinance as yf
import pandas as pd
from ..db_service import DatabaseConn

def insert_csv():
    df = pd.read_csv(r"..data/S&P500")
    for key, value1 in df.iteritems():



