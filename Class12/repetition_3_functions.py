def extender(input_list):
    input_list.append("new")

if __name__ == '__main__':
    my_list = ["old"]
    # list is mutable and so it is updated with the extender function
    extender (my_list)
    print my_list # ["old","new"]