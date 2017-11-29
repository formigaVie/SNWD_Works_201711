# print welcome to user
name = "FormigaVIE"
print "Welcome to {} calculator" .format(name)
print "=" *40

# read user input for operation
# mit CTRL + P zwischen eckiger Klammer zeigt an was dort hineinkommt - Funktion raw input
operation_symbol = raw_input("Please enter an operation (+,-,*,/): ")
print "You entered " + operation_symbol

# calculate
if operation_symbol == "+" or operation_symbol == "-" or operation_symbol == "*" or operation_symbol == "/":
    # read user input for first value
    # string in einen Integer fuer die Berechnung durchfuehren
    x = float(raw_input("Please enter your first value: "))
    print "You entered " + str(x)
    # read user input for second value
    y = float(raw_input("Please enter your second value: "))
    # print "You entered ", y andere Schreibweise
    print "You entered " + str(y)
    if operation_symbol == "+":
        print x + y
    elif operation_symbol == "-":
        print x - y
    elif operation_symbol == "/":
        print x / y
    elif operation_symbol == "*":
        print x * y
else:
    print "Invalid input, try again"
# print result
