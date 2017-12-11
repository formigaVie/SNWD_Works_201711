#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# def für define functionsname (x):
# pass ist ein Platzhalter
def func():
    print "Hi, this is main"

def print_greeting(name):
    print "Hello "+name


# Wenn if __name__ == '__main__': dann bei einlesen der Funktionen wir das nicht ausgeführt
# ab heute wichtig mai (und dann mit Tab autovervollständigen)
# runde Klammern () "callen" - rufen eine Funktion
# dunder (double underscoure)__name__, __file__
if __name__ == '__main__':
    func()
    print_greeting("Oli")



