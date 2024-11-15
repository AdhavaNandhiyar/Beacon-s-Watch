import turtle

class Player:
    def __init__(self):
        self.item = False

class Room:
    def __init__(self):
        self.description = ""

class Item:
    def __init__(self):
        self.description = ""

class Monster:
    def __init__(self):
        self.name = ""



def start_menu():
    print("|| Beacons Watch ||")
    #Starts the game if user presses 1
    start = int(input("Press one to start the game: "))
    if start == 1:
        start_game()

def start_game():
    print()

win = False
