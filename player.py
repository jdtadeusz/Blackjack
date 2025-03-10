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
            self.password = getpass.getpass("Enter your password: ")
            if self.validate_passw(self.password):
                break
            else:
                print("Password must not contain spaces. Please enter the password again.")
        
        self.name = str(input('Enter your full name: ').strip().capitalize())
        
        self.login = {self.email: self.password}
        
        with open('dataBase.txt', 'a') as f:
            json.dump(self.login, f)
            
        
        print(f"An account for {self.email} has been created!")
        
        
        
    def getUserInfo(self):
        return f"Player's name: {self.name}\nPlayer's email: {self.email}\nPlayer's password: {self.password}"        


