#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import random

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

creator = "FormigaVIE"
# Define a variable secret - with random.randint(0,30)
secret = random.randint(0,30)

def welcome_user():
# print welcome to user
    return "Welcome to {} {}" .format(creator, __file__)

def guess_secret():
    for x in range(5):
        guess = int(raw_input("Please enter your guess between 0 and 30: "))
        y = 4 - x
        # start with the code
        if secret == guess:
            print ""
            print "You entered " + str(guess)
            print "*" * 40
            print "Congratulations, this is the correct guess."
            print "*" * 40
            break
        elif secret < guess:
            print ""
            print "You entered " + str(guess)
            print "*" * 40
            print "This is the wrong guess, please try something smaller."
            print "Only {} tries left!".format(y)
            print "*" * 40
            print ""
        elif secret > guess:
            print ""
            print "You entered " + str(guess)
            print "*" * 40
            print "This is the wrong guess, please try something BIGGER."
            print "Only {} tries left!".format(y)
            print "*" * 40
            print ""

if __name__ == '__main__':
    print "=" *40
    print welcome_user()
    print "=" *40
    print ""
    print secret
    print guess_secret()