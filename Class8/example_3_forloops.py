#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Range erzeugt eine Liste mit 0-9
print range(10)
# Erzeugt eine Ausgabe von jeder 2.ten Zahl
print range(10)[::2]

for number in range(10):
    print number**2

# zweiter Wert ausschließlich (mit 3 Wert die Steps)
for number in range(1,10):
    print number**2