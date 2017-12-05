#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# define variable name
creator = "FormigaVIE"

# print welcome to user
print "=" *80
print "Welcome to {} example" .format(creator)
print "=" *80
# Put Make string lower case to a personal greeting
user=raw_input("\nPlease enter your name: ")
print "\n Hello {}, pleasure to have you here at example" .format(user.lower())
print "=" *80

DIGITS = 2
# Round notwendig da er es nicht versteht nich 0.2 sondern 0.199999999*
if round(float(0.2 + 0.1),DIGITS) == 0.3:
    print True
else:
    print False

