#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def addition(x,y):
    summe = x + y
    # return gibt den return Wert an die Stelle zurück womit es aufgerufen wurde
    return summe
    #variablen innerhalb einer Funktion werden nicht weitergegeben
def subtraction(x,y):
    summe = x - y
    return summe
    # auch möglich return = x + y

def multiplication(x,y):
    summe = x * y
    return summe

def division(x,y):
    summe = x / y
    return summe

if __name__ == '__main__':
    result = addition(10,23)
    print result
    result = subtraction(10,8)
    print result
    result = multiplication(4,2)
    print result
    result = division(27,3)
    print result