import time
import sys
import msvcrt
import keyboard
import json
import os
import dataBaseControl
import player
import deck


def menu(player_instance):
    clearConsole()
    dataBaseControl.fileCreate()
    
    print(("MENU:\n\n1. Log in\n2. Sign up\n3. About Us\n4. Regulations"))
    try:
        choice = int(input("\nOPTION:"))
        if choice == 1:
            d = player_instance.loginAccount()
            if d:
                submenu(player_instance)
        elif choice == 2:
            d = player_instance.accCreate()

            if d is True:
                player_instance.createWallet()
                print("Press enter to log in...")
                input()
                d = player_instance.loginAccount()
                if d is True:
                    time.sleep(2)
                    submenu(player_instance)
            else:
                closeWebsite()
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        else:
            print("Invalid choice. Try again.")
            time.sleep(2)
            menu()
    except ValueError:
        print("Invalid choice. Try again.")
        time.sleep(2)
        menu()
        
def submenu(player_instance):
    clearConsole()
    game_deck = deck.Deck()

    print("1. Play Blackjack\n2. Wallet\n3. Log out")
    choice = int(input(': '))

    if choice == 1:
        game_deck.play_blackjack()
    elif choice == 2:
        with open('myWallet.txt', 'r+') as f:
            lines = f.readlines()
            f.seek(0)
            amount = None
            for line in lines:
                email, money = line.strip().split("=")
                if email == player_instance.email:
                    amount = money
                    break
            if amount is not None:
                print(f"Your balance: {amount}")
            else:
                print("User wallet not found.")

            print("\n1. Deposit money\n2. Withdraw money\n3. Go back")
            choice = int(input(': '))
            if choice == 1:
                player_instance.addMoney()
def closeWebsite():
    print("\nCLOSE ANY BUTTON TO CLOSE WEBSITE")
    print("\nThe website will close automaticly in:\n")
    for i in range(5, 0, -1):  
        print(f"{i}...", end='\r')  
        sys.stdout.flush() 
        time.sleep(1)  
        if msvcrt.kbhit():  
            print("\nClosing immediately...")
            sys.exit()
            print(" " * 10, end='\r') 
    sys.stdout.flush()
    sys.exit()
    

def clearConsole():
    clear = lambda: os.system('cls')
    clear()

