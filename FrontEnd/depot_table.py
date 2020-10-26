from pytablewriter import MarkdownTableWriter
from pytablewriter.style import Style
import pandas as pd
import json

class DepotTable():
    def __init__(self, stock_data: list):
        self.writer = MarkdownTableWriter()
        self.stock_data = stock_data

    def calculate_relative_change(self) -> list:
        relative_change = []
        for i in range(len(self.stock_data)):
            relative_change.append(f"""{round((self.stock_data[i]["stock_price"] - self.stock_data[i]["stock_buyin_price"]) / self.stock_data[i]["stock_buyin_price"] * 100, 2)}%""")
        return relative_change

    def convert(self) -> str:
        df = pd.DataFrame(self.stock_data)[['logoUrl', 'stockName', 'amount', 'stock_price']]
        df["relative change"] = self.calculate_relative_change()
        self.writer.from_dataframe(df)
        self.writer.set_style(column="relative change", style=Style(color="#FFFFFF"))
        return self.writer.dumps()