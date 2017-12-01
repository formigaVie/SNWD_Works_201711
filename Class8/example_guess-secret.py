#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# define variable name
creator = "FormigaVIE"
# Define a variable secret (Hardcoded)
secret = 23

# print welcome to user
print "=" *40
print "Welcome to {} GUESS-SECRET" .format(creator)
print "=" *40
print ""

for x in range (5):
    guess = int(raw_input("Please enter your guess between 0 and 30: "))
    y = 4-x
# start with the code
    if secret == guess:
        print ""
        print "You entered " + str(guess)
        print "*"*40
        print "Congratulations, this is the correct guess."
        print "*"*40
        break

    elif secret < guess:
        print ""
        print "You entered " + str(guess)
        print "*"*40
        print "This is the wrong guess, please try something smaller."
        print "Only {} tries left!" .format(y)
        print "*"*40
        print ""
    elif secret > guess:
        print ""
        print "You entered " + str(guess)
        print "*"*40
        print "This is the wrong guess, please try something BIGGER."
        print "Only {} tries left!" .format(y)
        print "*"*40
        print ""
 #   else:
 #       print ""
 #       print "You entered " + str(guess)
 #       print "*"*40
 #       print "Sorry, you have used all of your {} tries" .format(x)
 #       print "*"*40
 #       print ""


