import random
import others

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
        rank, _ = card
        
        if rank in ['J', 'Q', 'K']:
            return 10
        elif rank == 'A':
            while True:
                one_or_el = int(input("As - 1/ 11 points?"))
                if one_or_el == 1:
                    return 1
                elif one_or_el == 11:
                    return 11
                else: 
                    print("Invalid choice. Try again.")
                    return False
        else:
            return int(rank)
            
    def calculate_score(self, hand):
        score = 0 
        
        for card in hand:
            score += self.scoreCard(card)
            
        return score

    def play_blackjack(self):
        player_deck = [self.draw_card(), self.draw_card()]
        dealer_deck = [self.draw_card(), self.draw_card()]
        
        
        while self.calculate_score(player_deck) < 21:
            try:
                print(f"Your hand: {player_deck}\nScore {self.calculate_score(player_deck)}")
                print(f"Dealer's first card {dealer_deck[0]}")
                print("Do you want to hit or stand?\n1.Hit\n2.Stand")
                choice = int(input("Choice:"))
                
                if choice == 1:
                    player_deck.append(self.draw_card())
                    print(f"Your hand: {player_deck}\nScore: {self.calculate_score(player_deck)}")
                elif choice == 2:
                    break
                else:
                    print("Invalid choice. Try again.")
                    others.clearConsole()
            except ValueError:
                print("Invalid input. Try again.")
                others.clearConsole()
        player_score = self.calculate_score(player_deck)
        dealer_score = self.calculate_score(dealer_deck)
        
        if player_score > 21:
            print("You bust! Dealer wins.")
        elif dealer_score > 21:
            print("Dealer bust! You win.")
        elif player_score > dealer_score:
            print("You win!")
        elif player_score < dealer_score:
            print("Dealer wins!")
        
        else:
            print("It's a tie!")
        
        
