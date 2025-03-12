import time
import sys
import msvcrt
import keyboard
import json
import os
import dataBaseControl
import player


def menu():
    clearConsole()
    dataBaseControl.fileCreate()
    
    print(("MENU:\n\n1. Log in\n2. Sign up\n3. About Us\n4. Regulations"))
    try:
        player_c = player.Player()
        choice = int(input("\nOPTION:"))
        if choice == 1:
            d = player_c.loginAccount()
            
            if d is True:
                pass
            else:
                closeWebsite()
        elif choice == 2:
            d = player_c.accCreate()

            if d is True:
                print("Press enter to log in...")
                input()
                player_c.loginAccount()
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

