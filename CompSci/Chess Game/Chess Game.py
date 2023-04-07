#Dylan Miller

#To Do:
#1 - Messages & Intro Text
#2 - King In Check
#3 - Promoting Pawns
#4 - Castling King & Rook
#5 - Checkmate (not capturing King)
#6 - En Passant
#7 - Displaying Taken Pieces Outside Board

from graphics import *
from math import *

class Piece:
    def __init__(self,color,name,coords,image):
        self.color = color
        self.name = name
        self.coords = coords
        self.image = image
        self.numbMoves = 0
        
    def getColor(self):
        return self.color

    def getName(self):
        return self.name

    def getCoords(self):
        return self.coords

    def setup(self,win):
        self.image.draw(win)

    def move(self,x2,y2):
        x,y = self.coords.getX(),self.coords.getY()
        x2,y2 = x2-x,y2-y
        x,y = x+x2,y+y2
        self.image.move(x2,y2)
        self.coords = Point(x,y)
        self.numbMoves = self.numbMoves + 1

    def capture(self):
        self.image.undraw()
        
class Pawn(Piece):
    def getMoves(self,whitePieces,blackPieces):
        if self.getColor() == "white":
            sameTeam = whitePieces
            enemyTeam = blackPieces
        else:
            sameTeam = blackPieces
            enemyTeam = whitePieces
        moves = []
        x,y = self.coords.getX(),self.coords.getY()
        if self.color == "white" and 1<y<7 and str(Point(x,y+1)) not in sameTeam and str(Point(x,y+1)) not in enemyTeam:
            moves = moves + [str(Point(x,y+1))]
            if self.numbMoves == 0 and str(Point(x,y+2)) not in sameTeam and str(Point(x,y+2)) not in enemyTeam:
                moves = moves + [str(Point(x,y+2))]
        if self.color == "black" and 1<y<7 and str(Point(x,y-1)) not in sameTeam and str(Point(x,y-1)) not in enemyTeam:
            moves = moves + [str(Point(x,y-1))]
            if self.numbMoves == 0 and str(Point(x,y-2)) not in sameTeam and str(Point(x,y-2)) not in enemyTeam:
                moves = moves + [str(Point(x,y-2))]
        if self.color == "white" and str(Point(x+1,y+1)) in enemyTeam:
            moves = moves + [str(Point(x+1,y+1))]
        if self.color == "white" and str(Point(x-1,y+1)) in enemyTeam:
            moves = moves + [str(Point(x-1,y+1))]
        if self.color == "black" and str(Point(x+1,y-1)) in enemyTeam:
            moves = moves + [str(Point(x+1,y-1))]
        if self.color == "black" and str(Point(x-1,y-1)) in enemyTeam:
            moves = moves + [str(Point(x-1,y-1))]
        if len(moves)>0:
            return moves
        else: return False

class Knight(Piece):
    def getMoves(self,whitePieces,blackPieces):
        if self.getColor() == "white":
            sameTeam = whitePieces
            enemyTeam = blackPieces
        else:
            sameTeam = blackPieces
            enemyTeam = whitePieces
        x,y = self.coords.getX(),self.coords.getY()
        moves = []
        for i in [1,-1]:
            if 0<y+i<8:
                if 0<x+2<8:
                    if str(Point(x+2,y+i)) not in sameTeam:
                        moves = moves + [str(Point(x+2,y+i))]
                if 0<x-2<8:
                    if str(Point(x-2,y+i)) not in sameTeam:
                        moves = moves + [str(Point(x-2,y+i))]
            if 0<y+(2*i)<8:
                if 0<x+1<8:
                    if str(Point(x+1,y+(2*i))) not in sameTeam:
                        moves = moves + [str(Point(x+1,y+(2*i)))]
                if 0<x-1<8:
                    if str(Point(x-1,y+(2*i))) not in sameTeam:
                        moves = moves + [str(Point(x-1,y+(2*i)))]
        if len(moves)>0:
            return moves
        else: return False
        
