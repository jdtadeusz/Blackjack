import time
import sys
import msvcrt
import keyboard


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
    
