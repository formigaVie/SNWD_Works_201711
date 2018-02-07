#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Define a variable secret (Hardcoded)
secret = 23
guess = int(raw_input("Please enter your guess between 0 and 30: "))

# start with the code

if secret == guess:
    print ""
    print "You entered " + str(guess)
    print "*"*40
    print "Congratulations, this is the correct guess."
    print "*"*40

else:
    print ""
    print "You entered " + str(guess)
    print "*"*40
    print "This is the wrong guess, please try it again"