#Dylan Miller

#These programs are practicing with loops to perform calculations
#based on the user's input

#This function calculates a person's IRA based on the information they
#provide about their interest rate, how often it is compounded, etc.
#   prameters: monthlyCont = user's montly contribution
              #interstRate = user's interest rate
              #years = how long user plans to invest
              #total = total amount in IRA
              #roundedTotal = total rounded to the nearest cent

def ira():
    #prints a series of statements asking for and evaluating
    #information regarding their interest rate and other necessary info
    print("I will calculate how much you've saved for retirement!")
    monthlyCont = eval(input("Enter your monthly contribution: "))
    interestRate = eval(input("Enter your interest rate: "))
    years = eval(input("Enter the number of years you plan to invest: "))
    total = 0

    #creates a loop that repeats for the number of years the person
    #wants to invest
    for i in range (years):

        #within each year is a loop that calculates interest compounded
        #montly as well as adds the monthly contibution amount
        for i in range (12):
            total = (total * interestRate/12) + total
            total = total + monthlyCont

    #rounds the total to a dollar ammount to the nearest cent
    #and prints the results to the user
    roundedTotal = round(total,2)
    print("After",years,"years, you will have $",roundedTotal," in your IRA")

#-----

#averages the scores of the user's assignments that they input
    #perameters: total = total of all the scores before they are divided
                #newScore = latest input score to be added to the total
                #numbScores = amount of scores the user wishes to input
    
def averageScore():
    total = 0

    #evaluates how many scores user has to input
    numbScores = eval(input("How many scores do you have to enter? "))

    #repeats for the number of scores the user wanted to enter in
    for i in range (numbScores):

        #sets the latest score input to newScore variable
        newScore = eval(input("Enter score: "))

        #calculates and averages the total by adding all the scores and
        #dividing my numbScores
        total = total + newScore
    print("the average of those scores is",round(total/numbScores),"percent!")

#-----

#This function converts a series of mesurements in feet to inches
    #peramerters: feet = list of lengths in feet

def convert():

    #asks user to provide the input
    print("This function will convert a set of lengths measured", end ="")
    print("in feet to inches.")
    feet = eval(input("Enter a list of lengths in feet: "))
    print("Those lengths in inches are:", end = " [ ")

    #repeats for the amount of numbers in the list
    for i in (feet):
        print(i*12, end = " ")
    print("] ")
        
#-----

#This function tells the user how many triangular numbers there are in all
#of the triangles leading up to their choice
    #peramerters: n = the amount of layers the user wants to calculate
                 #total = total amount of triangluar numbers in a given layer
                 #layer = adds the necessary amount each time
                          #we increase by one layer

def triangle(n):
    total = 0
    layer = 1
    print(0, end = ", ")

    #for every layer, it will increase "layer" by 1 and add it to total
    #add2 will set layer to 2 after the first calculation which allows it
    #to print 1 before continuing on with the pattern.
    for i in range (n):
        total = total + layer
        layer =  layer + 1

        #if the layer is not the last one being calculated it will
        #appear with a comma, if it is the last, it will have a period
        if (i < n-1):
            print(total, end =", ")
        else:
            print(total, end =".")
