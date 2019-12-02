"""There is a CSV file containing data in this format: Product name, price, quantity"""


def calc_price(filename, opens=open):
    """Calculate total cost for all products """
    cost_all_item = 0
    with opens(filename, 'rt') as csv_file:
        for row in csv_file.readlines():
            item = row.split(",")
            cost_all_item = (float(item[1]) * float(item[2])) + cost_all_item
    csv_file.close()
    return cost_all_item
