class PortfolioTable():
    def __init__(self):
        self.html = ""
        
    def add_css(self):
        self.html += """<style></style>
          """

    def __add_row(self, row_data:dict):

        relative_gain = round((row_data["stock_price"]-row_data["stock_buyin_price"])/row_data["stock_buyin_price"]*100,2)
        color = "green"

        self.html += f"""<tr>
                   <td><img src="{row_data["logoUrl"]}", height=30, width=30> {row_data["symbol"]}</td>
                   <td>{row_data["stockName"]}</td>
                   <td>{row_data["amount"]}</td>
                   <td>{row_data["stock_price"]}</td>
                   """
        if relative_gain < 0:
            color = "red"

        self.html += f"""<td style="color:{color};">{relative_gain}%</td></tr>"""

    def add_headers(self):
        self.html += f"""<tr style="background-color:black;color:white">
                        <td style="font weight:bold"></td>
                        <td style="font weight:bold">name</td>
                        <td style="font weight:bold">amount</td>
                        <td style="font weight:bold">market value</td>
                        <td style="font weight:bold">gain (%)</td>
                        </tr>
                        """
    
    def add_portfolio(self, stock_data:list):
        for i in range(len(stock_data)):
            self.__add_row(stock_data[i])

    def open(self):
        self.html += """<table style="width:100%">"""

    def close(self):
        self.html += """</table>"""

    def get_html(self):
        return self.html