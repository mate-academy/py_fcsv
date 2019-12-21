"""
calc_price
"""


def calc_price(filename, open_=open):
    """
    calc_price
    """
    with open_(filename, 'r') as file1:
        result = 0
        for line in file1:
            prepared_line = line.split(',')
            result += float(prepared_line[1]) * float(prepared_line[2])

    return result