class Bishop(Piece):
    def getMoves(self,whitePieces,blackPieces):
        if self.getColor() == "white":
            sameTeam = whitePieces
            enemyTeam = blackPieces
        else:
            sameTeam = blackPieces
            enemyTeam = whitePieces
        x,y = self.coords.getX(),self.coords.getY()
        moves = []
        while 0<x+1<8 and 0<y+1<8 and str(Point(x+1,y+1)) not in sameTeam and str(Point(x,y)) not in enemyTeam:                
            moves = moves + [str(Point(x+1,y+1))]
            x = x+1
            y = y+1
        x,y = self.coords.getX(),self.coords.getY()
        while 0<x-1<8 and 0<y+1<8 and str(Point(x-1,y+1)) not in sameTeam and str(Point(x,y)) not in enemyTeam:
            moves = moves + [str(Point(x-1,y+1))]
            x = x-1
            y = y+1
        x,y = self.coords.getX(),self.coords.getY()
        while 0<x-1<8 and 0<y-1<8 and str(Point(x-1,y-1)) not in sameTeam and str(Point(x,y)) not in enemyTeam:
            moves = moves + [str(Point(x-1,y-1))]
            x = x-1
            y = y-1
        x,y = self.coords.getX(),self.coords.getY()
        while 0<x+1<8 and 0<y-1<8 and str(Point(x+1,y-1)) not in sameTeam and str(Point(x,y)) not in enemyTeam:
            moves = moves + [str(Point(x+1,y-1))]
            x = x+1
            y = y-1
        if len(moves)>0:
            return moves
        else: return False

class Rook(Piece):
    def getMoves(self,whitePieces,blackPieces):
        if self.getColor() == "white":
            sameTeam = whitePieces
            enemyTeam = blackPieces
        else:
            sameTeam = blackPieces
            enemyTeam = whitePieces
        x,y = self.coords.getX(),self.coords.getY()
        moves = []
        while 0<y-1<8 and str(Point(x,y-1)) not in sameTeam and str(Point(x,y)) not in enemyTeam:
            moves = moves + [str(Point(x,y-1))]
            y = y-1
        x,y = self.coords.getX(),self.coords.getY()
        while 0<y+1<8 and str(Point(x,y+1)) not in sameTeam and str(Point(x,y)) not in enemyTeam:
            moves = moves + [str(Point(x,y+1))]
            y = y+1
        x,y = self.coords.getX(),self.coords.getY()
        while 0<x-1<8 and str(Point(x-1,y)) not in sameTeam and str(Point(x,y)) not in enemyTeam:
            moves = moves + [str(Point(x-1,y))]
            x = x-1
        x,y = self.coords.getX(),self.coords.getY()
        while 0<x+1<8 and str(Point(x+1,y)) not in sameTeam and str(Point(x,y)) not in enemyTeam:
            moves = moves + [str(Point(x+1,y))]
            x = x+1
        if len(moves)>0:
            return moves
        else: return False
    
class Queen(Piece):
    def getMoves(self,whitePieces,blackPieces):
        if self.getColor() == "white":
            sameTeam = whitePieces
            enemyTeam = blackPieces
        else:
            sameTeam = blackPieces
            enemyTeam = whitePieces
        x,y = self.coords.getX(),self.coords.getY()
        moves = []
        while 0<y-1<8 and str(Point(x,y-1)) not in sameTeam and str(Point(x,y)) not in enemyTeam:
            moves = moves + [str(Point(x,y-1))]
            y = y-1
        x,y = self.coords.getX(),self.coords.getY()
        while 0<y+1<8 and str(Point(x,y+1)) not in sameTeam and str(Point(x,y)) not in enemyTeam:
            moves = moves + [str(Point(x,y+1))]
            y = y+1
        x,y = self.coords.getX(),self.coords.getY()
        while 0<x-1<8 and str(Point(x-1,y)) not in sameTeam and str(Point(x,y)) not in enemyTeam:
            moves = moves + [str(Point(x-1,y))]
            x = x-1
        x,y = self.coords.getX(),self.coords.getY()
        while 0<x+1<8 and str(Point(x+1,y)) not in sameTeam and str(Point(x,y)) not in enemyTeam:
            moves = moves + [str(Point(x+1,y))]
            x = x+1
        x,y = self.coords.getX(),self.coords.getY()
        while 0<x+1<8 and 0<y+1<8 and str(Point(x+1,y+1)) not in sameTeam and str(Point(x,y)) not in enemyTeam:                
            moves = moves + [str(Point(x+1,y+1))]
            x = x+1
            y = y+1
        x,y = self.coords.getX(),self.coords.getY()
        while 0<x-1<8 and 0<y+1<8 and str(Point(x-1,y+1)) not in sameTeam and str(Point(x,y)) not in enemyTeam:
            moves = moves + [str(Point(x-1,y+1))]
            x = x-1
            y = y+1
        x,y = self.coords.getX(),self.coords.getY()
        while 0<x-1<8 and 0<y-1<8 and str(Point(x-1,y-1)) not in sameTeam and str(Point(x,y)) not in enemyTeam:
            moves = moves + [str(Point(x-1,y-1))]
            x = x-1
            y = y-1
        x,y = self.coords.getX(),self.coords.getY()
        while 0<x+1<8 and 0<y-1<8 and str(Point(x+1,y-1)) not in sameTeam and str(Point(x,y)) not in enemyTeam:
            moves = moves + [str(Point(x+1,y-1))]
            x = x+1
            y = y-1
        if len(moves)>0:
            return moves
        else: return False
    
