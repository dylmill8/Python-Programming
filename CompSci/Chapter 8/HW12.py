#Dylan Miller

from graphics import *

#This function will take a photo that the user specifies, convert it
#to greyscale, and save it as their specified file name
    #parameters: none
def greyscale():

    image = str(input("Photo to import (ppm, gif, or png): "))

    size = Image(Point(0,0),image)
    width = size.getWidth()
    height = size.getHeight()

    win = GraphWin("Greyscale",width,height)
    image = Image(Point(width/2,height/2),image)
    image.draw(win)

    fileName = input("Name of save file: ")

    x = 0
    y = 0

    win.getMouse()

    #for the area of the image in pixels (pixel width * pixel height)
    for i in range (height * width):

        #sets the red, green, and blue color values of the pixel and sets
        #them to r, g, and b respectively
        r,g,b = image.getPixel(x,y)

        #converts the red, green, and blue values into the equivalent
        #color in greyscale and sets the pixel to that color
        grey =  int((0.3 * r) + (0.6 * g) + (0.1 * b))
        image.setPixel(x,y,color_rgb(grey,grey,grey))

        #Increases x by one to reach the next pixel and everytime it
        #reaches the end of a line it will take the remainder of x devided by
        #the width of pixels effectively reseting it to the start
        x = (x + 1) % width

        #if the remainder equals 0 (reached the end of a line)
        #then it will icrease y by 1 to go down to the next row
        if x == 0:
            y = y + 1

            #updates the image every line to create the scrolling effect
            update()

    #saves the image as the file name the user chose
    image.save(fileName)
    
    win.getMouse()
    win.close()

#This function will calculte the number of months and total cost to pay back a
#loan based on the amount of interest and the amount payed back every month.
    #parameters: none
def loanCalculator():
    
    print("Welcome to the Loan Calculator")
    answer = "yes"

    #it will repeat until the user enters anything besides "yes"
    #(I made it check for "y" to allow leniency for typos)
    while answer[0] == "y":
        balance = eval(input("\nAmount borrowed ($): "))
        apr = eval(input("Annual interest rate (decimal): "))
        perMonth = eval(input("Monthly payment ($): "))
        total = 0
        months = 0

        #while the balance is above 0 in other words, this will repeat
        #untill there is no more money that needs to be paid back
        while balance > 0:

            #gets the balance after adding interest
            balance = (balance * (1 + (apr/12)))
            
            #finds the current balance by subtrancting the amount
            #that was paid back
            current = balance - perMonth

            #increase the amount of months to pay the loan back by 1
            months = months + 1

            #moves the "current" to "balance" for the next loop
            #(balance = last month / current = current month)
            balance = current

        #finds the total using the amount of months to pay the loan and the
        #remainder from the last month's balance
        total = round((perMonth * months) + balance,2)
        
        print("\nYou will pay off the loan in",months,"months")
        print("In total, you will pay $"+str(total))
        
        #asks the user to continue if they enter "y" it will loop again
        #otherwise the program will terminate
        answer = str(input("\nWould you like to continue (yes/no)? "))

#This program acts as a menu to call the two functions based on the user's input
#(I know this wasn't required but it makes it easier to test each program)
        #parameters: none
def main():

    try:
        option = int(input("Choose greyscale (1) or loan calculator (2): "))
        if option == 1:
            greyscale()
        elif option == 2:
            loanCalculator()
        else:
            print("sorry that is not a valid response.")
    except NameError:
        print("Not the best with numbers I see...")
    except ValueError:
        print("Try whole numbers next time.")
    except:
        print("error")
        
main()
