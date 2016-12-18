# Cows and Bulls - a guerssing of a number game
import random
import sys
import os
from random import randint

#code = "%d%d%d%d" % (randint(0,9), randint(0,9), randint(0,9), randint(0,9))

comp_number = str(random.randrange(1000,10000))

def checkDigitLocation(a,b):
    cows = 0
    bulls = 0
    for i in range(0,len(a)):
        for y in range(0,len(b)):
            if (a[i] == b[y]):
                if i == y:
                    cows += 1
                else:
                    bulls += 1
    return (cows, bulls)

def checkGuessRange(a):
    print "checking %r" % a
    while (True):
        if ((int(a) > 999) and (int(a) < 10000)):
            #guess_str = guess
            print "Your guess is %r" % a
            break
        else:
            a = raw_input("Fucker!! only FOUR guess:  ")
    return a

#guess = raw_input("Enter your four digit guess:  ")
new_guess = 0
guess_count = 0

while (guess_count < 10):
    print "looping around %r \n" % guess_count
    if (new_guess == comp_number):
        print "*" *30
        print "GOOD JOB!!!"
        print "*" *30
        break
    else:
        new_guess = raw_input("Enter your four digit guess:  ")
        a = checkGuessRange(new_guess)
        print "Cows = %r, and Bulls = %r" % checkDigitLocation(comp_number,a)
        print "This is your %r guess, you have %r left" % (guess_count,10-guess_count)
        guess_count += 1
        print "Computer Numner is %r" % comp_number
