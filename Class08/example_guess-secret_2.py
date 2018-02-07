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

while True:
    guess = int(raw_input("Please enter your guess between 0 and 30: "))
# start with the code
    if secret == guess:
        print ""
        print "You entered " + str(guess)
        print "*"*60
        print "Congratulations, this is the correct guess."
        print "*"*60
        break

    elif secret < guess:
        print ""
        print "You entered " + str(guess)
        print "*"*60
        print "This is the wrong guess, please try something smaller."
       # print "Only {} tries left!" .format(y)
        print "*"*60
        print ""
    elif secret > guess:
        print ""
        print "You entered " + str(guess)
        print "*"*60
        print "This is the wrong guess, please try something BIGGER."
      #  print "Only {} tries left!" .format(y)
        print "*"*60
        print ""
#    else:
#        print ""
#        print "You entered " + str(guess)
#        print "*"*40
#        print "Sorry, you are wrong"
#        print "*"*40
#        print ""


