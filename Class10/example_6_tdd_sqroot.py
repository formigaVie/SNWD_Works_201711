#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# """ in erster Zeile unter funktion dann kann ich googlestyle docstring (Restructred text) erstellen
# durch Type kann der Variablentype definiert werden und diese wird dann gecheckt
# durch rtype kann auch der Rueckgabewerttyp definiert werden
def cube_root(x):
    """
    :param x: cube root
    :type x:int or float
    :return:
    :rtype:int or float
    """
    return x**(1/3)

def check_cube_root():
    assert cube_root(27) == 27 ** (1/3)
    assert cube_root(81) == 81 ** (1/3)

if __name__ == '__main__':
    check_cube_root()
    print "Tests passed sucessfully"