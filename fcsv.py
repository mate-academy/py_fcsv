"""
module calculate costs of products from csv file
"""
import csv
from functools import reduce


def calc_price(filename: str, open_=open) -> float:
    """
    There is a CSV file containing data in this format:
    Product name, price, quantity
    Calculate total cost for all products (price * quantity).
    :param filename: str
    :param open_: open
    :return: float
    """
    with open_(filename, 'rt') as file:
        sum_prod_costs = 0.0
        csv_reader = csv.reader(file, delimiter=',')
        param_lsts = [list(map(float, line[1:])) for line in csv_reader]
        for lst in param_lsts:
            sum_prod_costs += reduce((lambda x, y: x * y), lst)
    return sum_prod_costs
