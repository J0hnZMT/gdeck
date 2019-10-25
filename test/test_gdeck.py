import pytest
from gdeck import *
import random

test_cards = ["Ace of Hearts", "2 of Hearts", "3 of Hearts", "Jack of Hearts", "Queen of Hearts", "King of Hearts"]
test_suit = 'Hearts'
sample_deck = Deck()


def test_card():
    # test the arguments taken of the Card()
    assert str(Card(1, test_suit)) == test_cards[0]
    assert str(Card(2, test_suit)) == test_cards[1]
    assert str(Card('3', test_suit)) == test_cards[2]
    assert str(Card(11, test_suit)) == test_cards[3]
    assert str(Card(12, test_suit)) == test_cards[4]
    assert str(Card(13, test_suit)) == test_cards[5]


def test_deck():
    # test if the Deck can create a deck of cards
    assert sample_deck.show(5) is print(sample_deck[0:5])
    assert sample_deck.show() is print(sample_deck[0:52])


def test_deck_size():
    # test the size of the deck
    assert len(sample_deck) is 52


def test_draw_cards():
    # to test the draw_top() function
    top_card = sample_deck[0]
    assert sample_deck.draw_top() is top_card
    assert next(sample_deck) is top_card


def test_choice():
    # test the choice function
    assert len(sample_deck.choice(5)) == 5


if __name__ == '__main__':
    pytest.main()





