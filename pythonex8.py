

from random import randint


num = int(raw_input("Guess a number between 1 and 9:"))

a = randint(1, 9)

guessNumber = 0


while a != num:
    
    if a > num:
        print "Too low!"
        print "The number was %d " % a
        raw_input("Would you like to play again?? press enter")
        num = int(raw_input("Guess a number between 1 and 9:"))
        guessNumber = guessNumber + 1
        
    elif a < num:
        print "Too high"
        print "The number was %d " % a
        raw_input("Would you like to play again?? press enter")
        num = int(raw_input("Guess a number between 1 and 9:"))
        guessNumber = guessNumber + 1
        
    elif a == num:
        print "You are right!!"
        print "It took you %r guesses!" % guessNumber
        break