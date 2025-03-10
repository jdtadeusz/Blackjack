import time
import sys
import msvcrt
import keyboard
import json


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
    
def dataBasePrint():
    try:
        with open('dataBase.txt', 'r') as f:
            data = json.load(f)  # Odczytanie danych JSON jako listy słowników
            for user in data:  # Iteracja po liście słowników
                print(user)
    except FileNotFoundError:
        print("Plik dataBase.txt nie istnieje.")
    except json.JSONDecodeError:
        print("Plik dataBase.txt zawiera niepoprawne dane JSON.")
    except Exception as e:
        print(f"Wystąpił błąd podczas odczytu pliku: {e}")
            
dataBasePrint()
