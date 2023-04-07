#Dylan Miller

#this program implements Minesweeper with three difficulty leavels
#using a graph to represent the board
#and Breadth First Search (BFS) to discover new squares

from graphics import *
from MineClasses import *
from time import *

#sets up the board everytime the game starts/restarts
def boardSetup(difficulty):
    #size of board based on difficulty selected (default 1: 8 X 8)
    if difficulty == 2:
        size = 12
    elif difficulty == 3:
        size = 16
    else:
        size = 8
    #creates the graphics window
    win = GraphWin("Minesweeper", 800, 800)
    win.setCoords(size+.5,size+.5,-.5,-1.5)

    #resets the mines and number of turns to track between
    #games when difficulty changes or game restarts
    mines = 0
    numberTurns = 1

    #creates patterned colored squares
    tiles = []
    for i in range(size**2):
        tile = Rectangle(Point(i%size,i//size),Point((i%size)+1,(i//size)+1))
        tiles.append(tile)
    for i in range(len(tiles)):
        if i%(size*2) < size and i%2 == 0:
            #dark green
            tiles[i].setFill("#ABE96A")
        elif i%(size*2) >= size+1 and i%2 == 1:
            #dark green
            tiles[i].setFill("#ABE96A")
        else:
            #light green
            tiles[i].setFill("#B7FE61")
        tiles[i].draw(win)

    #quit button
    line = Line(Point(.75,-.5),Point(.25,-1)).draw(win)
    line.setFill("black")
    line.setWidth(4)
    line = Line(Point(.75,-1),Point(.25,-.5)).draw(win)
    line.setFill("black")
    line.setWidth(4)

    #difficulty button
    difficultySelect = Rectangle(Point(size,-.25),Point(size-2,-1.25)).draw(win)
    difficultySelect.setFill("#F0F0F0")
    text = Text(Point(size-1,-.75),"Difficulty   ▼").draw(win)
    text.setSize(16)

    #flags remaining icon
    flagsPlaced = {}
    counter = 10*(difficulty**2)
    flag = Image(Point((size/2)+.25,-.75), "flag_icon.png").draw(win)
    flagsRemaining = Text(Point((size/2)-(difficulty/4),-.75),str(counter)).draw(win)
    flagsRemaining.setSize(30)
    
    return win,tiles,size,difficulty,mines,flagsRemaining,counter,flagsPlaced,numberTurns

#checks where the user clicked and performs any of the actions
#possible on a mouse click
def clickActions(win,tiles,size,difficulty,mines,flagsRemaining,counter,flagsPlaced,end,numberTurns):
    click = win.getMouse()

    #checks if quit button is clicked
    if .25 <= click.getX() <= .75 and -1 <= click.getY() <= -.5:
        #closes the window
        win.close()
        #sets the loss condition to prevent game from restarting
        counter = False
        return win,tiles,size,difficulty,mines,flagsRemaining,counter,flagsPlaced,end,numberTurns

    #if difficulty button is clicked close and open selection window
    if size-2 <= click.getX() <= size and -1.25 <= click.getY() <= -.25:
        win.close()
        #sets a new difficulty
        difficulty = difficultySelect()
        #ends the current game
        end = True
        return win,tiles,size,difficulty,mines,flagsRemaining,counter,flagsPlaced,end,numberTurns
    
    #creates matrix of tiles and generates mines if this is the users first turn
    #and the click is within the board
    if numberTurns == 1 and 0 <= click.getX() <= size and 0 <= click.getY() <= size:
        mines = mine(size)
        #scales the number of mines generated bsed on board size (10,40,90)
        mines.generateMines(10*(difficulty**2),int(click.getX())+(int(click.getY())*size)+1) #number of mines by difficulty
        numberTurns += 1
    
    #if user pressed shift before click, place flag
    if win.checkKey() == "Shift_L" and 0 <= click.getX() <= size and 0 <= click.getY() <= size:
        win,flagsRemaining,counter,flagsPlaced = flagClicked(win,flagsRemaining,counter,flagsPlaced,click,size,1)
        
    #if click is within grid
    elif 0 <= click.getX() <= size and 0 <= click.getY() <= size:
        #if user clicked a mine
        if mines.clickedMine(int(click.getX())+(int(click.getY())*size)+1) == True:
            #color tile red
            tiles[int(click.getX())+(int(click.getY())*size)].setFill("red")
            #display all bomb locations across the board
            for i in range(size**2):
                if mines.clickedMine(i+1)==True:
                    point = tiles[i].getCenter()
                    bomb = Image(point, "bomb_icon.png")
                    bomb.draw(win)
                    
            #restart button on a loss
            restart = Rectangle(Point(size,-.25),Point(size-2,-1.25)).draw(win)
            restart.setFill("#F0F0F0")
            text = Text(Point(size-1,-.75),"Restart").draw(win)
            text.setSize(16)

            #loss text
            text = Text(Point(size/2,size/2),"YOU LOSE!").draw(win)
            text.setSize(36)
            text.setStyle("bold")

            #waits for user to restart or quit
            while True:
                click = win.getMouse()
                if .25 <= click.getX() <= .75 and -1 <= click.getY() <= -.5:
                    win.close()
                    #set quit condition
                    counter = False
                    return win,tiles,size,difficulty,mines,flagsRemaining,counter,flagsPlaced,end,numberTurns
                if size-2 <= click.getX() <= size and -1.25 <= click.getY() <= -.25:
                    win.close()
                    #end game and restart
                    end = True
                    return win,tiles,size,difficulty,mines,flagsRemaining,counter,flagsPlaced,end,numberTurns

        #set tile color to indicate it is revealed if it was not a mine
        else:
            bfs = mines.returnSquares(int(click.getX())+(int(click.getY())*size)+1)
            for i in bfs:
                #light brown
                tiles[i-1].setFill("#F0D8B6")
                #adds the revealed square to the list of flags so that
                #a flag cannot be placed on a revealed square
                win,flagsRemaining,counter,flagsPlaced = flagClicked(win,flagsRemaining,counter,flagsPlaced,Point(((i-1)%size),((i-1)//size)),size,0)
                #gets the number of adjacent bombs
                number = mines.returnNumber(i)
                #draw the number on the window if it is greater than 0
                if number != 0:
                    text = Text(Point(((i-1)%size)+.5,((i-1)//size)+.5),str(number)).draw(win)
                    text.setSize(30)
                    #set the appropriate text color
                    if number == 1:
                        text.setFill("blue")
                    elif number == 2:
                        text.setFill("green")
                    elif number == 3:
                        text.setFill("red")
                    elif number == 4:
                        text.setFill("dark blue")
                    elif number == 5:
                        text.setFill("maroon")
                    elif number == 6:
                        text.setFill("teal")
                    elif number == 7:
                        text.setFill("black")
                    elif number == 8:
                        text.setFill("grey")

    return win,tiles,size,difficulty,mines,flagsRemaining,counter,flagsPlaced,end,numberTurns

#manages a dictionary of flags where the key is the position of the square
#and the value is the image object
def flagClicked(win,flagsRemaining,counter,flagsPlaced,click,size,x):
    flagKey = (int(click.getX())+(int(click.getY())*size))+1
    keys = flagsPlaced.keys()
    #if there is already a flag at the square
    if flagKey in keys:
        #if the key to the flag is 0 (revealed square) then just return
        if flagsPlaced.get(flagKey) == 0:
            return win,flagsRemaining,counter,flagsPlaced
        
        #otherwise undraw the flag
        else:
            flagsPlaced.get(flagKey).undraw()
            #adjust the counter and delete the flag from the dictionary
            counter += 1
            del(flagsPlaced[flagKey])
            
    #if input x is 0
    elif x == 0:
        #set the key of the square to 0 meaning that it is a square that
        #was revealed so no flags can be placed on it
        flagsPlaced[flagKey] = 0

    else:
        #draw a flag at the point clicked
        flag = Image(Point(int(click.getX())+.5,int(click.getY())+.5), "flag_icon.png")
        flag.draw(win)
        #adjust counter
        counter -= 1
        #save the image object in the value
        flagsPlaced[flagKey] = flag
    
    flagsRemaining.setText(str(counter))
        
    return win,flagsRemaining,counter,flagsPlaced

#creates a new window to select difficulty levels
def difficultySelect():
    win = GraphWin("Difficulty Select", 400, 400)
    win.setCoords(-.5,-.5,3.5,3.5)

    #creates different difficulty buttons
    button = Rectangle(Point(0,2.25),Point(3,3.25)).draw(win)
    button.setFill("#F0F0F0")
    text = Text(Point(1.5,2.75),"Easy: 8 X 8").draw(win)
    text.setSize(36)
    
    button = Rectangle(Point(0,1),Point(3,2)).draw(win)
    button.setFill("#F0F0F0")
    text = Text(Point(1.5,1.5),"Medium: 12 X 12").draw(win)
    text.setSize(36)
    
    button = Rectangle(Point(0,-.25),Point(3,.75)).draw(win)
    button.setFill("#F0F0F0")
    text = Text(Point(1.5,.25),"Hard: 16 X 16").draw(win)
    text.setSize(36)

    #checks to see which button is clicked and returns chosen difficulty
    while True:
        click = win.getMouse()
        if 0 <= click.getX() <= 3 and 2.25 <= click.getY() <= 3.25:
            win.close()
            return 1
        elif 0 <= click.getX() <= 3 and 1 <= click.getY() <= 2:
            win.close()
            return 2
        elif 0 <= click.getX() <= 3 and -.25 <= click.getY() <= .75:
            win.close()
            return 3

#runs the minesweeper game
def main():
    #sets default to play again until user quits
    playAgain = True
    #sets default difficulty
    difficulty = 1
    
    while playAgain == True:

        #initial board setup
        win,tiles,size,difficulty,mines,flagsRemaining,counter,flagsPlaced,numberTurns = boardSetup(difficulty)
        end = False

        #while the player has not won or lost
        while end is not True:

            #get a click
            win,tiles,size,difficulty,mines,flagsRemaining,counter,flagsPlaced,end,numberTurns = clickActions(win,tiles,size,difficulty,mines,flagsRemaining,counter,flagsPlaced,end,numberTurns)

            #checks for win condition
            if counter == 0 and len(flagsPlaced) == size**2:
                #restart button
                restart = Rectangle(Point(size,-.25),Point(size-2,-1.25)).draw(win)
                restart.setFill("#F0F0F0")
                text = Text(Point(size-1,-.75),"Restart").draw(win)
                text.setSize(16)

                #win text
                text = Text(Point(size/2,size/2),"YOU WIN!").draw(win)
                text.setSize(36)
                text.setStyle("bold")

                #waits for user to quit or restart
                while True:
                    click = win.getMouse()

                    #sets quit condition
                    if .25 <= click.getX() <= .75 and -1 <= click.getY() <= -.5:
                        win.close()
                        counter = False
                        break

                    #ends game and restarts
                    if size-2 <= click.getX() <= size and -1.25 <= click.getY() <= -.25:
                        win.close()
                        end = True
                        break

            #checks for quit condition and breaks loop
            if counter is False:
                playAgain = False
                break
                
main()
