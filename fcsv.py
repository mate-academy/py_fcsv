'''
Module
'''


def calc_price(read_file, open_=open):
    '''
    Calculate total cost for all products.
    :param read_file:
    :param open:
    :return:
    '''
    with open_(read_file, "rt") as reading:
        result = 0
        for line in reading:
            line = line.split(',')
            price, count = float(line[1]), float(line[2])
            result += price * count
    return result
