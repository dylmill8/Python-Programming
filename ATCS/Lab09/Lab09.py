#Dylan Miller

#this program implements geometric graphs, dijkstra's algorithm, and
#iterative deepening

from random import *
from math import *
from graphics import *

#rnadomly generates points, connecting them with edges to create a geometric graph
    #A is x-coord maximum
    #B is Y-coord maximum
    #N is number of points
    #D is distance between points that are selected to have an edge
def randGeoGraph(A,B,N,D):
    #list of vertices
    V = []
    #dictionary of adjacent points to each vertex
    E = {}
    for i in range(N):
        point = (randint(0,A),randint(0,B))
        V.append(point)
    for j in range(N):
        adjacent = []
        for i in range(N):
            distance = dist([V[j][0],V[j][1]],[V[i][0],V[i][1]])
            #checks if the point is within the max distance of the current vertex
            if distance <= D:
                adjacent.append(V[i])
            index = j
            E[index] = adjacent
    return V,E

#draws a given graph to scale in a new window  
    #V is list of vertices
    #E is list of edges
    #A & B are the upper bounds of the x and y axis respectively
def drawGraph(V,E,A,B):
    win = GraphWin("Geometric Graph",600,600)
    #scale the coordinates to fit the window
    win.setCoords(-1,-1,A+1,B+1)
    for i in range(A+1):
        line = Line(Point(i,0),Point(i,B))
        line.setFill("light grey")
        line.draw(win)
    for i in range(B+1):
        line = Line(Point(0,i),Point(A,i))
        line.setFill("light grey")
        line.draw(win)
    for i in V:
        index = V.index(i)
        #get adjacent points to current vertex
        listPoints = E.get(index)
        #draw current vertex
        p1 = Point(i[0],i[1])
        circle = Circle(p1,.25)
        circle.setFill("black")
        circle.draw(win)
        for j in listPoints:
            #connect current point and adjacent point with a line
            p2 = Point(j[0],j[1])
            line = Line(p1,p2)
            line.draw(win)
    win.getMouse()
    win.close()

#initializes the nodes of a graph to apply dijkstra's algorithm
    #V is list of vertices
    #E is list of edges
    #source is a given starting point
def InnitializeSingSource(V,E,source):
    W = {}
    for i in V:
        #vetex maps to [vertices traveled/days,predecessor point]
        #all vertices are set to infinity (99999)
        W[i] = [99999,None]
    #source node is set to 0
    W[source][0] = 0
    return W

#updates the shortest path from one vertex to another
    #current point
    #adjacent point
    #W is a dictionary where a vertex maps to [vertices traveled,(predecessor point}]
    #q is a sorted list of points that have not been evaluated (acts like min-priority queue)
def Relax(currentPoint,adjacentPoint,W,q):
    #prevents overlapping points and points being adjacent to themselves
    if currentPoint == adjacentPoint:
        return
    if W[adjacentPoint][0] > W[currentPoint][0] + 1:
        try:
            for j in range(len(q)):
                #checks every point in the list/queue to find the index of the adjacent point
                point = (q[j][2],q[j][3])
                if point == adjacentPoint:
                    #changes the nuber of vertices travelled in the list/queue
                    q[j][0] = W[currentPoint][0] + 1
                    q[j][1] = currentPoint
        except ValueError:
            pass
        #changes the nuber of vertices travelled in the dictionary
        W[adjacentPoint][0] = W[currentPoint][0] + 1
        W[adjacentPoint][1] = currentPoint     

#given a graoh and starting vertex the program will find the number of days
#required to travel to any other point
    #V is list of vertices
    #E is list of edges
    #W is a dictionary where a vertex maps to [vertices traveled,(predecessor point}]
    #source is the starting point
