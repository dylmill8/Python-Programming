from random import *

def randomNumber():

    numb = randint(0,10)
    guess = eval(input("What do you think the number is (0-10)? "))
    
    while guess != numb:
        guess = eval(input("What do you think the number is (0-10)? "))

    print("Congrats you got it!")

randomNumber()
