# Name: Reilly Sheehan

from graphics import *
from GraphAdjMatrix import *
from DFSMaze import Maze


def start():
    "Starting window method"
    # Open a window
    win = GraphWin("Maze Dimensions",300,200)
    win.setBackground("RoyalBlue4")
    # Instructions
    text = Text(Point(150,40),"Enter the dimensions of the maze.")
    text.setFill("seashell")
    text.setSize(18)
    # Width Entry Box
    width = Entry(Point(100,85),5)
    width.setFill("seashell")
    width.setSize(18)
    width.setText("Width")
    # Height Entry Box
    height = Entry(Point(200,85),5)
    height.setFill("seashell")
    height.setSize(18)
    height.setText("Height")
    # Button Rectangle
    button = Rectangle(Point(50,130),Point(250,170))
    button.setFill("gray25")
    # Button Text
    buttonText = Text(Point(150,150),"Generate Maze")
    buttonText.setFill("seashell")
    buttonText.setSize(22)
    # Draw them all
    text.draw(win)
    width.draw(win)
    height.draw(win)
    button.draw(win)
    buttonText.draw(win)
    pt = win.getMouse()
    errorText = Text(Point(150,185),"Too big. Max area = 1000.")
    numberCheck = False
    
    # Get mouse until area is acceptable and Generate Maze button is clicked
    while not (100 <= pt.getX() <= 200 and 130 <= pt.getY() <= 170 and\
               numberCheck):
        
        # Check area if numbers have been entered
        try:
            if float(width.getText())*float(height.getText()) <= 1000:
                numberCheck = True
            else:
                numberCheck = False
        except:
            numberCheck = False
            
        # If numbers weren't good, display error message
        if numberCheck and float(width.getText())*float(height.getText()) > 1000:
            errorText.draw(win)
            pt = win.getMouse()
            errorText.undraw()
        else:
            pt = win.getMouse()
        errorText.undraw()

    win.close()
    
    return width.getText(),height.getText()

def generateMaze(x,y,maze):
    "Draws maze"
    # Open window
    win = GraphWin("Maze",700,800)
    # Divide 620  by 620 square by 3X width + 1 and 3X height + 1 : wall width is
    # one of those units, room width is two.
    wallWidth = 620/(2*int(x)+1+int(x))
    wallHeight = 620/(2*int(y)+1+int(y))
    roomWidth = 2*wallWidth
    roomHeight = 2*wallHeight
    # Top of first row start at 4
    top = 40
    bottom = 40+wallHeight
    # List of rectangles that will be black, empty spots don't need a rectangle
    rectList = []
    # First loop interates through y values; program draws all the rectangles in
    # one row before moving down one.
    for j in range(2*int(y)+1):
        # Each time through, starting x value is reset to far left side
        left = 40
        right = 40+wallWidth
        # Second loop iterates through x values
        for i in range(2*int(x)+1):
            # If there is an edge at this square, there needs to be a black
            # rectangle.
            if maze.isAdjacent(i,j):
                rect = Rectangle(Point(left,top),Point(right,bottom))
                # Start is green, end is red, all others are black
                if (i==0 and j==1):
                    rect.setFill("lime green")
                elif (i==2*x and j==2*x-1):
                    rect.setFill("red")
                else:
                    rect.setFill("black")
                rectList.append(rect)
            # When i is even, it is on a wall. Update left and right values to
            # border the room to the right.
            if i%2 == 0:
                left += wallWidth
                right += roomWidth
            # Vice versa, when i is odd, it is on a room. Update left and right.
            else:
                left += roomWidth
                right += wallWidth
        # Same concept for y values.
        if j%2 == 0:
            top += wallHeight
            bottom += roomHeight
        else:
            top += roomHeight
            bottom += wallHeight
    # Draw rectangles at end after all the math is complete for maximum drawing
    # speed (since there are so many tiny rectangles, it is already pretty slow
    # but this helps it go faster).
    for i in rectList:
        i.draw(win)
    # Quit button rectangle
    quitRect = Rectangle(Point(140,705),Point(260,755))
    quitRect.setFill("RoyalBlue4")
    quitRect.setOutline("RoyalBlue4")
    # Quit button text
    quitText = Text(Point(200,730),"QUIT")
    quitText.setSize(18)
    quitText.setFill("seashell2")
    # Play again button rectangle
    playRect = Rectangle(Point(440,705),Point(560,755))
    playRect.setFill("seashell2")
    playRect.setOutline("seashell2")
    # Play again button text
    playText = Text(Point(500,730),"PLAY AGAIN")
    playText.setSize(18)
    playText.setFill("RoyalBlue4")
    # Draw them all
    quitRect.draw(win)
    quitText.draw(win)
    playRect.draw(win)
    playText.draw(win)
    # Return win so that I can close it in the main function
    return win
    

def main():
    while True:
        # Get dimensions
        x,y = start()
        x,y = int(x),int(y)
        maze = Maze()
        # Get graph
        graph = maze.generateMaze(x,y)
        # Draw maze
        win = generateMaze(x,y,graph)
        # Get mouse until user clicks quit or play again
        pt = win.getMouse()
        while not ((705 <= pt.getY() <= 755) and ((140 <= pt.getX() <= 260) or \
                                                  (440 <= pt.getX() <= 560))):
            pt = win.getMouse()
        # Either way, close window
        win.close()
        # If quit, break out of while loop
        if  140 <= pt.getX() <= 260:
            break


main()
