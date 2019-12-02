"""
There is a CSV file containing data in this format:
Product name, price, quantity.
Calculate total cost for all products.
"""


def calc_price(filename, open_=open):
    """Calculate total cost for all products"""
    total_cost = 0
    with open_(filename, 'rt') as rfile:
        for line in rfile.readlines():
            total_cost += float(line.split(',')[1]) * int(line.split(',')[2])
    return total_cost
