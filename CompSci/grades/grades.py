#Dylan Miller

#This program displays the grades of students (obtained from a separate file)
#in a class as a bar graph
    #parameters: none

#imports graphics library
from graphics import *

def grades():

    #counts the number of \n characters in the file to find the total number of
    #lines in the file
    inputFile = open("input.py","r")
    numbGrades = inputFile.read()
    numbGrades = numbGrades.count("\n")
    inputFile.close()

    #this sets the size of the window and scales it to the total number of
    #student grades in the input file
    inputFile = open("input.py","r")
    win = GraphWin("grades",600,600)
    win.setCoords(0,-1,120,numbGrades)

    #loops for the number of lines (student data) in the imput file
    for i in range(numbGrades):

        #separates the initials and number grade from each line
        text = inputFile.readline()
        text = text[:-1]
        initials = text[0:2]
        grade = float(text[3:])

        #determines the letter grade that the student recieves based on their
        #number grade in the class
        if grade >= 90:
            letterGrade = "A"
        if 80 <= grade < 90:
            letterGrade = "B"
        if 70 <= grade < 80:
            letterGrade = "C"
        if 65 <= grade < 70:
            letterGrade = "D"
        if grade < 65:
            letterGrade = "F"

        #Positions the number/letter grade in the center of each bar
        #in the graph and positions the initials along the left edge
        numbText = Text(Point(10+(grade/2),i),str(grade)+"% ("+letterGrade+")")
        numbText.draw(win)
        initialText = Text(Point(5,i),initials)
        initialText.draw(win)

        #displays the automatically scaling recatangles (bars) in the graph
        rect = Rectangle(Point(10,i-.25),Point(10+grade,i+.25))
        rect.draw(win)

    #closes the input file at the end and waits for a mouse click
    #to close the window
    inputFile.close()
    win.getMouse()
    win.close()

#calls the function automatically when the file is run
grades()
