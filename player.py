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
        others.clearConsole()


        while True:
            print("REGISTRATION\n")
            try: 
                birth_date_str = input("Enter your date of birth (YYYY-MM-DD): ")
                self.birthDate = datetime.strptime(birth_date_str, "%Y-%m-%d").date()
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD\n\nPress enter to try again...")
                input()
                others.clearConsole()
                
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
        
        while True:
            others.clearConsole()
            
            print("LOGIN\n")
            self.email = input("E-mail: ")
            self.password = getpass.getpass("Password: ")
            
            try:
                with open("dataBase.txt", 'r') as f:
                    for user in f:
                        email, password = user.strip().split("=")
                        if email == self.email and password == self.password:
                            print("\nLogged in successful!\nPress enter to continue...")
                            input()
                            return True
                        else:
                            print("\n!! Invalid email or password !!")
                            return False

            except FileNotFoundError:
                print("Data base not found.")
            except ValueError:
                print("Database file is corrupted. Please check the content.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
            
            
    def getUserInfo(self):
        return f"Player's name: {self.name}\nPlayer's email: {self.email}\nPlayer's password: {self.password}"        

    def createWallet(self):
        self.money = 0
        try:
            with open("myWallet.txt", 'r') as f:
                for line in f:
                    parts = line.strip().split("=")
                    email, _ = parts

                    if email == self.email:
                        return 
        except FileNotFoundError:
            pass 
        with open("myWallet.txt", 'a') as f:
            f.write(f"{self.email}={self.money}\n")
            
    def addMoney(self): 
        others.clearConsole()
        try:
            with open("myWallet.txt", 'r+') as f:
                lines = f.readlines()
                f.seek(0)
                amount = float(input("How much money would You like to deposit?\n: "))
                found = False
                for line in lines:
                    parts = line.strip().split("=")
                    if len(parts) == 2:
                        email, money = parts
                        if email == self.email:
                            found = True
                            money = float(money) + amount
                            f.write(f"{self.email}={money}\n")
                        else:
                            f.write(line)
                if not found:
                    print("No such user.")
                    return False
                return True
        except FileNotFoundError:
            print("Wallet file not found.")
            return False
        except ValueError:
            print("Wallet file corrupted.")
            return False

    def logOut(self):
        self.email = None
        self.name = None 
        self.password = None 
        self.birthDate = None
        self.money = 0

        print("Logged out successfully.\n\nPress enter to continue...")
        input()

    def withdrawMoney(self):
        try:
            with open('myWallet.txt', 'r+') as f:
                lines = f.readlines()
                f.seek(0)
                found = False
                for line in lines:
                    parts = line.strip().split('=')
                    if len(parts) == 2:
                        email, money = parts
                        if email == self.email:
                            found = True
                            if float(money) > 0:
                                amount = float(input("How much money would You like to withdraw?\n\n: "))
                                if amount > float(money):
                                    return False
                                else:
                                    money = float(money) - amount
                                    f.write(f"{self.email}={money}\n")
                            else:
                                return False

                        else: 
                            f.write(line)
                if not found:
                    print("No such user.")
                    return False
                return True
        except FileNotFoundError:
            print("Wallet file not found.")
        except ValueError:
            print("Wallet file corrupted.")
                        