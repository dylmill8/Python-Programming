
#Dylan Miller

#These programs are practicing with functions imported from the math library

#This function will find the remaining side and two angle measures
#in degrees of an SAS triangle
    #parameters: a = side a (given)
                #gamma = angle opposite to side c (given)
                #b = side b (given)
                #cosDeg = store the value of the cosine of angle gamma
                #calcSide = stores the law of cosines formula
                #sideC = final value of side C
                #beta = value of angle beta
                #s = semiperimeter of the trangle
                #area = final area of the triangle (using herons formula)

#imports math library for all future programs
import math

def SAS(a,gamma,b):
    #finds cosine of gamma
    cosDeg = math.cos(math.radians(gamma))
    
    #plugs into the law of cosines to find side c using math library functions
    calcSide = a**2 + b**2 - 2*b*a * cosDeg
    sideC = math.sqrt(calcSide)
    print("Side C =",round(sideC,2))

    #finds angle beta then alpha by subtracting gamma and beta from 180
    beta = b * (gamma/sideC)
    print("Angle Beta =",round(beta,2))
    print("Angle Alpha =",round(180 - beta - gamma,2))

    #finds the semiperimeter of the triangle using sies we calculated
    s = (a + b + sideC)/2

    #plugs in all the values we have collected into herons formula to find area
    area = math.sqrt(s * (s - a)*(s - b)*(s - sideC))
    print("The area of the triangle is:",round(area,2))

#-----

#This function convers any binary number into a 'normal' number
    #perameters: total = total amount after adding up all digits
                #binNumb = user input binary number
                #digit = current digit being manipulated in the sequence

def fromBinary():
    total = 0

    #takes the integer of the input so the user
    binNumb = int(input("Give me a binary number and I will convert it: "))

    #repeats for the length of the string of numbers (repeats for each digit)
    for i in range(len(str(binNumb))):

        #divides by 10 and takes remainder to find the current digit in the
        #sequence
        digit = binNumb % 10

        #uses integer division to remove the last digit in the binary
        #number for the next time it loops
        binNumb = binNumb // 10

        #only manipulates the total if the binary number is non-zero
        if digit > 0:
            total = (2 ** i) + total
    print(total)

#-----

#This function converts any number into binary
    #parameters: numb = the user input number to be converted
                #log = holds the value of the log of the remaining number
    
def toBinary():
    #prevents decimal inputs
    numb = int(input("Give me a number and I will convert it to binary: "))

    #repeats for the length of the highest power of 2 that is less than
    #the number. This essentially allows the loop to start from the highest
    #possible number and work its way down to 0
    for i in range(math.trunc(math.log2(numb)),-1,-1):

        #This means that if the value of 2**i (the current power of 2) is
        #greater than the current total then it will print 0
        if (2**i > numb):
            print(0, end = " ")

        #If the power fits within the total then we calculate the new total
        #and add a 1 to the sequence
        else:

            #takes greatest possible power of 2 that fits within the total
            log = math.trunc(math.log2(numb))

            #sets the new total of the number for the next loop
            numb = numb - (2**log)
            #not working couldn't figure out why: print(math.trunc(log) % 2)
            #sometimes it was printing 0 instead of 1 so I simplified it
            #with the if else functions and it ended up being more efficient
            print(1, end = " ")
