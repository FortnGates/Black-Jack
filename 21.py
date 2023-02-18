import os
import random
from tkinter import *
from itertools import  product

rank = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
suit = ["♥","♠","♣","♦"]



class Card():

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def card_value(self):
        if self.rank in "TJQK":
            return 10
        else:
            return " A23456789".index(self.rank)

    def get_rank(self):
        return self.rank

    def __str__(self):
        return "%s%s" % (self.rank, self.suit)



class Deck(Card):

    def __init__(self):
        self.deck = []
        self.deck = [Card(name, suit) for name, suit in product(rank, suit)]
        random.shuffle(self.deck)

    def __str__(self):
        for card in self.deck:
            print(card)
        return (self.deck)

    def random_card(self):
        card = random.choice(self.deck)
        self.deck.remove(card)
        # print(card)
        return (card)

class Player(Deck):

    def __init__(self, name=''):
        self.name = name
        self.player_hand = []
        self.score = 0

    def __str__(self):
        print(self.name)
        return Deck.__str__(self)

    def print(self):
        for card in self.player_hand:
            print(card)
        return (self.player_hand)

    def add(self, card):
        self.player_hand.append(card)
        return self.player_hand

class Game:
    def __init__(self):
        gam = Deck()
        #gam.__str__()
        print("-------------------------")
        d1 = Player("Dealer")
        p1 = Player("Gamer")
        d1.add(gam.random_card())
        d1.add(gam.random_card())
        d1.print()
        p1.add(gam.random_card())
        p1.add(gam.random_card())
        p1.print()

        root = Tk()
        root.title("21 очко",)
        root.config(width=500, height=350, background="green")
        dealerWin = Label(root, text="Кількість перемог гравця ШІ: ")
        playerWin = Label(root, text="Кількість ваших перемог: ")
        scorePlayer = Label(root, text="У вас на руках: ")

        hit = Button(root, text="Ще карту")
        hit.grid(row=0, column=0, pady=50, padx=50)
        hit.bind("<Button-1>", )
        stop = Button(root, text="Хватить з мене")
        stop.grid(row=0, column=1, pady=50, padx=50)
        stop.bind("<Button-1>", )
        #rozdacha(decka)

        #root.resizable(0, 0)
        root.mainloop()
game = Game()


# root = Tk()
# root.title("21 очко",)
# root.config(width=500, height=350, background="green")
# dealerWin = Label(root, text="Кількість перемог гравця ШІ: ")
# playerWin = Label(root, text="Кількість ваших перемог: ")
# scorePlayer = Label(root, text="У вас на руках: ")
#
# hit = Button(root, text="Ще карту")
# hit.grid(row=0, column=0, pady=50, padx=50)
# hit.bind("<Button-1>", )
# stop = Button(root, text="Хватить з мене")
# stop.grid(row=0, column=1, pady=50, padx=50)
# stop.bind("<Button-1>", )
# #rozdacha(decka)
#
# #root.resizable(0, 0)
# root.mainloop()

