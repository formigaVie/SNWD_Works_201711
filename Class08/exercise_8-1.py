#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# define variable name
creator = "FormigaVIE"

# print welcome to user
print "=" *80
print "Welcome to {} Unit Converter \n" .format(creator)
print "In this program you can convert kilometres to miles."
print "=" *80

while True:
    # Ask the user for the input of a kilometer value \n is for start in an additional new line
    unit=raw_input("\nPlease add your value (in km) which you want to be converted to miles: ")
    print "\nYou want {} km to be converted to miles." .format(float(unit))

    # Define variable Digits for rounding to 2 decimal places at the calculation of miles
    DIGITS = 2
    convert = round(float(unit) / 1.61, DIGITS)

    print "\n {} km = {} mi" .format(float(unit),convert)

    # Ask the user for an additional conversion
    again=raw_input("\nDo you like to calculate one more time (n for exit): ")
    if again.lower()=="n":
        break