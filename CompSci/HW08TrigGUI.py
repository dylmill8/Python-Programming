#Dylan Miller

#This program displays the aproximation of a function as a graph
#acording to the user's specified minimum x and maximum x values
    #parameters: none

#imports graphics and math libraries to be called up later
from graphics import *

import math

def trig():

    #sets the tital and size of the window
    win = GraphWin("HW08TrigGUI", 600, 600)

    #this creates and displays the text that acompanies the entry boxes
    #allowing the user to chose their minimum and maximum x values and
    #the interval of points that will be graphed
    textMinX = Text(Point(150,30),"minimum x-value?")
    textMaxX = Text(Point(300,30),"maximum x-value?")
    textPoints = Text(Point(450,30),"How many points?")
    textMinX.draw(win)
    textMaxX.draw(win)
    textPoints.draw(win)

    #this creates entry boxes for the user to enter inputs
    entryMinX = Entry(Point(150,90),5)
    entryMaxX = Entry(Point(300,90),5)
    entryPoints = Entry(Point(450,90),5)
    entryMinX.draw(win)
    entryMaxX.draw(win)
    entryPoints.draw(win)

    #displays continue text when the user is done entering numbers
    textContinue = Text(Point(300,300),"Click anywhere to continue!")
    textContinue.draw(win)

    #waits for a mouse click confirming that the user is done inputing
    #values, then sets variables equal to the data in each entry box
    win.getMouse()
    minX = entryMinX.getText()
    maxX = entryMaxX.getText()
    points = entryPoints.getText()

    #undraws the entry boxes and text to prepare for the graph
    textContinue.undraw()
    entryMinX.undraw()
    entryMaxX.undraw()
    entryPoints.undraw()
    textMinX.undraw()
    textMaxX.undraw()
    textPoints.undraw()

    #checks to make sure the lowest value is stored in minX and if not
    #it switches minX and maxX
    if int(minX)>int(maxX):
        minX, maxX = maxX, minX

    #displays the domain as text across the x axis (shown as a line)
    xAxis = Line(Point(50,300),Point(550,300))
    xAxis.draw(win)
    xMinLabel = Text(Point(30,300),str(minX))
    xMinLabel.draw(win)
    xMaxLabel = Text(Point(570,300),str(maxX))
    xMaxLabel.draw(win)

    #finds the scale of the graph/how many pixels correspond to 1 unit
    #on the domain and range by dividing the number of pixels by the
    #range on the x and y axes
    xPixelUnit = 500/(int(maxX) - int(minX))
    yPixelUnit = 500/10

    #checks if the domain that the user chose includes 0 and if so draws the
    #y-axis at the appropriate position on the x axis
    if int(minX) <= 0 <= int(maxX):

        #finds the absolute value of the minX (distance from 0), which is
        #negative since the program checked if minX <= 0
        yInt = abs(int(minX))

        #draws a line at the correct x position on the graph by taking the
        #pixels per unit and multipying that by the distance from 0
        yAxis=Line(Point(50+xPixelUnit*yInt,550),Point(50+xPixelUnit*yInt,50))
        yAxis.draw(win)

        #labels the max and min y values on the y axis
        yMinLabel = Text(Point(50+xPixelUnit*yInt,570),"-5")
        yMinLabel.draw(win)
        yMaxLabel = Text(Point(50+xPixelUnit*yInt,30),"5")
        yMaxLabel.draw(win)

    #if the y axis is not included in the domain then only the
    #y min and max is displayed
    else:
        yMinLabel = Text(Point(30,550),"-5")
        yMinLabel.draw(win)
        yMaxLabel = Text(Point(30,50),"5")
        yMaxLabel.draw(win)

    #states the clone point upfront to avoid an error that occures when
    #the program defines a line including the point clonePoint without
    #defining it first, so these statements set the clonePoint to the position
    #of the first point/minX
    yValue = (3*(math.sin(int(minX)/2)))-(math.cos((2*int(minX))+(math.pi/4)))
    clonePoint = Point(50,300 - (yPixelUnit*yValue))

    #loops for the duration of the minimum x value to the maximum x value
    #(including the max) with an interval of the domain of x divided by the
    #interval determined by the user (min,max,n)
    for i in range(int(minX),int(maxX)+1,(int(maxX)-int(minX))//int(points)):

        #finds the y value of the x coordinate we plug in using the math library
        yValue = (3*(math.sin(i/2)))-(math.cos((2*i)+(math.pi/4)))

        #defines a point at the x value (i) that we are on and the y value
        #that was just calculated using the pixels per unit
        point = Point(50 + (xPixelUnit*(i-int(minX))),300 - (yPixelUnit*yValue))

        #graphs a line from the clonePoint (previous point saved as a clone) to
        #the current point, essentially connecting the last point to the current
        #point with a line
        graph = Line(clonePoint,point)

        #defines the clonePoint as the current point in the loop so that
        #next time the program repeats, the old point is stored within the clone
        clonePoint = point.clone()
        graph.draw(win)
        clonePoint.draw(win)

    #waits for the user mouse input and closes the window
    win.getMouse()
    win.close()

#automatically calls the function when the file is run
trig()
