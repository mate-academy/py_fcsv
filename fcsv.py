"""Total price module"""
import csv


def calc_price(filename, open_=open):
    """
    Search total price in all file
    :param filename: file for reading
    :param open:
    :return: the sum of all multiplications
    """
    with open_(filename, 'rt') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        result = 0
        for row in reader:
            result += float(row[1]) * float(row[2])
    return result
