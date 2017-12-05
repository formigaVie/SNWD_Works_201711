#!/usr/bin/env python
# -*- coding: UTF-8 -

a_dict = {}
points = {"alfred":10,
          "bettina":100,
          "christian":50,
          "doris":75}

print points # {'christian': 50, 'bettina': 100, 'doris': 75, 'alfred': 10}

# reference
print points ["alfred"]

for name in ["alfred", "bettina"]:
    print name, points [name]

# change
points["alfred"] = 30
print points
points["franz"] = 40
print points

for name in ["alfred", "bettina"]:
    points [name] += 10
    print points

# update
points.update({"erwin":-10,"alfred":200})
print points