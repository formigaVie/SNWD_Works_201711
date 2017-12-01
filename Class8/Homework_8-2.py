#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# define variable name
creator = "FormigaVIE"

# print welcome to user
print "=" *80
print "Welcome to {} FizzBuzz" .format(creator)
print "=" *80

while True:
    # Ask the user for the input of a kilometer value \n is for start in an additional new line
    numbx=raw_input("\nPlease select a number between 1 and 100: ")
    print "\n Selected value{} \n".format(int(numbx))
    # start with the ouptut
    for x in range (int(numbx)+1):
        # Output dependent on values with Modulo 3,5 or both
        if x % 3 != 0 and x % 5 != 0:
            print x
        elif x % 3 == 0 and x %5 == 0:
            print "fizzbuzz"
        elif x % 3 == 0:
            print "fizz"
        elif x % 5 == 0:
            print "buzz"
        else:
            break

    # Give the user the info that he can try it again
    again=raw_input("\nDo you like to calculate one more time (n for exit): ")
    if again.lower()=="n":
        break