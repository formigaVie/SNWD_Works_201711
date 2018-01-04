def extender(input_list):
    input_list.append("new")
    # return wird verwendet fuer die Weitergabe der Liste an eine Variable
    return input_list

if __name__ == '__main__':
    my_list = ["old"]
    my_list = extender (my_list)
    print my_list # ["old","new"]