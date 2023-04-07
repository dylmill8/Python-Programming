#Dylan Miller

#this program implements a random walk using the GraphAdjMatrix class

#imports the GraphAdjMatrix class and the random library
from GraphAdjMatrix import *
from random import *

#implements a random walk using the GraphAdjMatrix class
#and a given file of vertices and edges
def randomWalk(adjMatrix,file):
    #removes \n from the end of each line
    file = [line[:-1] for line in file]
    vertices = []
    for i in file:
        #separates the vertices into u and v
        u,v = i.split(",")
        #adds the vertices to a tracker list
        vertices = vertices + [u] + [v]
        #adds the vertices and creates an edge in the adjMatrix
        adjMatrix.addEdge(u,v)
    play = "y"
    while play[0] == "y":
        n = ""
        #forces the user to imput an integer
        while True:
            try:
                n = int(input("Number of walks: "))
                break
            except: n = ""
        start = ""
        #forces the user to pick a valid vertex from the tracker list
        while start not in vertices:
            start = input("Starting vertex: ")
        print("Start",start,"->",end=" ")
        path = []
        #repeats for the desired number of walks
        for i in range(n):
            #finds the neighbors of the current vertex
            neighbors = adjMatrix.getNeighbors(start)
            #generates a random vertex from the list of neighbors
            number = randint(0,len(neighbors)-1)
            #appends the chosen vertex to the path tracker
            path.append(neighbors[number])
            #resets the start to the new vertex for the next iteration
            start = neighbors[number]
        path = " -> ".join(path)
        print(path,"End\n")
        play = input("Would you like to continue (y/n)? ")

def main():
    randomWalk(GraphAdjMatrix(),open("Lab07sample.py","r"))
main()
