import random
import player
import dataBaseControl 

class Deck: 
    def __init__(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        
        self.cards = [(rank, suit) for rank in ranks for suit in suits]
        random.shuffle(self.cards)
        
    def draw_card(self):
        self.score = 0
        if self.cards:
            return self.cards.pop()
        else:
            return None
        
    def scoreCard(self, card):
        rank, _ = card
        
        if rank in ['J', 'Q', 'K']:
            return 10
        elif rank == 'A':
            return 11
        else:
            return int(rank)
        

dataBaseControl.fileCreate()
player.Player.accCreate()
desk = Deck()

card = desk.draw_card()
print(card, desk.scoreCard(card))