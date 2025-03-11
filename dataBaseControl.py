import os

def fileCreate():
    if not os.path.exists("dataBase.txt"):
        try:
            f = open("dataBase.txt", 'x')
            f.close()  
            print("File dataBase.txt has been created.")
        except FileExistsError:
            pass
        except Exception as e:
            print(f"Error while creating a file: {e}")
    else:
        pass