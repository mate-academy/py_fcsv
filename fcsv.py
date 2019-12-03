"""This program collects quantitative product data (price, q-ty)
 and calculates the total value"""
import csv


def calc_price(filename, open_=open):
    """Find the total value of all products"""
    result = 0
    csv_file = open_(filename, "r")
    csv_reader = csv.reader(csv_file, delimiter=',')
    for line in csv_reader:
        result += float(line[1]) * float(line[2])
    filename.close()

    return result
