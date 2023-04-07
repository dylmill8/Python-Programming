#Dylan Miller

#uses a decision tree to implement a game of twenty questions

class Tree:
    """a tree is a list of nodes representing a decision tree"""

    def __init__(self):
        """creates a list to store node objects"""
        self.nodes = []

    def addNode(self,node):
        """appends a node to the list"""
        self.nodes.append(node)

    def getNodes(self):
        """returns the list of nodes"""
        return self.nodes

class Node:
    """a node stores a question and the index positions of the next node
depending on if the guess was correct or not"""
    
    def __init__(self,question,yesIndex,noIndex):
        """creates variables to hold the question and yes/no node indices"""
        self.question = question
        self.yesIndex = yesIndex
        self.noIndex = noIndex

    def getQ(self):
        """returns the question"""
        return self.question

    def getYes(self):
        """returns the index of the next node if the guess is correct"""
        return self.yesIndex

    def getNo(self):
        """returns the index of the next node if the guess is wrong"""
        return self.noIndex

    def setQ(self,question):
        """sets the question"""
        self.question = question

    def setYes(self,yesIndex):
        """sets the index of the node for correct guesses"""
        self.yesIndex = yesIndex

    def setNo(self,noIndex):
        """sets the index of the node for wrong guesses"""
        self.noIndex = noIndex

#implements a game of twenty questions using a decision tree
#comprised of a node and tree class
def twentyQs():
    print("Welcome to Twenty Questions\nThink of something and I'll try to guess it asking at most 20 questions.")

    #creates a tree with a starting "root" question and two subsequent
    #questions depending on the user's respnse to the guess (yes/no)
    tree = Tree()
    node = Node("Is it bigger than a bread box?",1,2)
    tree.addNode(node)
    node = Node("Is it a(n) elephant?",None,None)
    tree.addNode(node)
    node = Node("Is it a(n) mouse?",None,None)
    tree.addNode(node)

    #loops until the player chooses to quit
    play = "yes"
    while play[0] == "Y" or play[0] == "y":
        print()

        #sets the win condition to False
        correct = False
        nodes = tree.getNodes()
        #gets the root question
        current = nodes[0]
        for i in range(20):
            response = input(current.getQ()+" ")
            
            if response[0] == "Y" or response[0] == "y":
                #if there are no other nodes and the last guess was correct
                if current.getYes() == None:
                    #sets the win condition to True
                    correct = True
                    break
                #sets current to the "yes" node for the next iteration
                current = nodes[current.getYes()]

            else:
                #if there are no other nodes and the last guess was wrong
                if current.getNo() == None:
                    break
                #sets current to the "no" node for the next iteration
                current = nodes[current.getNo()]

        #checks for win condition
        if correct == True:
            print("Yay, I guessed it!")

        else:
            print("Oh no, I couldn't get it!")
            item = input("What were you thinking? ")
            question = input("What is a distinguishing question? ")
            answer = input("Is yes or no the correct answer to your question? ")
            print("Got it -- thanks!")

            #adds two new nodes to the tree, one with the player's new
            #item and the other with the current question/item
            node = Node(current.getQ(),None,None)
            tree.addNode(node)
            node = Node("Is it a(n) "+item+"?",None,None)
            tree.addNode(node)

            #sets the current node to the user's new distinguishing question
            current.setQ(question)

            #if the answer to the player's distinguishing question is "yes"
            if answer[0] == "Y" or answer[0] == "y":
                #set the yes/no indices of the current node to the new positions
                current.setYes(len(nodes)-1)
                current.setNo(len(nodes)-2)
            else:
                current.setYes(len(nodes)-2)
                current.setNo(len(nodes)-1)

        play = input("\nDo you want to play again? ")
        
    print("Thanks for playing!")
              
def main():
    twentyQs()
main()
