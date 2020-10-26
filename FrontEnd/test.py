import pandas as pd

data = [{
    "wkn": "string",
    "amount": 0,
    "stockName": "string",
    "stock_price": 0,
    "stock_buyin_price": 0,
    "countryId": "string",
    "industry": "string",
    "logoUrl": "string"
    },
        {
    "wkn": "string",
    "amount": 0,
    "stockName": "string",
    "stock_price": 0,
    "stock_buyin_price": 0,
    "countryId": "string",
    "industry": "string",
    "logoUrl": "string"
    }
        ]

df = pd.DataFrame(data)
print(df)

