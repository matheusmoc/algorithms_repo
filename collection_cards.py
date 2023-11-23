import collections
from random import choice

card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JKQA')
    suits = 'spades diamonds clubs hearts'.split()
    

    def __init__(self):
        self._cards = [card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)
        #13 ranks * 4 suits
    
    def __getitem__(self, position):
        return self._cards[position]

#namedtuple()
beer_card = card('7', 'diamonds')
print(beer_card)    
#Card(rank='7', suit='diamonds')

#__len__
deck = FrenchDeck()
print(f'Total Deck: {len(deck)}')
#52

# __getitem__
print(deck[0])
#Card(rank='2', suit='spades')
print(deck[1])
#Card(rank='3', suit='spades')
print(deck[-1])
#Card(rank='A', suit='hearts')


