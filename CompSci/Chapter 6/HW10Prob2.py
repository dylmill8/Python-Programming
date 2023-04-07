#Dylan Miller

#This program will allow the user to input an image and then will allow them
#to click over the faces in the image to cover them with a smily face

#imports graphics and math libraries
from graphics import *
from math import *

#This function will break down 2 points into their x and y values and use
#them to calculate the distance between the points using distance formula
    #parameters: P1 - first point
                #P2 - second point
def distance(p1,p2):
    x1 = p1.getX()
    y1 = p1.getY()
    x2 = p2.getX()
    y2 = p2.getY()
    distance = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    return(distance)

#creates a face at the points that the user clicked
    #parameters: p - first click (center of circle)
                #r - radius of circle determined by distance function
                #win - window that it will be drawn in
def face(p,r,win):

    #creates a circle at center point with the radius equal to the distance
    #between the two points that were clicked
    circle = Circle(p,r)
    circle.setFill("yellow")
    circle.draw(win)

    #gets the x and y of the center point to use as refrences for drawing
    #the features of the face
    x = p.getX()
    y = p.getY()

    #creates left and right eye as well as a smilebased on a ratio of
    #the radius to have the eyes change size based on the size of the face
    eyeL = Circle(Point(x-(r/3),y-(r/3)),r/10)
    eyeL.setFill("black")
    eyeL.draw(win)
        
    eyeR = Circle(Point(x+(r/3),y-(r/3)),r/10)
    eyeR.setFill("black")
    eyeR.draw(win)

    smile = Polygon(Point(x+(r/3),y),Point(x-(r/3),y),Point(x,y+(r/4)))
    smile.setFill("red")
    smile.draw(win)

#This will take the users image imput, number of faces they need to cover, and
#create the window to interact with the image
    #parameters: none
def main():

    image = str(input("Photo to import (ppm, gif, or png): "))
    numbFaces = int(input("Number of faces to cover: "))
    print("For each face, click the center and a point on the edge")

    #creates the image at a point so we can check the width and length
    #for the window that will be created later
    size = Image(Point(0,0),image)
    width = size.getWidth()
    height = size.getHeight()

    #creates a window using the width and height of the image and draws the
    #image into the window
    win = GraphWin("Photo Anonymizer",width,height)
    image = Image(Point(width/2,height/2),image)
    image.draw(win)

    #repeats for the number of faces you chose to have
    for i in range(numbFaces):

        #sets center to the first click and the outer edge to the second click
        center = win.getMouse()
        outer = win.getMouse()

        #for every circle it will calculate the radius using the distance
        #function and the center and outer click that were just set
        radius = distance(center,outer)

        #creates the face using the radius found by the distance
        face(center,radius,win)

    #after all faces are comeplete the window waits to recieve a click and closes
    win.getMouse()
    win.close()

main()
