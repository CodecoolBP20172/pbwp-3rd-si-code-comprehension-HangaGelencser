#Guessing numbers

import random #Imports random module from library

guessesTaken = 0 # Assign value(0) to variable

print('Hello! What is your name?') # prints the question in the breq	brackets
myName = input() # Assign input to variable (myName)

number = random.randint(1, 20) # Returns a random integer between 1-20
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.') # Prints a sentence, with inserted variable (myName)

while guessesTaken < 6: # While loop executes the target statement as long as guessesTaken < 6 is True
    print('Take a guess.') # Prints a sentence
    guess = input() # Asking input for a variable
    guess = int(guess) # Converts guess variables value from a string to an integer

    guessesTaken += 1 # Adds one to guessesTaken variable, while changing the variable itself in process

    if guess < number: # Using if condition to compare if guess variable is smaller than number
        print('Your guess is too low.') # If the condition is True, it prints a sentence reflectted on the actual condition

    if guess > number: # Using if condition again to decide if guess variable is bigger than number
        print('Your guess is too high.') # If the condition is True, it prints a sentence reflectted on the actual condition

    if guess == number: # Using if condition with equal operation
        break # If this condition is True, then it breaks out from the innermost, enclosing while loop

if guess == number: # With if condition it checks, if guess variable and number variable is equal
    guessesTaken = str(guessesTaken) # If the condition is True, it convert guessesTaken variable to string
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!') # Prints a sentence reflected on the main task, inserting myName variable and guessesTaken variable

if guess != number: # With if condition it checks, if guess variable is not equal to number variable
    number = str(number) # If True, it converts number to a string
    print('Nope. The number I was thinking of was ' + number) # Prints a sentence reflected on it, with number variable added to it
