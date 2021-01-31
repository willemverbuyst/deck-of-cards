from card import Card
from random import shuffle


class Deck:

    def __init__(self):
        values = ["A", "2", "3", "4", "5", "6",
                  "7", "8", "9", "10", "J", "Q", "K"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.cards = [Card(value, suit) for value in values for suit in suits]

    def __repr__(self):
        return f"Deck of {self.count()} cards."

    def count(self):
        return len(self.cards)

    def shuffle(self):
        if self.count() != 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self

    def _deal(self, number_of_cards):
        if self.count() == 0:
            raise ValueError("All cards have been dealt")
        else:
            amount = min(self.count(), number_of_cards)
            cards = self.cards[-(amount):]
            self.cards = self.cards[:-(amount)]
            return cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, number_of_cards):
        return self._deal(number_of_cards)
