#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#Funktion schreiben, die zu jeder Zahl die Quadratzahl zurückgibt

def cube_number(x):
    return x**3

def check_cube_number():
    assert cube_number(3) == 27
    assert cube_number(-3) == -27

if __name__ == '__main__':
    check_cube_number()
    print "Passed test completed"