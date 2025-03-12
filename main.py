import random
import player
import dataBaseControl 
import desk
import others
import os
import time


    
    
#others.menu()

user = player.Player

deck = desk.Deck()

card = deck.draw_card()

if card:
    deck.scoreCard(card)
else:
    print("Deck is empty.")


