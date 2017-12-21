#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import random
from datetime import date

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

creator = "FormigaVIE"
datum = date.today()

def welcome_user():
# print welcome to user
    return "Welcome to {} {} \n actual date: {}" .format(creator, __file__, datum)

def question():
    countg = []
    guess = int(raw_input("Please enter how many random numbers would you like to have: "))
    for i in range(0,guess+1):
        if i < guess:
            lotto = random.randint(0,45)
            countg.append(lotto)
        else:
            pass
        return countg
def christmas():
    # for a christmas greeting between first of december and sixth of january
    if str(datum) >= "2017-12-01" and str(datum) <= "2018-01-06":
        print ""
        print " "*3+"Merry"+" "*3+"/"+"\\"
        print "Christmas"+" "+"/"+" "*2+"\\"
        print " "*4+"To"+" "*3+"/"+" "*4+"\\"
        print " "*3+"You"+" "*2+"/"+"_"*6+"\\"
    else:
        pass
if __name__ == '__main__':
    print welcome_user()
    print question()
    print christmas()