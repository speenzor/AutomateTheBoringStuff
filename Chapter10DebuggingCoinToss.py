#! /usr/bin/env python3

"""Automate the Boring Stuff Chapter 10 Challenge - Debugging Coin Toss

The author gives us a program that is a simple coin toss guessing game.
The challenge is to find the bugs. What is below is the de-bugged version
of the coin toss game script given by the book.
"""

import random

guess = ''
while guess not in ('heads','tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

toss = random.randint(0,1) #0 is tails, 1 is heads
toss_landing = ['tails','heads']

if toss_landing[toss] == guess:
    print ('You got it!')
else:
    print ('Nope! Guess again!')
    guess = input()
    if toss_landing[toss] == guess:
        print ('You got it!')
    else:
        print ('Nope. You are really bad at this game.')
