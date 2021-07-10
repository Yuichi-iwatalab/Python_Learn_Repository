from random import shuffle
import chapter15_1 as ch15

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range(4):
                self.cards.append(ch15.Card(i,j))
        shuffle(self.cards)
    
    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

# deck = Deck()
# print(deck.cards)
# print(deck.rm_card())