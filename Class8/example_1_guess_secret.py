secret = 22
guess = None

# From Tutorial Class 8
# Run with debugger
# Go to break point / go to next line
# Console work with the code (Show python prompt)

while True:
    guess = int(raw_input("Guess the secret number (between 1 and 30): "))

    if guess == secret:
        print "You guessed it - congratulations! It's number 22 :)"
    else:
        print "Sorry, your guess is not correct... Secret number is not " + str(guess)