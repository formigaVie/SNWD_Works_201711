#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# V0.1: source:www.pythoncentrail.io/python-snippets-how-to-generate-random-string/
# V0.2: adapted/enhanced M. Grie�er 16.01.2018: add allchar2 without punctuation and pwd2, add readable date, add length of created pwd, print it at the console

vers = "V0.2"

import string
import datetime
from random import *

min_char = 8
max_char = 12
allchar = string.ascii_letters + string.punctuation + string.digits
allchar2 = string.ascii_letters + string.digits
password = "".join(choice(allchar) for x in range (randint(min_char, max_char)))
password2 = "".join(choice(allchar2) for x in range (randint(min_char, max_char)))
#currentdatetime = datetime.datetime.now()
#readabledate= currentdatetime.strftime("%Y-%m-%d %H:%M:%S")
# optimized output of datetime
readabledate = (datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
print "Generation Date:" ,readabledate+" Version: ",vers
print "This is your password:" ,password+"the length is: ",len(password)
print "This is your password2:" ,password2+"the length is: ",len(password2)

