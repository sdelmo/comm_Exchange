from abc import (ABC, abstractmethod)


class EconomicGood(ABC):
    """
    An Economic Good Abstract class with attributes:
    - name: name of the economic good
    - unit: unit of measurement for the good
    - price: last price of the good
    - time_last_trade: last date on which the good was traded

    From this one can build commodity and currency objects
    which can be traded on an exchange
    """

    def __init__(self, name, unit, price, time_last_trade):
        # initialize attributes
        self.name = name
        self.unit = unit
        self.price = price
        self.time_last_trade = time_last_trade

    # Set up getters/setters

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, goodName):
        self._name = goodName

    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, unitName):
        self._unit = unitName

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, newPrice):
        self._price = newPrice

    @property
    def time_last_trade(self):
        return self._time_last_trade

    @time_last_trade.setter
    def time_last_trade(self, last_Time):
        self._time_last_trade = last_Time

    @abstractmethod
    def __repr__(self) -> str:
        return f"EconomicGood({self.name}, {self.unit}, {self.price:10.2f}, {self.time_last_trade})"
