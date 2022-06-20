from operator import index
import random
from typing import Tuple
from enum import Enum

class Suit(str, Enum):
    Club    = "♣"
    Diamond = "♦"
    Heart   = "♥"
    Spade   = "♠"

class Card:
    def __init__(self, rank: str, suit: str) -> None:
        self.suit = suit
        self.rank = rank
        self.hard, self.soft = self._points()        
    
    def __str__(self) -> str:
        return f"{self.rank}{self.suit}"

    def _points(self) -> tuple[int,int]:
        return int(self.rank),int(self.rank)
    
class AceCard(Card):
    def _points(self) -> tuple[int,int]:
        return 1,11

class FaceCard(Card):
    def _points(self) -> tuple[int,int]:
        return 10,10

"""THIS DECK CLASS VERSION IS A WRAPPER DESIGN THAT CONTAINS AN INTERNAL COLLECTION """
class Deck:
    def __init__(self) -> None:
        self._cards = [Card(r + 1, s) for r in range(13) for s in iter(Suit)]
        random.shuffle(self._cards)

    def pop(self) -> Card:
        return self._cards.pop()

"""THIS DECK CLASS VERSION MAKES USE OF A LIST WHICH GIVES ACCESS TO ADDITIONAL METHODS, SUCH AS DELETE(), REMOVE() """
class Deck2(list):
    def __init__(self) -> None:
        super().__init__(cardFactory(r + 1, s) for r in range(13) for s in iter(Suit))
        random.shuffle(self)

"""THIS DECK CLASS VERSION ALLOWS FOR MULTIPLE 52-CARD DECKS""" 
class Deck3(list):
    def __init__(self, decks: int = 1) -> None:
        super().__init__()
        for i in range(decks):
            self.extend(cardFactory(r + 1, s) for r in range(13) for s in iter(Suit))
        random.shuffle(self)

'''THIS FACTORY FUNCTION IS USED TO AUTOMATE THE CREATION OF A 52-CARD DECK'''
def cardFactory(rank: int, suit: Suit) -> Card:
    if rank == 1:
        return AceCard("A", suit)
    elif 2 <= rank < 11:
        return Card(str(rank), suit)
    elif 11<= rank < 14:
        name = {11: "J", 12: "Q", 13: "K"}[rank]
        return FaceCard(name, suit)
    raise Exception("Design Failure")

'''INITIALIZER SPECIAL METHOD, WHICH CAN LOAD ALL THE ITEMS IN ONE STEP'''
class Hand:
    def __init__(self, dealer_card: Card, *cards: Card) -> None:
        self.dealer_card = dealer_card
        self.cards = list(cards)
    
    def card_append(self, card: Card) -> None:
        self.cards.append(card)
    
    def hard_total(self) -> None:
        return sum(c.hard for c in self.cards)
    
    def soft_total(self) -> None:
        return sum(c.soft for c in self.cards)

    def __repr__(self) -> None:
        return f"{self.__class__.__name__}({self.dealer_card!r},*{self.cards})"

    def show_hand(self):
        return True

class GameStrategy:
    def insturance(self, hand: Hand) -> bool:
        return False

    def split(self, hand: Hand) -> bool:
        return False

    def double(self, hand: Hand) -> bool:
        return False

    def hit(self, hand: Hand) -> bool:
        return sum(c.hard for c in hand.cards) <= 17       

class Table:
    def __init__(self) -> None:
        self.deck = Deck()

    def place_bet(self, amount: int) -> None:
        print("Bet", amount)
    
    def get_hand(self) -> Hand:
        try:
            self.hand = Hand(self.deck.pop(), self.deck.pop(), self.deck.pop())
            self.hole_card = self.deck.pop()
        except IndexError:
            # Out of cards: need to shuffle and try again.
            self.deck = Deck()
            return self.get_hand()
        print("Deal", self.hand)
        return self.hand

    def can_insure(self) -> bool:
        return hand.dealer_card.insure

'''**********************************MAIN PROGRAM***********************************'''
'''myDeck = Deck3()
hand = [myDeck.pop(), myDeck.pop()]
for i in range(len(hand)):
    print(str(hand[i]))'''

deck = Deck()
hand = Hand(deck.pop(),deck.pop())

dumb = GameStrategy()