def roadtrip(V,E,W,source):
    #list of remaining points to be relaxed
    q = []
    for i in V:
        #distance from source, predecessor, x-coord, y-coord
        pointWeight = [W[i][0],W[i][1],i[0],i[1]]
        q.append(pointWeight)
    while len(q) > 0:
        #sorts queue to get minimum distance from the current vertex
        q.sort()
        closestPointValues = q.pop(0)
        closestPoint = (closestPointValues[2],closestPointValues[3])
        index = V.index(closestPoint)
        #calls relax function on the adjacent points of the current vertex
        for i in E[index]:
            #current point, adjacent point, distances travelled, remaining points
            Relax(closestPoint,i,W,q)
    print("Start Point:",source)
    for i in V:
        if i != source:
            if W[i][0] >= 99999:
                print("Point",i,"is unreachable")
            else:
                print("Point",i,"takes",W[i][0],"days to travel")

#uses depth-first search to find if a vertex is reachable from the start point
#in a given number of steps
    #V is list of vertices
    #E is list of edges
    #point current vertex
    #verticesChecked list of visited vertices
    #L maximum number of steps to find the target
def DFS(V,E,point,verticesChecked,L):
    #tracks every point that has been reached from the start
    if point not in verticesChecked:
        verticesChecked.append(point)
    index = V.index(point)
    #checks every adjacent point
    for i in E[index]:
        #DFS starts with length L and works backwards to check all possible paths
        for j in range(L):
            DFS(V,E,i,verticesChecked,L-1)

#returns True if point T is reachable from S in at most L steps
    #V is list of vertices
    #E is list of edges
    #S is the start vertex
    #T is the target vertex
    #L maximum number of steps to find the target
def checkPath(V,E,S,T,L):
    verticesChecked = []
    DFS(V,E,S,verticesChecked,L)
    if T in verticesChecked:
        return True
    else: return False

#uses binary search to find the shortest path between two points
    #V is list of vertices
    #E is list of edges
    #S is the start vertex
    #T is the target vertex
    #L maximum number of steps to find the target
    #LB is the lower bound of possible path lengths (0)
    #UB is the upper bound of possible path lengths (Number of points - 1)
def iterativeDeepening(V,E,S,T,LB,UB):
    splitIndex = (LB+UB)//2
    #returns None if the lower bound crosses the upper bound
    #meaning that the target is unreachable
    if LB > UB:
        return None
    #checks if the shortest path is at the split/halfway point
    elif checkPath(V,E,S,T,splitIndex) and not checkPath(V,E,S,T,splitIndex-1):
        return splitIndex
    #if the target is reachable with a path length equal to or less than
    #the halfway point then recurse on paths of length lower bound to halfway
    elif checkPath(V,E,S,T,splitIndex) == True:
        return iterativeDeepening(V,E,S,T,LB,splitIndex)
    #else recurse on paths of length halfway to upper bound
    else:
        return iterativeDeepening(V,E,S,T,splitIndex+1,UB)

def main():
    
    #problem 1
    A = 50
    B = 50
    N = 50
    D = 13
    V,E = randGeoGraph(A,B,N,D)
    drawGraph(V,E,A,B)

    #problem 2
    A = 8
    B = 8
    N = 6
    D = 6
    V,E = randGeoGraph(A,B,N,D)
    source = V[randint(0,N-1)]
    W = InnitializeSingSource(V,E,source)
    roadtrip(V,E,W,source)
    drawGraph(V,E,A,B)

    print("\n----------\n")

    #problem 4 A
    A = 8
    B = 8
    N = 6
    D = 5
    L = 2
    V,E = randGeoGraph(A,B,N,D)
    S = None
    T = None
    while S == T:
        S = V[randint(0,N-1)]
        T = V[randint(0,N-1)]
    print("Start Point:",S,"\nEnd Point:",T)
    print("Is the target reachable in",L,"steps?",end=" ")
    print(checkPath(V,E,S,T,L))
    drawGraph(V,E,A,B)

    print("\n----------\n")
    
    #problem 4 B
    A = 8
    B = 8
    N = 5
    D = 5
    LB = 0
    UB = 4
    V,E = randGeoGraph(A,B,N,D)
    S = None
    T = None
    while S == T:
        S = V[randint(0,N-1)]
        T = V[randint(0,N-1)]
    print("Start Point:",S,"\nEnd Point:",T)
    print("Shortest path between",S,"and",T,"is",end=" ")
    path = iterativeDeepening(V,E,S,T,LB,UB)
    if path == None:
        print("unreachable")
    else:
        print(path)
    drawGraph(V,E,A,B)
main()
