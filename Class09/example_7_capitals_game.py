#!/usr/bin/env python
# -*- coding: UTF-8 -

import random

# define variable name
creator = "FormigaVIE"
current_points = 0

# print welcome to user
print "=" *80
print "Welcome to {} Capital Game" .format(creator)
print "=" *80
# Put Make string lower case to a personal greeting
user=raw_input("\nPlease enter your name: ")
print "\n Hello {}, pleasure to have you here at the Capital Game" .format(user.upper())
print "=" *80

points = {user:current_points}
capitals = {"FRANCE":"PARIS",
            "ICELAND":"REYKJAVIK",
            "DENMARK":"COPENHAGEN",
            "LITHUANIA":"VILNIUS",
            "CANADA":"OTTAWA",
            "AUSTRIA":"VIENNA",
            "GERMANY":"BERLIN",
            "SUISSE":"BERN"}
while True:
    for x in range (1,4):
        current_country =  random.choice(capitals.keys())
        print current_country
        y = 3 - x
        # Schreibe ein Programm mit random (Land) mit Eingabe und checken ob es korrekt war und Ausgabe des
        answer=raw_input("Please enter the capital of {}: ".format(current_country))
        if answer.upper() == capitals[current_country]:
            print "\n Congratulations - You are right - the capital of {} is {}" .format(current_country,capitals[current_country])
            points [user] += 1
            print "Your actual points are: {}".format(points[user])
        elif answer.upper() != capitals[current_country]:
            print "Sorry your answer isn't correct - the capital of {} is {}" .format(current_country,capitals[current_country])
            print "Only {} tries left" .format(y)

    again = raw_input("\nDo you like to calculate one more time (n for exit): ")
    if again.lower() == "n":
        print "\nThank you {} for choining us, your points: {}." .format(user.upper(), points[user])
        break

        # Erweiterung für Weiterführung