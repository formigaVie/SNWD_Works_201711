#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def change_list(a_list):
    a_list.append("New")

# bei Listen wird der direkte Wert zurückgegeben, also wenn die Liste in einer Funktion bearbeitet wird, wird der neue Wert mitgegeben

if __name__ == '__main__':
    my_list = range(19)
    print my_list
    change_list(my_list)
    print my_list