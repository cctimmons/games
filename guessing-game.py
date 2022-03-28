import random


def getInput():
    print('inside input function')
    return input('enter a guess: ')


def randomNumber():
    print('inside random number')
    return random.randrange(1,10)

x = randomNumber()

y = getInput() 
if x == int(y):
    print('correct')
else:
    print('incorrect, the correct value is ' + str(x))
