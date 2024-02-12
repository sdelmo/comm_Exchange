from .commodity import Commodity


class Exchange:
    """
    Defines an exchange class
    An exchange has a:
    - name
    - list of commodities it trades
    """

    def __init__(self, name) -> None:
        self.name = name
        self.comms_offered = {}

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n):
        self._name = n

    def add_commodity(self, *args):
        """Adds a commodity/s to the commodities offered by an exchange"""

        self.comms_offered.update(
            {c.name: c for c in args if isinstance(c, Commodity)})

        return self.comms_offered

    def remove_commodity(self, *args):
        """Removes a commodity/s from the comms offered by an exchange"""

        comms = list(args)

        # Pythonic implementation
        try:
            [self.comms_offered.pop(c.name)
             for c in comms if isinstance(c, Commodity)]
        except AttributeError:
            print(
                f'One of the objects in {comms} is not an instance of the Commodity class')
        return self.comms_offered

    def display_comms(self):
        # Displays exchange name and commodities traded
        print(f"{self.name:<12s}", end='')
        comms = [c for c in self.comms_offered.keys()]
        print(*comms, sep=', ', end='')

    def __repr__(self) -> str:
        return (f"Exchange({self.name}, {self.comms_offered})")
