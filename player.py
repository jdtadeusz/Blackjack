from datetime import datetime
from dateutil.relativedelta import relativedelta
import time
import sys
import msvcrt
import others
import json
import getpass
import keyboard

class Player:
    def validate_passw(self, password):
        return not any(char.isspace() for char in password)

    def ageConsent(self, date):
        todaysDate = datetime.today().date()
        
        actAge = relativedelta(todaysDate, date).years
        
        if actAge <= 18:
            returnAge = date + relativedelta(years=18) 
            print(f"You must be at least 18 years old to create an account. You can come back on {returnAge.strftime('%Y-%m-%d')}")
            return False
        
        return True
    
    def passwsec(self):
        print("Enter your password (asterisks will be displayed):")
        password = ""
        while True:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                if event.name == 'enter':
                    break
                elif event.name == 'backspace':
                    if password:
                        password = password[:-1]
                        sys.stdout.write('\b \b')
                        sys.stdout.flush()
                elif event.name in ['shift', 'ctrl', 'alt', 'left shift', 'right shift', 'left ctrl', 'right ctrl', 'left alt', 'right alt', 'caps lock']:
                    pass
                else:
                    password += event.name
                    sys.stdout.write('*')
                    sys.stdout.flush()
        self.password = password
        print("\nPassword entered.") 
        
        
    def accCreate(self):
        
        while True:
            try: 
                birth_date_str = input("Enter your date of birth (YYYY-MM-DD): ")
                self.birthDate = datetime.strptime(birth_date_str, "%Y-%m-%d").date()
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD")
                
        if self.ageConsent(self.birthDate):
            pass
        else:
            print("Account creation failed. User is underage. ")
            others.closeWebsite()
        
        self.email = str(input("Enter you email: ")).strip()
            
        while True:
            self.passwsec()
            if self.validate_passw(self.password):
                break
            else:
                print("Password must not contain spaces. Please enter the password again.")
                
        
        self.name = str(input('Enter your full name: ').strip().capitalize())
        
        self.login = {self.email: self.password}
        
        with open('dataBase.txt', 'a') as f:
            json.dump(self.login, f)
            f.write('\n')
            
        return f"An account for {self.email} has been created!"
        
        
        
    def getUserInfo(self):
        return f"Player's name: {self.name}\nPlayer's email: {self.email}\nPlayer's password: {self.password}"        

user = Player()

print(user.accCreate())
