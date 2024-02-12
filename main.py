from decimal import Decimal
from datetime import datetime
from time import sleep
import os

from eco_goods.economicGood import EconomicGood
from eco_goods.catalogue import Catalogue
from eco_goods.commodity import Commodity
from eco_goods.exchange import Exchange


def get_user_type():
    """
    Takes input from user, the input is used to show different functionality depending on
    whether the user is admin or not.

    args: none


    """
    global userId
    userId = {1: 'User', 2: 'Admin'}
    title = """
 .----..----..----.  .---.  .----. .-.   .-..-.   .-.
{ {__  | {_  | {}  }/  ___}/  {}  \|  `.'  ||  `.'  |
.-._} }| {__ | {}  }\     }\      /| |\ /| || |\ /| |
`----' `----'`----'  `---'  `----' `-' ` `-'`-' ` `-'
"""
    print(title)
    resp = None
    while resp not in userId.keys():
        try:
            resp = int(input(
                '\nWelcome to COMM commodity and exchange catalogue, please select one of the options below to begin:\n1 - User\n2 - Admin\n'))
        except ValueError:
            print("Sorry, that wasn't a valid option.")
            continue

    os.system('cls||clear')
    return userId[resp]


def user_ui(userType):
    resp = None
    global admin_options
    global user_options
    user_options = {
        1: catalogue.display_everything,
        2: catalogue.display_commodities,
        3: catalogue.display_commodity,
        4: catalogue.display_exchange
    }

    admin_options = {
        1: catalogue.add_exchange_from_string,
        2: catalogue.remove_exchange_from_string,
        3: catalogue.add_commodity_from_string,
        4: catalogue.remove_commodity_from_string,
        5: catalogue.add_commodity_to_exchange,
        6: catalogue.remove_commodity_from_exchange,
    }

    if userType == 'User':
        while (resp not in user_options.keys()) and (resp != 5):
            try:
                resp = int(input("Welcome, please select one of the options below:\n\
                                 1 - List all exchanges and the commodities they trade\n\
                                 2 - List all commodities and their information\n\
                                 3 - Get information about one commodity\n\
                                 4 - List all information about one exchange\n\
                                 5 - Return to the main menu\n"))
            except ValueError:
                print("Sorry, that wasn't a valid option.")
                continue

        os.system('cls||clear')
        return (resp, userType)

    elif userType == 'Admin':
        while (resp not in admin_options.keys()) and (resp != 7):
            try:
                resp = int(input("Welcome Admin, please select one of the options below:\n\
                                 1 - Create an exchange\n\
                                 2 - Delete an exchange \n\
                                 3 - Create a commodity\n\
                                 4 - Delete a commodity\n\
                                 5 - Add a commodity to an exchange\n\
                                 6 - Remove a commodity from an exchange\n\
                                 7 - Go back to the main menu\n"))
            except ValueError:
                print("Sorry, that wasn't a valid option.")
        os.system('cls||clear')
        return (resp, userType)
    return


def do_stuff(action, userType):
    """
    Takes a str from user to interact with commodity/exchanges objects

    Args: resp -> str
    """
    exch_name = None
    if userType == 'Admin':
        try:
            admin_options[action]()
            sleep(2)
            os.system('cls||clear')
        except KeyError:
            if action == 7:
                us = get_user_type()
                sleep(2)
                os.system('cls||clear')
                return us
            else:
                print(f"{action} is not a valid option for Admin user")

    elif userType == 'User':
        try:
            user_options[action]()
            sleep(5)
            os.system('cls||clear')
        except KeyError:
            if action == 5:
                us = get_user_type()
                sleep(1)
                os.system('cls||clear')
                return us
            else:
                print(f"{action} is not a valid option for User")

    os.system('cls||clear')
    return userType


if __name__ == "__main__":
    # Initialization and creating some commodities for testing
    com_on = True
    gold = Commodity(name='Gold', unit='USD/kg',
                     price=Decimal(63234), time_last_trade=datetime.now())
    silver = Commodity(name='Silver', unit='USD/kg',
                       price=Decimal(63234), time_last_trade=datetime.now())
    crude_oil = Commodity(name='WTI Crude', unit='USD/barrel',
                          price=Decimal(78.81), time_last_trade=datetime.now())

    lme = Exchange(name='LME')
    ftx = Exchange(name='FTX')
    catalogue = Catalogue()
    catalogue.add_commodity(gold)
    catalogue.add_commodity(silver)
    catalogue.add_commodity(crude_oil)
    lme.add_commodity(
        catalogue.commodities['Gold'], catalogue.commodities['Silver'])
    ftx.add_commodity(
        catalogue.commodities['WTI Crude'], catalogue.commodities['Gold'])
    catalogue.add_exchange(lme)
    catalogue.add_exchange(ftx)

    user = get_user_type()

    while com_on:
        re, us = user_ui(user)
        us = do_stuff(action=re, userType=us)
        re, user = None, us
