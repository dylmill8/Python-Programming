#Dylan, Randy, Brian

#This program runs a text based Jeopardy trivia game complete with
#a points system and item rewards.

import random
import time

#superclass that creates an item with basic functions
#such as manipulating points and tracking the player's inventory
class Items:
    """the Item class creates an item that can change point values
and keep track of the number of items in a player's inventory"""
    def __init__(self,player,numbItems):
        "Creates the item object"
        self.Player = player
        self.numbItems = numbItems

    #tracks the number of items a player has
    def itemCount(self):
        "returns number of items the player has recieved"
        return self.numbItems

    #adds an item to the player's inventory
    def addItem(self):
        "adds an item to the player's inventory"
        self.numbItems = self.numbItems + 1

    #removes an item from the player's inventory
    def removeItem(self):
        "removes an item from the player's inventory"
        self.numbItems = self.numbItems - 1

    #adds points to the player's point total
    def addPoints(self,points):
        "adds points to the player's total"
        newTotal = player.getTotal() + points
        player.newTotal(newTotal)

#creates a Daily Double item
class DailyDouble(Items):
    """the daily double class creates an object that manipulates the players
point values"""
    #doubles the points earned if the player answers correctly
    def addPoints(self,points,player):
        "doubles the points a user wagers on a question"
        newTotal = player.getTotal() + (points * 2)
        player.newTotal(newTotal)

#creates a Bonus item
class Bonus(Items):
    """the bonus class creates an object that manipulates the players
point values"""
    #increases the points earned by 100 if the player answers correctly
    def addPoints(self,points,player):
        "increases the points a user wagers on a question by 100"
        newTotal = player.getTotal() + (points + 100)
        player.newTotal(newTotal)

#creates a No Loss item
class NoLoss(Items):
    """the no loss class creates an object that manipulates the players
point values"""
    #removes the penalty for a wrong question by adding 1/2 the points of
    #the player's wager
    def removePoint(self,points,player):
        "adds 1/2 the points that a player wagers"
        newTotal = player.getTotal() + (points/2)
        player.newTotal(newTotal)

#creates an object to add or remove points from the player
class Points:
    def __init__(self,points,player):
        "creates point object"
        self.points = points
        self.player = player

    #adds the amount of points the player wagers to their total
    def addPoints(self):
        "adds points to the player"
        newtotal = self.player.getTotal() + self.points
        self.player.newTotal(newtotal)

    #subtracts the amount of points the player wagers from their total
    def removePoints(self):
        "removes points from the player"
        newtotal = self.player.getTotal() - self.points
        self.player.newTotal(newtotal)

#the player class tracks and manipulates a player's total points
#and their current round
class Player:
    def __init__(self,total,room):
        "creates player object"
        self.total = total
        self.room = room

    #tracks player's point total
    def getTotal(self):
        "returns total points"
        return self.total

    #tracks the round number
    def getRoom(self):
        "returns player's current round number"
        return self.room

    #moves the player to the next round
    def nextRoom(self):
        "increase the player's round by one"
        self.room = self.room + 1
        return self.room

    #changes the player's total points to an input amount
    def newTotal(self, newtotal):
        "changes the player's total points"
        self.total = newtotal
        return self.total

#the question class creates a dictionary of questions that the player will be
#asked throughout the game and can check the player's answers
class Question:
    #when called question class will create a dictionary of questions
    def __init__(self):
        "creates questions"
        self.listQuestions = self.createQuestions()

    #adds all questions to the dictionary
    def createQuestions(self):
        "creates a dictionary of trivia questions"
        self.questions = {'How many sides does a nonagon have':'9',
                          'What is an angle called if it is greater than 90 degrees':'obtuse',
                          'What is 177 + 46':'223',
                          'What number is twice the sum of its digits':'18',
                          'What planet is closest to the sun':'mercury',
                          'How many manned moon landings have there been':'6',
                          'Where is the smallest bone in the body found':'ear',
                          'What is the shortest complete sentence in English':'go',
                          'What is 87 + 56':'143',
                          'What are the characters that move called in block based programming':'sprites',
                          'What is the largest organ in the body':'skin',
                          'What was prehistoric Earth\'s supercontinent called':'pangea',
                          'How many stars does the American flag have':'50',
                          'What is 2 to the power of 10':'1024',
                          'What is Spanish for hello':'hola',
                          'What country produces the most coffee':'brazil',
                          'What is the capital of Spain':'madrid',
                          'What is the pH level of water to the nearest integer':'7',
                          'What color player starts in chess':'white',
                          'What color is a giraffe\'s tongue':'black',
                          'What part of the atom has no electrical charge':'nuetron',
                          'What is the name of the world’s longest river':'nile',
                          'How many continents are there in the world':'7',
                          'Which country gifted the statue of liberty to the US':'france',
                          'How many points is a touchdown worth':'6',
                          'Which Ocean is the Bermuda Triangle located in':'atlantic',
                          '"Fe" is a chemical symbol for what element':'iron',
                          'Which US state is the largest':'alaska',
                          'How many hearts does an octopus have':'3',
                          'What was the first US state':'Delaware'}
        return self.questions

    #creates a list containing all the questions
    def getKeys(self):
        "return a list of the questions"
        return list(self.listQuestions.keys())

    #creates a list containing the answers to all the questions
    def getValues(self):
        "returns a list of the answers"
        return list(self.listQuestions.values())

    #removes a question from the dictionary after it has been used
    def remove(self,question):
        "removes a question from the dictionary"
        self.questions.pop(question)
        return self.questions

    #checks if the player's input corresponds to the question's answer
    def checkAnswer(self,response,numb):
        "checks if the player's input is the same as the answer to the question"
        values = self.getValues()
        if response == values[numb]:
            return True
        else: return False

    #gets the number of remaining questions that haven't been used
    def getLength(self):
        "returns the length of the question list"
        return len(self.listQuestions)

