from deck import Deck

deck = Deck()
print(deck)
print(deck.cards)
deck.shuffle()
print("******************************************")
print(deck.cards)
print("******************************************")
print(deck.deal_card())
print("******************************************")
print(deck.cards)
print("******************************************")
print(deck.deal_hand(3))
print("******************************************")
print(deck.cards)
print("******************************************")
for card in deck:
    print(card)
