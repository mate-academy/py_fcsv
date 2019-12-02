"""Reader from csv module return a reader object
which will iterate over lines in the given csv file"""
from csv import reader


def calc_price(filename, opener=open):
    """return total cost for all products in csv file"""
    with opener(filename, "rt") as csvfile:
        csvreader = reader(csvfile)
        return sum(float(row[1]) * float(row[2]) for row in csvreader)
