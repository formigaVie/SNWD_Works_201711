import random

countg = []
guess = int(raw_input("Please enter how many random numbers would you like to have: "))
for i in range(0, guess + 1):
    if i < int(guess):
        lotto = random.randint(0, 45)
        countg.append(lotto)
    else:
        pass
print countg