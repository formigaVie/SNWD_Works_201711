#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# define variable name
creator = "FormigaVIE"
outfile = open("menu.txt","w+")

# print welcome to user
print "=" *80
print "Welcome to {} your Restaurant Menu" .format(creator)
print "=" *80
# Put Make string lower case to a personal greeting
user=raw_input("\nPlease enter your name: ")
print "\n Hello {}, pleasure to have you here at Restaurant Menu" .format(user.upper())
print "=" *80

menu = {}
print menu
while True:
    dish = raw_input("Please enter the dish: ")
    price = raw_input("Please enter the price of the dish:")
    menu[dish]=price
    outfile.write(dish+":"+price+"\n")
    print menu
    again = raw_input("\nDo you like to add an additional meal? (n for exit): ")
    if again.lower() == "n":
        print "\nThank you {} for choining us." .format(user.upper())
        break
outfile.close()
