from nsetools import Nse


class NseInitializer:
    def __init__(self):
        self.nse = Nse()

    def get_stock_codes(self):
        all_stock_codes = self.nse.get_stock_codes()
        return all_stock_codes

    def get_quote(self,symbol):
        quote = self.nse.get_quote(symbol)
        return quote