class King(Piece):
    def getMoves(self,whitePieces,blackPieces):
        if self.getColor() == "white":
            sameTeam = whitePieces
            enemyTeam = blackPieces
        else:
            sameTeam = blackPieces
            enemyTeam = whitePieces
        x,y = self.coords.getX(),self.coords.getY()
        moves = []
        for i in [1,-1]:
            if 0<y+i<8 and 0<x+i<8 and str(Point(x+i,y+i)) not in sameTeam:
                moves = moves + [str(Point(x+i,y+i))]

            if 0<y+i<8 and 0<x-i<8 and str(Point(x-i,y+i)) not in sameTeam:
                moves = moves + [str(Point(x-i,y+i))]
            if 0<x+i<8 and str(Point(x+i,y)) not in sameTeam:
                moves = moves + [str(Point(x+i,y))]
            if 0<y+i<8 and str(Point(x,y+i)) not in sameTeam:
                moves = moves + [str(Point(x,y+i))]                
        if len(moves)>0:
            return moves
        else: return False

def intro():
    win = GraphWin("Chess Board",800,800)
    win.setCoords(-1,-1,9,9)
    message = Text(Point(4,8.5),"Welcome To Chess!\n\n\n(click to continue)")
    message.draw(win)
    win.getMouse()
    return win,message

