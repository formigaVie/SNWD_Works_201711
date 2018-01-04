def extender(input_list):
    input_list.append("new")

if __name__ == '__main__':
    my_list = ["old"]
    # list is sliced (copy from first till last value) and so the my_list is the same as before
    extender (my_list [:])
    print my_list # ["old","new"]