from pylab import *
import random as rd

# This code is an implementation of the game Black Jack By Henrik & Amiir



deck_size = input("How many decks do you want to play with? (1-8) ") # How many decks do you want to play with
for i in range(0,int(deck_size)):
    gamedeck.append(deck_size)

print("The total number of cards in the deck is: ", len(gamedeck))


class Deck:
    def __init__(self, type, card, amount):
        self.type = type
        self.card = card
        self.amount = amount

gamedeck = []
for i in range(4):



def dealer(deck):
