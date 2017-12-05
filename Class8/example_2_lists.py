a_list = []
b_list = [1,2,3,4]
c_list = ()
d_list = (5,6,7,8)
print a_list
print b_list
print c_list
print d_list
# referenzieren
# print a_list[0] # IndexError, because has no elements
print b_list[1]  #2
b_list [1]=10
print b_list
# print c_list(0) # IndexError, because has no elements
# print d_list(2) # not callable
# d_list (1)=5  # SyntaxError, because immutable
print d_list
# slicen
print b_list[1:3]  #[10,3]
print b_list[1:-1] #[10,3]
print b_list[-2:] #[3,4]
print b_list[::-1] #[4,3,10,1]
print b_list[::-2] #[4,10] "-" bedeutet umkehren der reihenfolge
# [start : end : iterationrule]
# iteration rule < 0: reverse
# iteration rule = 2: every second value

# append
# Fuege an der letzten Stelle hinzu
b_list.append(5)
print b_list # [1,10,3,4,5]

# remove
# bezieht sich auf die Zahl und loescht erstes vorkommen
b_list.remove(3)
print b_list # [1,10,4,5]

#extend
# mehrere Werte an das Ende der Liste anfuegen
b_list.extend([0,77,99])
print b_list # [1,10,4,5,0,77,99]

b_list += [100,101]
print b_list # [1,10,4,5,0,77,99,100,101]
