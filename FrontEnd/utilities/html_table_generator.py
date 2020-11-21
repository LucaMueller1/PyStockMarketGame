"""
    desc:       portfolio table generator module for PyBroker Streamlit GUI
    author:     Ben Schaper
    date:       2020-11-16
"""
# MODULE IMPORTS
import streamlit as st

# UTILITY IMPORTS
import utilities.utils as utils


class PortfolioTable:
    """
    desc:   Class that generates the portfolio table. Methods help with initializing the
            table, with adding rows and with closing the table.
    author: Ben Schaper
    date:   2020-11-20
    """

    def __init__(self):
        self.html = ""

    def __add_row(self, row_data: dict) -> None:
        """
        desc:   internal method, adds a row to the html table given a proper row data dict.
        param:  (dict) row_data
        test:   pass: row data contains all needed keys. Row can be added.
                fail: provided row data is missing information. Row can not be added.
        """

        relative_gain = self.__calculate_relative_gain(
            row_data["stockValue"]["stock_price"], row_data["stock_buyin_price"]
        )
        color = "green"

        self.html += f"""<tr>
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

    def __calculate_relative_gain(
        self, current_price: float, buyin_price: float
    ) -> float:
        """
        desc:   internal method, calculates relative gain for a current price and a buyin price.
        param:  (float) current_price, (flot) buyin_price
        test:   pass: parameters are provided with correct type, must be numerical.
                fail: parameters are provided as a type which can not be divided.
        """
        return round((current_price - buyin_price) / buyin_price * 100, 2)

    def add_headers(self) -> None:
        """
        desc:   adds the portfolio table headers to the html.
        """
        self.html += f"""<tr style="font-size:small">
                        <td></td>
                        <td>name</td>
                        <td>amount</td>
                        <td>buy in price</td>
                        <td>market price</td>
                        <td>gain ($)</td>
                        <td>gain (%)</td>
                        </tr>
                        """

    def add_portfolio(self, stock_data: list) -> None:
        """
        desc:   adds all portfolio positions to the table, provided by the stock_data parameter.
        param:  (list) stock_data
        test:   pass: stock_data is of type list. It contains 0 or many positions.
                fail: stock_data is not of type list.
        """
        for i in range(len(stock_data)):
            self.__add_row(stock_data[i])

    def open_table(self) -> None:
        """
        desc:   opens the portfolio table html.
        """
        self.html += """<div class="table-responsive"><table class="table" cellspacing="0" cellpadding="0" width="100%" style="border-collapse:collapse;border-color:transparent;">"""

    def close_table(self) -> None:
        """
        desc:   closes the portfolio table html.
        """
        self.html += """</table></div>"""

    def get_html(self) -> str:
        """
        desc:   returns the portfolio table html.
        """
        return self.html
