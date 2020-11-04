import utilities.requests_server as requests_server
# BUY
def check_for_entry_string(entry):
    if entry != "N/A":
        return entry
    else:
       return "N/A"

def get_single_stock_value(auth_key, ticker_code):
    stock_price = ((requests_server.get_stockprice_history(auth_key, ticker_code, "1d"))[0]["stock_price"])
    if stock_price != "N/A":
        return round(float(stock_price), 2)
    else:
        return "N/A"

def get_total_stock_value(single_stock_value, quantity):
    if single_stock_value != "N/A":
        return (single_stock_value * quantity)
    else:
        return "N/A"

def get_total_purchase_value(total_stock_value, purchase_fees):
    if total_stock_value != "N/A":
        return (str(total_stock_value + purchase_fees) + "$")
    else:
        return ("N/A")

def get_dividend_yield(dividend_yield_raw):
    if dividend_yield_raw != "N/A":
        dividend_yield = str(int(dividend_yield_raw) * 100)
        return dividend_yield
    else:
        dividend_yield = "N/A"
        return dividend_yield


# SELL
