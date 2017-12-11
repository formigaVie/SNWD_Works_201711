#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#Funktion schreiben, die zu jeder Zahl die Quadratzahl zurückgibt

def square_number(x):
    return x**2

def check_square_number():
    assert square_number(9) == 81
    assert square_number(-3) == 9

if __name__ == '__main__':
    check_square_number()
    print "Passed test completed"