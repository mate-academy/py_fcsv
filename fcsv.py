"""
fcsv module
Functions:
    calc_price(products, open_=open) -- return
total cost of all products in the file products
"""
import csv


def calc_price(products, open_=open):
    """
    Return total cost of all products
    in the file products
    :param products: csv
    :param open_:
    :return: float
    """
    total = 0
    with open_(products, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            try:
                price, quantity = float(line[1]), int(line[2])
            except ValueError:
                print("Incorrect type for price or quantity value!!!")
            total += price * quantity
    return total
