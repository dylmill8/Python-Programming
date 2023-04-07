#Dylan Miller

#this function creates card and deck classes to be used in a card game
#and implements common uses such as shuffling, card values,and card suits

import random

#creates the class card
class Card:
    """card class takes in a card's value and suit and can return them
when called"""

    def __init__(self,value,suit):
        "creates the card object using the card's value and suit"
        self.value = value
        self.suit = suit

    def getValue(self):
        "returns the value of the card"
        return self.value

    def getSuit(self):
        "returns the suit of the card"
        return self.suit

    #returns both the value and suit of a card
    def __str__(self):
        return str(self.value) + " of " + self.suit

#creates the deck class comprised of card objects
class Deck:
    """the deck class creates a deck of 52 unique card objects from an
Ace (1) to a King (13) and can perform actions with the deck such as
shuffling, finding the remaining cards, and removing the top card"""

    def __init__(self):
        "create the deck object"
        self.createDeck()

    #when called it will recreate a full deck of 52 card objects
    def createDeck(self):
        "rebuilds the deck of 52 cards"
        self.deck = []
        value = 0
        for i in range (13):
            value = value + 1
            self.deck = self.deck + [Card(value,"Hearts")]
            self.deck = self.deck + [Card(value,"Diamonds")]
            self.deck = self.deck + [Card(value,"Clubs")]
            self.deck = self.deck + [Card(value,"Spades")]
    
    #returns the top card (string) and removes it from the deck
    def getTopCard(self):
        "returns the top card of the deck and removes it from the deck"
        self.topCard = self.deck[0]
        del self.deck[0]
        return self.topCard

    def getCardsLeft(self):
        "returns the number of cards remaining in the deck"
        return len(self.deck)

    #uses random library to shuffle the deck
    def shuffle(self):
        "returns a shuffled deck"
        self.createDeck()
        random.shuffle(self.deck)
        return self.deck

    #returns the top card and remaining cards in the list
    def __str__(self):
        return str(self.deck[0]) + ", " + str(len(self.deck))
