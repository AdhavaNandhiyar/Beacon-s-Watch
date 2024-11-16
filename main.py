import turtle

class Player:
    def __init__(self):
        self.item = False

class Room:
    def __init__(self, description =""):
        self.description = description or ""

class Item:
    def __init__(self, description =""):
        self.description = description or ""

class Monster:
    def __init__(self, name, attack, health, description =""):
        self.name = name
        self.attack = attack
        self.health = health
        self.description = description or ""

bear = Monster("Bear", 4, 40, "A large black bear with a scar on its chest")

devilsIslandKey = Item()
outerIslandKey = Item()
bulb = Item()
flashlight = Item()
logbook = Item()
flareGun = Item()
keyset = Item()
fuse = Item()
tranquilizerGun = Item()



def start_menu():
    print("|| Beacons Watch ||")
    #Starts the game if user presses 1
    start = int(input("Press one to start the game: "))
    if start == 1:
        start_game()

def start_game():
    print()

win = False
