#This is my solution to the Collatz function challenge at the end of Chapter 3

def collatz(number):
    number=int(number)
    try:
        while (number != 1):
            if (number % 2 == 0):
                print (number//2)
                number = number//2
            elif (number % 2 == 1):
                print (3*number+1)
                number=3*number+1
    except TypeError:
        print('Please enter integer.')
