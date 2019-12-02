"""
docstring
"""
import pandas as pd


def calc_price(filename):
    """

    :param filename:
    :return:
    """
    file = pd.read_csv(filename, names=["name", "price", "quantity"])
    return sum(file['price'] * file['quantity'])
