#!/usr/bin/env python
# -*- coding: UTF-8 -

capitals = {"France":"Paris",
            "Iceland":"Reykjavik",
            "Denmark":"Copenhagen",
            "Litauen":"Vilnius",
            "Canada":"Ottawa",
            "Austria":"Vienna"}

print "Study the following list:"
print
print capitals.items()
print
for country,capital in capitals.items():
    print country, capital

# Alle Länder meiner Liste
print capitals.keys()
print capitals.values()

