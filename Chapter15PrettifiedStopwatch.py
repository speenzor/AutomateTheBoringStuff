#! /usr/bin/env python3

#Automate The Boring Stuff Chapter 15 - Prettified Stopwatch
#This program will make a nice looking stopwatch that stars when you press enter
#and then prints out laps when you press enter.

import time, pprint

#Display the program's instructions
print('Press ENTER to begin. Afterwards, press Enter to "click" the stopwatch. Press Ctrl-C to quit.')
input()                     #press Enter to begin
print('Started.')
startTime = time.time()     #get the first lap's start time
lastTime = startTime
lapNum = 1

#Start tracking the lap times.
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #'.ljust(5) + (str(lapNum)+':').rjust(3) + (str(totalTime)+' (').rjust(8) + (str(lapTime)+')').rjust(6))
        lapNum += 1
        lastTime = time.time()  #reset the last lap time
except KeyboardInterrupt:
    #Handle the Ctrl-C exception to keep the error message from displaying
    print('\nDone.')
