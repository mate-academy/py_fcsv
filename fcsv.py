"""There is a CSV file containing data in this format: Product name, price, quantity
Calculate total cost for all products."""
import csv


def calc_price(filename: str, open_=open) -> float:
    """Multiply every second and third element in the row, and return the sum"""
    with open_(filename, 'rt') as file:
        reader = csv.reader(file, delimiter=',')
        total_cost = sum([float(row[1])*float(row[2]) for row in reader])
        return total_cost
