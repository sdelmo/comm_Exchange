from .economicGood import EconomicGood


class Commodity(EconomicGood):
    """
    A commodity is an Economic good with a price, unit, time of last trade, and a name
    """

    def __init__(self, name, unit, price, time_last_trade):
        super().__init__(name, unit, price, time_last_trade)

    def __repr__(self) -> str:
        return f"Commodity({self.name}, {self.unit}, {self.price:10.2f}, {self.time_last_trade})"
