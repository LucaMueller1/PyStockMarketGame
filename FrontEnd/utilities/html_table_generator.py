import streamlit as st

class PortfolioTable():
    """
    desc: main function, generates app
    param: (type) name, (type) name
    return: (type)
    test:
    """

    def __init__(self):
        self.html = ""

    def __add_row(self, row_data:dict):

        relative_gain = self.__calculate_relative_gain(row_data["stockValue"]["stock_price"],
                                                       row_data["stock_buyin_price"])
        color = "green"

        self.html += f"""<tr style="background-color:#f2f2f2">
                   <td style="text-align: center;"><img src="{row_data["logoUrl"]}", width="60em" border-radius="10%"></td>
                   <td style="font-weight:bold">{row_data["stockName"]}</td>
                   <td>{row_data["amount"]}</td>
                   <td>{round(row_data["stock_buyin_price"],2)}$</td>
                   <td>{round(row_data["stockValue"]["stock_price"],2)}$</td>
                   """

        if relative_gain < 0:
            color = "red"

        self.html += f"""<td style="color:{color};">{round(row_data["stockValue"]["stock_price"]-row_data["stock_buyin_price"],2)}$</td>"""
        self.html += f"""<td style="color:{color};">{relative_gain}%</td></tr>"""

    def __calculate_relative_gain(self, current_price: float, buyin_price: float) -> float:
        return round((current_price-buyin_price)/buyin_price*100,2)

    def add_headers(self):
        self.html += f"""<tr style="background-color:transparent;color:black;font-size:small">
                        <td></td>
                        <td>name</td>
                        <td>amount</td>
                        <td>buy in price</td>
                        <td>market price</td>
                        <td>gain ($)</td>
                        <td>gain (%)</td>
                        </tr>
                        """

    def add_portfolio(self, stock_data:list):
        for i in range(len(stock_data)):
            self.__add_row(stock_data[i])

    def open_table(self):
        self.html += """<table cellspacing="0" cellpadding="0" width="100%" style="border-collapse:collapse">"""

    def close_table(self):
        self.html += """</table>"""

    def get_html(self):
        return self.html