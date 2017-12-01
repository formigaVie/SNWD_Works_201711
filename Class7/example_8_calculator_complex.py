#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# define variable name
name = "FormigaVIE"

# print welcome to user
print "=" *40
print "Welcome to {} calculator" .format(name)
print "=" *40

while True:
    while True:
        # read user input for operation
        # mit CTRL + P zwischen eckiger Klammer zeigt an was dort hineinkommt - Funktion raw input
        operation_symbol = raw_input("Please enter an operation (+,-,*,/): ")
        print "You entered " + operation_symbol
        if operation_symbol in ["+", "-", "/", "*"]:
            break
        else:
            print "Please enter a valid operation, you entered: "+ operation_symbol

    while True:
        # read first number
            try:
                x = float(raw_input("Please enter your first number: "))
                print "you entered " + str(x)
                break
            except ValueError:
                print "Please enter a valid operation, you entered: " + str(x)

    while True:
        # read second number
            try:
                y = float(raw_input("Please enter your second number: "))
                print "you entered " + str(y)
                break
            except ValueError:
                print "Please enter a valid operation, you entered: " + str(y)
    # calculate and print result
    if operation_symbol == "+":
        print x + y
    elif operation_symbol == "-":
        print x - y
    elif operation_symbol == "/":
        if y == 0:
            # additional entry if divisor is 0
            print "Division by Zero"
        else:
            print x / y
    elif operation_symbol == "*":
        print x * y
    else:
        #print error if entry doesn't consists the
        print "Invalid input, try again"

    again=raw_input("Do you like to calculate one more time (n for exit): ")
    if again.lower()=="n":
        break