#this function prints the introduction and instructions
    #parameters: none
def intro():
    print("""Welcome to Jeopardy!
--------------------
The objective of this game is to complete 5 rounds of trivia.
Be sure to accumulate 7000 points before the boss round.
The questions will be difficult but don't worry!
Throughout the game you will be able to receieve random items!
Although don't rely on these items too heavily.
There is a chance you could answer incorrectly and lose your item.
You will be facing the final round once you complete all the questions.
Goodluck!""")

#this function will add an item to the player's inventory based
#on a random number generated after each question
    #parameters: itemNumb - randomly generated number
                #dailyDouble - daily double object
                #bonus - bonus object
                #noLoss - no loss object
def recieveItem(itemNumb,dailyDouble,bonus,noLoss):
    #checks if the player should recieve an item
    if itemNumb == 1:
        print("""You recived the Daily Double item!
When you choose to use the item it will double thw points of your next question.
However, if you answer incorrectly, you will lose the item and the regular amount of points.\n""")
        #adds one item of the corresponding class
        #to the player's inventory
        dailyDouble.addItem()
    elif itemNumb == 2:
        print("""You recieved a Bonus item!
When you use this item, you will be awarded 100 points if you answer the next question correctly.\n""")
        bonus.addItem()
    elif itemNumb == 3:
        print("""You recived a No Loss item!
After using this item if you answer the next question incorrectly you will still recieve half points.\n""")
        noLoss.addItem()

#allows the player to use one of their items before answering the next question
    #parameters: totalItems - total number of items in the inventory
                #dailyDouble - daily double object
                #bonus - bonus object
                #noLoss - no loss object
def chooseItem(totalItems,dailyDouble,bonus,noLoss):
    chosenItem = 0
    useItem = 0
    #checks if the player has an item in their inventory
    if totalItems > 0:
        #repeats until the user chooses a valid item or cancels
        while useItem == 0:
            try:
                #asks the user if they want to use an item and checks for yes
                useItem = str(input("\nWould you like to use one of your items (Y/N)? "))
                if useItem[0] == "y" or useItem[0] == "Y":
                    #repeats until the user chooses a valid whole number 1-4
                    while chosenItem != '1' and chosenItem != '2' and chosenItem != '3' and chosenItem != '4':
                        chosenItem = input("\nWhich Item would you like to use?\n1 - Daily Double\n2 - Bonus Point\n3 - No Loss\n4 - Cancel\n\n> ")
                        #cheks if the player has the item they are trying
                        #to select and if not then the process repeats
                        if chosenItem == '1' and dailyDouble.itemCount() <= 0:
                            print("\nYou do not have a Daily Double item.")
                            #resets their chosen item if it is invalid
                            chosenItem = 0
                        elif chosenItem == '2' and bonus.itemCount() <= 0:
                            print("\nYou do not have a Bonus item.")
                            chosenItem = 0
                        elif chosenItem == '3' and noLoss.itemCount() <= 0:
                            print("\nYou do not have a No Loss item.")
                            chosenItem = 0
            except:
                useItem = 0
    return chosenItem,totalItems

#this function runs one round containing 3 trivia questions
    #parameters: player - player object
                #questionList - list of questions
                #totalItems - total number of items in the inventory
                #dailyDouble - daily double object
                #bonus - bonus object
                #noLoss - no loss object
