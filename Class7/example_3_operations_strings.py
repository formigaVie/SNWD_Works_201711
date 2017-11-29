# Variablendefinition
greeting = "Hello, World!" #= Zuweisungsoperator
name = "formigaVIE"

#Ausgabe
print greeting

print greeting + " - AI" # concat

print "*" * 30 #* Operator

print "Greeting:%s, Name: %s" %(greeting, name) # alte Variante
print "Greeting2: {}, Name2: {}".format(greeting, name) #.format ist fuer alle Datendatenbank

# == Vergleich der Werte
print greeting == name
print greeting == "Hello, World!"

# erste Zeile Strings -> die concatonated werden
# zweite Zeile sTrings in Int umwandeln daher wird es addiert
print "3" + "3"
print int("3")+int("3")

# Testfall fuer Ausgabe -> TypeError
#print int("3") + "3"

#Strings nur dann in Integer umwandeln wenn es eine ganze Zahl ist -> ValueError
# print int("a")