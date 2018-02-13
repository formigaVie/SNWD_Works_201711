"""use pylint"""

def add_numbers(xvalue, yvalue):
    """ add numbers and return sum

    :param xvalue:
    :type xvalue: int or float
    :param yvalue:
    :type yvalue: int or float
    :return:
    :rtype: int or float
    """
    return xvalue+yvalue


if __name__ == '__main__':
    print add_numbers(1, 2)
