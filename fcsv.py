"""Module for reading CSV file and calculations
"""
import csv


def calc_price(filename, open_=open):
    """
    Get the total bill amount
    :param filename: CSV file
    :param open_: function to open file, default - built-in open()
    :return: result of calculations
    """
    result = 0
    with open_(filename, 'r') as bill:
        bill = csv.reader(bill, delimiter=',')
        for i in bill:
            result += float(i[1]) * float(i[2])
    return result
