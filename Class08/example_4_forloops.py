#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# zahlen bis 100

# wenn die Zahl gerade: print "yu"
# wenn die zahl ungerade und groeßer 50: print "yo"
# wenn die zahl kleiner als 20 print: "ye"
# sonst print die zahl

# 2 -> yu
# 51 -> yo
# 19 -> ye
# 35 -> 35

number = raw_input("\nPlease select a number between 1 and 100: ")
print "Selected value {}" .format(int(number))
for number in range(1,int(number)+1):
    if number % 2 == 0:
        print "yu", number
    elif number %2 != 0 and number > 50:
        print "yo", number
    elif number < 20:
        print "ye", number
    else:
        print number
    # Pass als möglichkeit nichts zu tun
    # pass