import random

class Deck: 
    def __init__(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        
        self.cards = [(rank, suit) for rank in ranks for suit in suits]
        random.shuffle(self.cards)
        
    def draw_card(self):
        if self.cards:
            return self.cards.pop()
        else:
            return None
        
    def scoreCard(self, card):
        self.score = 0
        rank, _ = card
        
        if rank in ['J', 'Q', 'K']:
            self.score += 10
        elif rank == 'A':
            self.score += 11
        else:
            self.score += int(rank)
        print(self.score)
            