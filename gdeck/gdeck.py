"""
Module for building a deck of cards

"""
import random


class Card(object):
    suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

    # initialize the rank and suit of a card
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    # print an instance of card
    def __repr__(self):
        if self.rank == 1:
            rank = "Ace"
        elif self.rank == 11:
            rank = "Jack"
        elif self.rank == 12:
            rank = "Queen"
        elif self.rank == 13:
            rank = "King"
        else:
            rank = self.rank
        if self.suit == Card.suits[0] or self.suit == Card.suits[1] or \
                self.suit == Card.suits[2] or self.suit == Card.suits[3]:
            suit = self.suit
        else:
            raise ValueError("value must be any of the suits within a deck of cards")
        return "{} of {}".format(rank, suit)


class Deck(object):
    # list of suits and ranks
    suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    # initialize the deck
    def __init__(self):
        self.cards = []
        self.generate()
        self.index = 0

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
    def show(self, index=None):
        if index is None:
            print(self.cards)
        else:
            print(self.cards[0:index])

    # Generate 52 cards in deck
    def generate(self):
        self.cards = []
        for suit in Deck.suits:
            for rank in Deck.ranks:
                self.cards.append(Card(rank, suit))

    # Shuffle the deck
    def shuffle(self):
        random.shuffle(self.cards)

    # draw random card in the deck
    def choice(self, index=None):
        if index is None:
            return random.choice(self.cards)
        else:
            return random.choices(self.cards, k=index)

    # draw the top card of the deck
    def draw_top(self):
        return self.cards[0]