def playRound(player,questionList,totalItems,dailyDouble,bonus,noLoss):
    #prints the player's current round number
    print("\nRound",player.getRoom(),"\n-------")
    #repeats for 3 trivia questions
    for i in range (3):
        wager = 0
        #loops until a player enters a multiple of 100 from 100-500
        while wager != '100' and wager != '200' and wager != '300' and wager != '400' and wager != '500':
            wager = input("How many points would you like to wager (100, 200, 300, 400, 500)? ")
        #converts the user's wager to a number value after to prevent type errors
        wager = int(wager)
        #checks if the player has an item and wants to use it
        chosenItem,totalItems = chooseItem(totalItems,dailyDouble,bonus,noLoss)
        chosenItem = int(chosenItem)
        #generates a random number from 0 to the length of the question list
        numb = random.randint(0,questionList.getLength()-1)
        keys = questionList.getKeys()
        #takes a random question from the list
        question = keys[numb]
        #gets the player's response to the question
        response = input("\n"+question+"? ")
        response = response.lower()
        #checks if the player's response matches the question answer
        if questionList.checkAnswer(response,numb) == True:
            print("Correct!\n")
            #if the player chose to use a daily double or bonus item
            #and they answer the question corretly, then their
            #wager points will be modified
            if chosenItem == 1:
                dailyDouble.addPoints(wager,player)
            elif chosenItem == 2:
                bonus.addPoints(wager,player)
            #if no items were chosen, add the regular wager to the total
            else:
                points = Points(wager,player)
                points.addPoints()
        else:
            print("Incorrect!\n")
            #if the player was incorrect and they chose to use the no loss
            #item then the amount of points they lose will be modified to
            #reduce the penalty
            if chosenItem == 3:
                noLoss.removePoint(wager,player)
            #if no items were chosen, remove the regular wager from the total
            else:
                points = Points(wager,player)
                points.removePoints()
        #removes the respective item from the player's inventory after it
        #has been used
        if chosenItem == 1:
            dailyDouble.removeItem()
        elif chosenItem == 2:
            bonus.removeItem()
        elif chosenItem == 3:
            noLoss.removeItem()
        #chooses a random number 1-9 giving the player a 33% chance to
        #recieve an item
        itemNumb = random.randint(1,9)
        #checks if a player should recieve an item and adds it to the inventory
        recieveItem(itemNumb,dailyDouble,bonus,noLoss)
        #reevaluates the player's total items by summing all the items
        #in the inventory
        totalItems = dailyDouble.itemCount() + bonus.itemCount() + noLoss.itemCount()
        #removes the used question from the list
        questionList.remove(question)
        print("You have a total of",int(player.getTotal()),"points!\n")
    return questionList,player.getTotal(),totalItems,dailyDouble,bonus,noLoss

#this function runs the final round of the game after the player has
#aquired 6000 points and has completed all 5 rounds
    #parameters: points - total number of points the player has
                #questionList - the list of remaining unused questions
                #wins - tracks how many times the player has beaten the game
def bossBattle(points,questionList,wins):
    numbCorrect = 0
    val = 0
    if points >= 6000:
        print("""Congratulations, you have qualified for the final round!
You will be asked 5 questions and have 20 seconds to answer each.
Answer 4 out of the 5 questions correctly and you will win the game.
Good luck!""")
        input("\nPress enter to begin the final round! ")
        for i in range(5):
            numb = random.randint(0,questionList.getLength()-1)
            keys = questionList.getKeys()
            question = keys[numb]
            #starts a timer that will run until the player answers the question
            start = time.time()
            response = input("\n"+question+"? ")
            #stops timer
            stop = time.time()
            #finds how long the timer was running
            duration = stop - start
            if duration >= 20:
                print("You took to long!")
            else:
                if questionList.checkAnswer(response,numb) == True:
                    print("Correct!")
                    #tracks how many out of the 5 questions the player
                    #answers correctly
                    numbCorrect += 1
                else:
                    print("Incorrect!")
            questionList.remove(question)
    else: print("""You did not reach the required points to enter the boss battle,
better luck next time!""")
    if numbCorrect >= 4:
        print("\nYou won!")
        wins = wins + 1
    else: print("""\nUnfortunately you did not answer 4 of the questions correctly.
Better luck next time!""")
    return wins

#this function runs the full jeopardy trivia game, allowing the player
#to play multiple games if they choose to continue
def main():
    #runs intro text
    intro()
    playAgain = "Y"
    wins = 0
    #checks after each completed game if the player wants to play again
    while playAgain[0] == "y" or playAgain[0] == "Y":
        #resets the player with 0 points in round 1
        player = Player(0,1)
        #rests the items in the player's inventory at the start of a new game
        dailyDouble = DailyDouble(player,0)
        bonus = Bonus(player,0)
        noLoss = NoLoss(player,0)
        totalItems = 0
        #recreates the list of questions
        questionList = Question()
        for i in range (5):
            #plays a round
            questionList,points,totalItems,dailyDouble,bonus,noLoss = playRound(player,questionList,totalItems,dailyDouble,bonus,noLoss)
            #advances the round number
            player.nextRoom()
        #runs the boss battle after round 5
        wins = bossBattle(points,questionList,wins)
        playAgain = str(input("\nWould you like to play again (Y/N)? "))
    print("\nYou won",wins,"times!")
    print("Thanks for playing!")
main()
