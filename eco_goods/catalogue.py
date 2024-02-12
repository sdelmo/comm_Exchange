from .commodity import Commodity
from .exchange import Exchange
from decimal import Decimal
from datetime import datetime
import os


class Catalogue():
    """
    Catalogue object that displays exchanges, the commodities they trade, and can produce reports, 
    only accessible by user type, not admin type

    The catalogue should be able to return a report on all commodities traded, as well as exchanges and their commodities

    """

    def __init__(self):
        self.exchanges = {}
        self.commodities = {}

    def add_exchange(self, ex):

        try:
            self.exchanges[ex.name] = ex
        except TypeError:
            print(
                "The object you are trying to add to the catalogue is not an Exchange Object")

    def add_exchange_from_string(self):
        # Takes input from user to create an exchange and add it to the catalogue
        exchange_name = input(
            "Enter the name of the exchange to create below:\n").upper()
        warn = None
        # Check and warn if we are overwriting an exchange
        if exchange_name in self.exchanges.keys():
            while warn not in (1, 2):
                try:
                    warn = int(input(f"It seems exchange {exchange_name} already exists in the catalogue,\n\
                                     1 - Overwrite the exchange object \n\
                                     2 - Return to main menu\n"))
                except ValueError:
                    print("Sorry, that's not a valid option.")
                    continue
            if warn == 2:
                return
            elif warn == 1:
                pass

        self.add_exchange(Exchange(name=exchange_name))
        print(f"Exchange {exchange_name} created")

    def remove_exchange(self, ex):

        try:
            self.exchanges.pop(ex.name)
        except TypeError:
            print(
                "The object you are trying to add to the catalogue is not an Exchange Object")

    def remove_exchange_from_string(self):
        # Takes input from user to remove an exchange from the catalogue
        exchange_name = None

        # Print exchanges
        self.print_exchanges()

        # Let user decide which one to delete and log
        while exchange_name not in self.exchanges.keys():
            exchange_name = input(
                "Enter the name of the exchange to delete:\n").upper()

        self.remove_exchange(self.exchanges[exchange_name])
        print(f"Exchange {exchange_name} successfully deleted\n")

    def add_commodity(self, c):

        try:
            self.commodities[c.name] = c
        except TypeError:
            print(
                "The object you are trying to add to the catalogue is not a Commodity Object")

    def add_commodity_from_string(self):
        # Takes in user input to create a commodity object
        print("You are now creating a commodity object, please provide the details as required\n")
        commodity_name = input('Commodity Name: ')
        lowercase_comms = [k.lower() for k in self.commodities.keys()]
        warn = None
        # Check and warn if we are overwriting a commodity
        if commodity_name in lowercase_comms:
            while warn not in (1, 2):
                try:
                    warn = int(input(f"It seems commodity {commodity_name.capitalize()} already exists in the catalogue,\n\
                                 1 - Overwrite the commodity object\n\
                                 2 - Return to main menu\n"))
                except ValueError:
                    print("Sorry, that's not a valid option.")
                    continue

            if warn == 2:
                return
            elif warn == 1:
                pass

        # Finish creating the commodity object

        commodity_unit = input('Unit of Measurement: ')

        commodity_price = None

        while type(commodity_price) != Decimal:
            try:
                commodity_price = Decimal(float(input('Price: ')))
            except:
                print(
                    "Something went wrong, make sure you are inputting a number, be it a float or an int :)")

        commodity_time = datetime.now()
        self.add_commodity(Commodity(name=commodity_name, unit=commodity_unit,
                           price=commodity_price, time_last_trade=commodity_time))
        print(f"Commodity {commodity_name} successfully created")

    def remove_commodity(self, c):

        try:
            # Remove the commodity from every exchanges' catalogue
            secondary_stores = [
                e for e in self.exchanges.keys() if c.name in self.exchanges[e].comms_offered.keys()]

            [self.exchanges[e].remove_commodity(c) for e in secondary_stores]

            self.commodities.pop(c.name)
        except TypeError:
            print(
                "The object you are trying to add to the catalogue is not an Commodity Object")

    def remove_commodity_from_string(self):

        # Takes user input to remove a commodity from the catalogue
        commodity_name = None
        self.print_commodities()

        # Get user to pick a commodity
        while commodity_name not in self.commodities.keys():
            commodity_name = input(
                "Enter the name of the commodity to delete:\n")

        # Remove commodity object from catalogue and log
        self.remove_commodity(self.commodities[commodity_name])
        print(f"Commodity {commodity_name} Delete successful")

    def add_commodity_to_exchange(self):
        commodity_name = None
        exchange_name = None

        self.print_commodities()

        # Keep looping until user provides a valid Commodity name

        while commodity_name not in self.commodities.keys():
            commodity_name = input("Commodity to add: ")

        self.print_exchanges()

        # Keep looping until user provides a valid Exchange name
        while exchange_name not in self.exchanges.keys():
            exchange_name = input(
                "Exchange to add commodity to: ").upper()

        self.exchanges[exchange_name].add_commodity(
            self.commodities[commodity_name])
        print(
            f"Commodity {commodity_name} successfully added to {exchange_name} exchange.")

    def remove_commodity_from_exchange(self):
        commodity_name = None
        exchange_name = None

        # Print all exchanges
        self.print_exchanges()

        while exchange_name not in self.exchanges.keys():
            exchange_name = input("Exchange: ").upper()

        # Print all commodities offered by an exchange
        print("Now select the commodity you want to remove from it: ")
        print(*self.exchanges[exchange_name].comms_offered.keys(), sep='\n')

        # Take a commodity name to remove
        while commodity_name not in self.commodities.keys():
            commodity_name = input("Commodity name: ")

        # Remove commodity from chosen exchange and log
        self.exchanges[exchange_name].remove_commodity(
            self.commodities[commodity_name])
        print(
            f"Commodity {commodity_name} successfully removed from {exchange_name} exchange.")

    def display_everything(self):
        """Displays exchanges along the commodities they trade"""
        e = 'Exchange'
        print(f"{e:<12s}", 'Commodities offered', sep='')

        [(self.exchanges[e].display_comms(), print())
         for e in self.exchanges.keys()]

    def display_commodities(self):
        # Display all commodities and their details
        cols = ['Commodity', 'Unit', 'Price', 'Time of Last Trade']
        print(f"{cols[0]:<15s}{cols[1]:<15s}{cols[2]:<15s}{cols[3]:<15s}")

        [print(
            f"{name:<15s}{object.unit:<15s}{object.price:<15.2f}{str(object.time_last_trade):<15}")
         for name, object in self.commodities.items()]

    def display_commodity(self):
        commodity_name = None

        self.print_commodities()
        while commodity_name not in self.commodities.keys():
            commodity_name = input("Commodity: ")

        os.system('cls||clear')
        obj = self.commodities[commodity_name]
        cols = ['Unit', 'Price', 'Last Traded', 'Exchanges trading']
        print(f"{obj.name}\n")
        print(f"{cols[0]:<18s}: {obj.unit:<15s}")
        print(f"{cols[1]:<18s}: {obj.price:<15.2f}")
        print(f"{cols[2]:<18s}: {str(obj.time_last_trade):<15s}")
        print(f"{cols[3]:<18s}: ", end='')

        exch = [k for k, v in self.exchanges.items(
        ) if commodity_name in v.comms_offered.keys()]

        print(*exch, sep=', ')

    def display_exchange(self):
        exchange_name = None
        self.print_exchanges()
        while exchange_name not in self.exchanges.keys():
            exchange_name = input("Exchange: ").upper()
        os.system('cls||clear')

        obj = self.exchanges[exchange_name]
        print(f"{obj.name:<15s}")
        print("Commodities traded: ", end='')
        coms = list(obj.comms_offered.keys())
        print(*coms, sep=', ')
        return

    def print_commodities(self):
        print('Select a commodity from the options below: ')
        print(*self.commodities.keys(), sep='\n')

    def print_exchanges(self):
        print('Select an exchange from the options below: ')
        print(*self.exchanges.keys(), sep='\n')

    def __repr__(self) -> str:
        return f"Catalogue({self.exchanges})"
