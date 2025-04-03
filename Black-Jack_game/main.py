from pylab import *
import random as rd

# This code is an implementation of the game Black Jack By Henrik & Amiir



# deck_size = input("How many decks do you want to play with? (1-8) ") # How many decks do you want to play with
# for i in range(0,int(deck_size)):
#     gamedeck.append(deck_size)
#
# print("The total number of cards in the deck is: ", len(gamedeck))


class Deck:
    def __init__(self, type, card, value):
        self.type = type
        self.card = card
        self.value = value


gamedeck = []

for i in range(0, 4):
    for j in range(1, 10):
        if i == 0:
            gamedeck.append(Deck("Hearts", j , j))
        if i == 1:
            gamedeck.append(Deck("Spades", j, j))
        if i == 0:
            gamedeck.append(Deck("Diamonds", j, j))
        if i == 1:
            gamedeck.append(Deck("Clubs", j, j))


def kortvelger():


def dealer(deck):
    print()

# Commit test