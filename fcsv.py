"""
docstring
"""


def calc_price(filename, open_=open):
    """

    :param filename:
    :return:
    """
    with open_(filename, 'rt') as file:
        return sum(float(line.split(',')[1]) * int(line.split(',')[2]) for line in file.readlines())
