"""
Module for building a deck of cards

"""
import random


class Card(object):
    # initialize the rank and suit of a card
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    # Implementing build in methods so that you can print a card object
    def __str__(self):
        return self.show()

    def __repr__(self):
        return self.show()

    # print an instance of card
    def show(self):
        return "{} of {}".format(self.suit, self.rank)


class Deck(object):
    # list of suits and ranks
    suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    # initialize the deck
    def __init__(self):
        self.cards = []
        self.build()
        self.index = 0

    # make the class iterator
    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.cards):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.cards[index]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, index):
        return self.cards[index]

    # Display all cards in the deck
    def show(self):
        for get_card in self.cards:
            print(get_card.show())

    def __str__(self):
        return self.show()

    def __repr__(self):
        return self.show()

    # Generate 52 cards in deck
    def build(self):
        self.cards = []
        for suit in Deck.suits:
            for rank in Deck.ranks:
                self.cards.append(Card(suit, rank))

    # Shuffle the deck
    def shuffle(self, num=1):
        for _ in range(num):
            # build in shuffle method
            random.shuffle(self.cards)

    # draw random card in the deck
    def draw(self):
        return random.choice(self.cards)

    # draw the top card of the deck
    def draw_top(self):
        return self.cards[0]

