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
            f.write(f"{self.email}={self.password}\n")
        
        print(f"\nAn account for {self.email} has been created!")
        
        return True
        
    def loginAccount(self):
        others.clearConsole()
        
        self.email = input("E-mail: ")
        self.password = getpass.getpass("Password: ")
        
        try:
            with open("dataBase.txt", 'r') as f:
                for user in f:
                    email, password = user.strip().split("=")
                    if email == self.email and password == self.password:
                        print("Logn successful!")
                        return True
                print("Invalid email or password. Try again.")
                return False 
        except FileNotFoundError:
            print("Data base not found.")
            return False
        except ValueError:
            print("Database file is corrupted. Please check the content.")
            return False
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False 
        
    def getUserInfo(self):
        return f"Player's name: {self.name}\nPlayer's email: {self.email}\nPlayer's password: {self.password}"        

    def createWallet(self):
        self.money = 0
        try:
            with open("myWallet.txt", 'r') as f:
                for line in f:
                    email, _ = line.strip().split("=")
                    if email == self.email:
                        return 
        except FileNotFoundError:
            pass 
        with open("myWallet.txt", 'a') as f:
            f.write(f"{self.email}={self.money}\n")
            
    def addMoney(self, amount): #poprawic
        self.amount = amount
        with open("myWallet.txt", 'r+') as f:
            try:
                for wallet in f:
                    if wallet.strip("=")[0] == self.email:
                        #wallet.write(f"{self.email}={self.money+=self.amount}")
                        pass
                    else:
                        pass
            except ValueError:
                print("No such user.")
                