def GUI(win):
    linePos = 0
    offset = 0
    for k in range(8):
        for i in range(4):
            darkSquare = Rectangle(Point(linePos%8,linePos//8),Point(linePos%8+1,linePos//8+1))
            darkSquare.setFill("light blue")
            darkSquare.draw(win)
            linePos = linePos + 2
        if k%2 == 0:
            linePos = linePos + 1
        else: linePos = linePos - 1
    linePos = 0
    for i in range(9):
        line = Line(Point(linePos,0),Point(linePos,8)).draw(win)
        line = Line(Point(0,linePos),Point(8,linePos)).draw(win)
        linePos = linePos + 1
    letter = 65
    linePos = 0
    for i in range(8):
        boardLabel = Text(Point(linePos+.5,-.5),chr(letter)).draw(win)
        boardLabel = Text(Point(-.5,linePos+.5),letter-64).draw(win)
        letter = letter + 1
        linePos = linePos + 1
    quitButton = Circle(Point(8.5,8.5),.4)
    quitButton.setFill("light grey")
    quitButton.draw(win)
    quitText = Text(Point(8.5,8.5),"Q U I T").draw(win)
    win,whitePieces,blackPieces = setup(win)
    return win,whitePieces,blackPieces

def setup(win):
    whitePieces = {}
    x = .5
    for i in range(8):
        whitePawn = Pawn("white","pawn",Point(x,1.5),Image(Point(x,1.5),"whitePawn.png"))
        whitePawn.setup(win)
        whitePieces[str(whitePawn.getCoords())] = whitePawn
        x = x + 1
    x = 1.5
    for i in range(2):
        whiteKnight = Knight("white","knight",Point(x,.5),Image(Point(x,.5),"whiteKnight.png"))
        whiteKnight.setup(win)
        whitePieces[str(whiteKnight.getCoords())] = whiteKnight
        x = 6.5
    x = 2.5
    for i in range(2):
        whiteBishop = Bishop("white","bishop",Point(x,.5),Image(Point(x,.5),"whiteBishop.png"))
        whiteBishop.setup(win)
        whitePieces[str(whiteBishop.getCoords())] = whiteBishop
        x = 5.5
    x = .5
    for i in range(2):
        whiteRook = Rook("white","rook",Point(x,.5),Image(Point(x,.5),"whiteRook.png"))
        whiteRook.setup(win)
        whitePieces[str(whiteRook.getCoords())] = whiteRook
        x = 7.5
    whiteQueen = Queen("white","queen",Point(3.5,.5),Image(Point(3.5,.5),"whiteQueen.png"))
    whiteQueen.setup(win)
    whitePieces[str(whiteQueen.getCoords())] = whiteQueen
    whiteKing = King("white","king",Point(4.5,.5),Image(Point(4.5,.5),"whiteKing.png"))
    whiteKing.setup(win)
    whitePieces[str(whiteKing.getCoords())] = whiteKing
    blackPieces = {}
    x = .5
    for i in range(8):
        blackPawn = Pawn("black","pawn",Point(x,6.5),Image(Point(x,6.5),"blackPawn.png"))
        blackPawn.setup(win)
        blackPieces[str(blackPawn.getCoords())] = blackPawn
        x = x + 1
    x = 1.5
    for i in range(2):
        blackKnight = Knight("black","knight",Point(x,7.5),Image(Point(x,7.5),"blackKnight.png"))
        blackKnight.setup(win)
        blackPieces[str(blackKnight.getCoords())] = blackKnight
        x = 6.5
    x = 2.5
    for i in range(2):
        blackBishop = Bishop("black","bishop",Point(x,7.5),Image(Point(x,7.5),"blackBishop.png"))
        blackBishop.setup(win)
        blackPieces[str(blackBishop.getCoords())] = blackBishop
        x = 5.5
    x = .5
    for i in range(2):
        blackRook = Rook("black","rook",Point(x,7.5),Image(Point(x,7.5),"blackRook.png"))
        blackRook.setup(win)
        blackPieces[str(blackRook.getCoords())] = blackRook
        x = 7.5
    blackQueen = Queen("black","queen",Point(3.5,7.5),Image(Point(3.5,7.5),"blackQueen.png"))
    blackQueen.setup(win)
    blackPieces[str(blackQueen.getCoords())] = blackQueen
    blackKing = King("black","king",Point(4.5,7.5),Image(Point(4.5,7.5),"blackKing.png"))
    blackKing.setup(win)
    blackPieces[str(blackKing.getCoords())] = blackKing
    return win,whitePieces,blackPieces
    
def turn(win,message,team,whitePieces,blackPieces):
    message.setText(team+"'s turn to move")
    while True:
        mouseClick = win.getMouse()
        if quitCheck(win,mouseClick) == True:
            return True
        x,y = int(mouseClick.getX())+.5,int(mouseClick.getY())+.5
        if team == "white" and (str(Point(x,y)) in whitePieces.keys()):
            selectedPiece = whitePieces[str(Point(x,y))]
            message.setText(str(selectedPiece.getColor())+" "+str(selectedPiece.getName()))
            if selectedPiece.getMoves(whitePieces,blackPieces) != False:
                break
        elif team == "black" and (str(Point(x,y)) in blackPieces.keys()):
            selectedPiece = blackPieces[str(Point(x,y))]
            message.setText(str(selectedPiece.getColor())+" "+str(selectedPiece.getName()))
            if selectedPiece.getMoves(whitePieces,blackPieces) != False:
                break
        message .setText("invalid move")
    oldKey = selectedPiece.getCoords()
    dotList = []
    for i in selectedPiece.getMoves(whitePieces,blackPieces):
        dot = Circle(eval(i),.1)
        dotList = dotList + [dot]
        dot.setFill("light grey")
        dot.draw(win)
    while True:
        mouseClick = win.getMouse()
        if quitCheck(win,mouseClick) == True:
            return True
        x,y = int(mouseClick.getX())+.5,int(mouseClick.getY())+.5
        if str(Point(x,y)) in selectedPiece.getMoves(whitePieces,blackPieces):
            selectedPiece.move(x,y)
            for i in dotList:
                i.undraw()
            break
    if team == "white":
        whitePieces[str(selectedPiece.getCoords())] = whitePieces.pop(str(oldKey))
        if str(selectedPiece.getCoords()) in blackPieces:
            captured = blackPieces.pop(str(selectedPiece.getCoords()))
            captured.capture()
    elif team == "black":
        blackPieces[str(selectedPiece.getCoords())] = blackPieces.pop(str(oldKey))
        if str(selectedPiece.getCoords()) in whitePieces:
            captured = whitePieces.pop(str(selectedPiece.getCoords()))
            captured.capture()
    #if selectedPiece.getName() == "pawn":
        #if selectedPiece.getCoords() == 
        
def quitCheck(win,mouseClick):
    x = mouseClick.getX()
    y = mouseClick.getY()
    distance = sqrt(((x-8.5)**2)+((y-8.5)**2))
    if distance <= .4:
        win.close()
        return True

def main():
    win,message = intro()
    win,whitePieces,blackPieces = GUI(win)
    while True:
        if turn(win,message,"white",whitePieces,blackPieces) == True:
            break
        if turn(win,message,"black",whitePieces,blackPieces) == True:
            break
main()
