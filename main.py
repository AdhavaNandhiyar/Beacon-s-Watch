import csv
import os
import turtle
import random

# turtle pointer
my_turtle = turtle.Turtle()

# map for entrance
def draw_entrance(t, length):
    for _ in range(1):
        t.forward(length/2)
        t.left(90)
        t.forward(0.8*length)
        t.right(90)
        t.forward(length)
        t.left(90)
        t.forward(0.4*length)
        t.left(90)
        t.forward(length)
        t.right(90)
        t.forward(0.8*length)
        t.left(90)
        t.forward(length/2)
        t.left(90)
        t.forward(length*2)

#Map 2 - Lobby
def draw_lobby(t, length):
    for _ in range(4):
        t.forward(length/2)
        t.right(90)
        t.forward(length/2)
        t.left(90)
        t.forward(length/1)
        t.left(90)
        t.forward(length/2)
        t.right(90)
        t.forward(length/2)
        t.left(90)

#Map 3 - Kitchen
def draw_kitchen(t, length):
    for _ in range(2):
        t.forward(length)
        t.left(90)
        t.forward(length*2)
        t.left(90)

#Map 4 - Bedroom
def draw_bedroom(t, length):
    for _ in range(1):
        t.forward(2*length)
        t.left(120)
        t.forward(length)
        t.left(60)
        t.forward(length)
        t.left(60)
        t.forward(length)

#Map 5 - Lair
def draw_lair(t, length):
    for _ in range(1):
       t.circle(90)

#Map 6 - Dining Room
def draw_dining(t, length):
    t.penup()
    t.backward(length)
    t.pendown()
    for _ in range(2):
       t.forward(length*4)
       t.left(90)
       t.forward(length*2)
       t.left(90)

#Map 7 - Trophy Room
def draw_trophy(t, length):
    sides = 5
    for _ in range(sides):
        t.forward(length*2)
        t.left(360/sides)

#Map 8 - Cellar
def draw_cellar(t, length):
    for _ in range (4):
       t.forward(length*2)
       t.left(45)
       t.forward(length)
       t.left(45)

#Map 9 - armory
def draw_armory(t, length):
    for _ in range (2):
       t.forward(length*2)
       t.left(45)
       t.forward(length)
       t.left(90)
       t.forward(length)
       t.left(45)

#Map 10 - Storage
def draw_storage(t, length):
    for _ in range (4):
       t.forward(length*2)
       t.left(90)

#Map 11 - Library
def draw_library(t, length):
    sides=8
    for _ in range(sides):
        t.forward(length)
        t.left(360 / sides)

#Map 12 - Gate
def draw_gate(t, length):
    for _ in range(1):
       t.forward(length/2)
       t.left(20)
       t.forward(length*2)
       t.left(70)
       t.forward(length/2)
       t.left(70)
       t.forward(length*2)
       t.left(20)
       t.forward(length/2)
       t.goto(0,0)

#Map 13 - Exit
def draw_exit(t, length):
    for _ in range(1):
        t.backward(length / 2)
        t.left(90)
        t.backward(0.8 * length)
        t.right(90)
        t.backward(length)
        t.left(90)
        t.backward(0.4 * length)
        t.left(90)
        t.backward(length)
        t.right(90)
        t.backward(0.8 * length)
        t.left(90)
        t.backward(length / 2)
        t.left(90)
        t.backward(length * 2)

def create_rooms():
    # Return a dictionary defining room properties and their other keys and values
    return {
        "entrance": {"name": "entrance", "description": "A dark and dreary opening into a dungeon. Enter at your risk", "has_treasure": False, "connected_rooms": ["lobby"], "has_item": False, "draw": draw_entrance},
        "lobby": {"name": "lobby", "description": "A large, open room with a high ceiling. There is a delectable smell to your left", "has_treasure": False, "connected_rooms": ["entrance", "kitchen", "bedroom", "armory"], "has_item": False, "draw": draw_lobby},
        "wine cellar": {"name": "wine cellar", "description": "A wide room filled to the walls with various jugs of wine. There seems to be a paper in an empty bottle maybe you should check it?", "has_treasure": False, "connected_rooms": ["dining room", "armory", "library"], "has_item": True, "draw": draw_cellar},
        "lair": {"name": "lair", "description": "A room with a big dreary troll but luckily it's asleep. There seems to be a treasure on its head but it's best to run away and come back with a weapon", "has_treasure": True, "connected_rooms": ["dining room"], "has_item": False, "draw": draw_lair},
        "kitchen": {"name": "kitchen", "description": "A dimily lit room with stoves, cabinets, and an oven yet none of them seem able to work.", "has_treasure": False, "connected_rooms": ["lobby", "dining room"], "has_item": False, "draw": draw_kitchen},
        "dining room": {"name": "dining room", "description": "A hanging lamp over a dining table, with various items on the table", "has_treasure": False, "connected_rooms": ["lair", "kitchen", "wine cellar"], "has_item": False, "draw": draw_dining},
        "armory": {"name": "armory", "description": "A room filled with different weapons! maybe one can help?", "has_treasure": False, "connected_rooms": ["wine cellar", "lobby"], "has_item": True, "draw": draw_armory},
        "bedroom": {"name": "bedroom", "description": "A cold room with various dressers filled with items but it seems like there is something shining on the shelf", "has_treasure": False, "connected_rooms": ["lobby", "trophy room"], "has_item": True, "draw": draw_bedroom},
        "trophy room": {"name": "trophy room", "description": "A room filled with various trinkets and treasures. But you see in the corner a safe. Maybe it is useful?", "has_treasure": True, "connected_rooms": ["bedroom", "storage room"], "has_item": False, "draw": draw_trophy},
        "storage room": {"name": "storage room", "description": "A large, open room with various items scattered around", "has_treasure": False, "connected_rooms": ["trophy room"], "has_item": False, "draw": draw_storage},
        "library": {"name": "library", "description": "A wide room filled with various shelves of books and artifacts. You see in the middle of the shelves a large display case wth a Treasure but it is locked.", "has_treasure": True, "connected_rooms": ["wine cellar", "gate"], "has_item": False, "draw": draw_library},
        "gate": {"name": "gate", "description": "A cold and damp room with a huge gate with 3 holes for treasures. There is some light peering out of the crack.", "has_treasure": False, "connected_rooms": ["library", "exit"], "has_item": False, "draw": draw_gate},
        "exit": {"name": "exit", "description": "You have reached the exit and have won the game congrats!", "has_treasure": False, "connected_rooms": [], "has_item": False, "draw": draw_exit},
    }

# Initialize treasures dictionaries 
def create_treasures():
    # Return a dictionary indicating which rooms contain treasures.
    return {"trophy room": True, "lair": True, "library": True}

# Initialize items dictionaries
def create_items():
    # Return a dictionary indicating which rooms contain items.
    return {"armory": True, "bedroom": True, "wine cellar": True}

# Initialize monster dictionaries
def create_monster():
    # Return a dictionary defining the monster's name and health and damage.
    return {"name": "Troll", "health": 50, "dead": False}

# Print room information from its dictionary
def describe_room(current_room):
    # Displays the current room's name.
    print(f"\nYou are in {current_room['name']}")  
    # Display the current room's description from its dictionary
    print(current_room['description']) 

# Handle treasure collection dictionaries
def collect_treasure(current_room, treasures, items, monster):
    # Check if the room has treasure.
    if current_room["has_treasure"]: 
        if current_room["name"] == "trophy room":
            if items["wine cellar"] == False:
                choice = input("You approach the safe in corner and unlock it with the code and see a treasure! Do you want to pick it up? (y/n): ").lower()
                # If player chooses to collect treasure.
                if choice == "y":  
                    # Mark the treasure as collected.
                    current_room["has_treasure"] = False 
                    # Update treasures dictionary.
                    treasures[current_room["name"]] = False 
                    # change the room description
                    current_room["description"] = "A room filled with various trinkets and treasures. The safe is left open."
                    print("You picked up the treasure from the safe!")
                elif choice == "n":
                    # change the room description
                    current_room["description"] = "A room filled with various trinkets and treasures. The safe is left open with the treasure stil in it."
            else:
                # inform player item is needed to get treasure
                print("There seems to be treasure near by but you need an item. The wine cellar may seem useful")
        elif current_room["name"] == "library":
            if items["bedroom"] == False:
                choice = input("You approach the large display case and using the key from the bedroom you unlock it and see a treasure! Do you want to pick it up? (y/n): ").lower()
                # If player chooses to collect treasure.
                if choice == "y":  
                    # Mark the treasure as collected.
                    current_room["has_treasure"] = False 
                    # Update treasures dictionary.
                    treasures[current_room["name"]] = False 
                    # change the room description
                    current_room["description"] = "A wide room filled with various shelves of books and artifacts. You see in the middle of the shelves a large display case opened."
                    print("You picked up the treasure!")
                elif choice == "n":
                    # change the room description
                    current_room["description"] = "A wide room filled with various shelves of books and artifacts. You see in the middle of the shelves a large display case opened with the treasure on it."
            else:
                # inform player item is needed to get treasure
                print("The case needs to be unlocked with a key! The bedroom may be useful")
        elif current_room["name"] == "lair":
            if items["armory"] == False and monster["dead"] == True: 
                choice = input("You see the Troll's corpse with the shiny treasure still on its head. Do you want to pick it up? (y/n): ").lower()
                # If player chooses to collect treasure.
                if choice == "y":  
                    # Mark the treasure as collected.
                    current_room["has_treasure"] = False 
                    # Update treasures dictionary.
                    treasures[current_room["name"]] = False 
                    # change the room description
                    current_room["description"] = "A room with a dead Troll evidently from your fight with it."
                    print("You pull the treasure off the trolls head and have now acquired a treasure!")
            else:
                # infroms player based on conditions of the monstr and player
                if items["armory"] == True and monster["dead"] == False:
                    print("The troll is asleep so its probably best to head to the armory to pick up some weapons to fight it")
                elif items["armory"] == False and monster["dead"] == False:
                    print("Its too risky to grab the treasure while its alive. You should fight the troll first. Make sure to Win!")
    else:
        # infrom player no treasure in room
        print("It seems this room doesn't have a hint of treasure in it")

# Handle item collection dictionaries
def collect_item(current_room, items):
    # Check if the room has an item.
    if current_room["has_item"] == True: 
        if current_room["name"] == "bedroom":
            # get players input
            choice = input("You approach the shiny object on the shelf and see a key! Do you want to pick it up? (y/n): ").lower()
            # If player chooses to collect item.
            if choice == "y":  
                # Mark the item as collected.
                current_room["has_item"] = False 
                # Update items dictionary.
                items[current_room["name"]] = False 
                # change the room description
                current_room["description"] = "A cold room with various dressers filled with items"
                print("You grab the key off the shelf and have accquired a key!")
        elif current_room["name"] == "wine cellar":
            # get players input
            choice = input("You approach the bottle and see the paper has varuous numbers on it! Do you want to open it and grab the paper? (y/n): ").lower()
            # If player chooses to collect item.
            if choice == "y":  
                # Mark the item as collected.
                current_room["has_item"] = False 
                # Update items dictionary.
                items[current_room["name"]] = False 
                # change the room description
                current_room["description"] = "A wide room filled to the walls with various jugs of wine."
                print("You open the bottle and take out the paper and see it is the combination to the safe!")
        elif current_room["name"] == "armory":
            # get players input
            choice = input("You approach the weapons on the wall. This may help against the troll. Do you want to grab a weapon? (y/n): ").lower()
            # If player chooses to collect item.
            if choice == "y":  
                # Mark the item as collected.
                current_room["has_item"] = False 
                # Update items dictionary.
                items[current_room["name"]] = False 
                # change the room description
                current_room["description"] = "A room filled with different weapons!"
                print("You picked up Sword and grabbed a light of the wall! You are now armed")
    else:
        # inform player no items are useful in the room
        print("It seems this room doesn't have any useful items in it")

# Monster encounter 
def fight_monster(current_room, monster, items):
    # Check to make sure monster is dead so to not start a fight
    if monster["dead"] == True:
        print("You have killed the monster there is no more need to fight!")
    # Check parameter to start fight
    elif current_room["has_treasure"] and monster["dead"] == False and items["armory"] == False:
        print("You awaken the troll and stun it with a light! prepare to fight for its treasure!")
        # initialize the players health
        player_health = 50
        # Fight until the monster's health reaches 0.
        while monster["health"] > 0:
            # player input
            choice = input("Would you like to attack the troll? (y/n): ").lower()
            # if player attacks
            if choice == "y":
                # Player attacks.
                print(f"You attack the {monster['name']} with your sword.") 
                # Damage player does
                damage = random.randint(5, 12)
                # Reduce monster's health by damage dealt.
                monster["health"] -= damage 
                #Tell the amount of health monster has and how much damage dealt
                print(f'You deal {damage} damage! The {monster['name']} has {monster['health']} health left!')
            if monster["health"] > 0:
                # Monster attacks
                monster_attack = random.randint(3, 10)
                # inform player of their health and how much damage monster did
                print(f'The {monster['name']} deals {monster_attack} damage to you! You have {player_health} left!')
                # Lower player health
                player_health -= monster_attack
                # If players health is lower than or equal to 0 game is over
                if player_health <= 0:
                    print(f'You have failed to defeat the {monster['name']}. You Lose.')
                    return False
        # Inform player they can grab the treasure now
        print(f'With one final blow you defeat the {monster['name']}! and are now free to claim the treasure from its head')
        # Update that the monster is dead
        monster["dead"] = True
        # Update room description
        current_room["description"] = "A room with a dead Troll evidently from your fight with it. There seems to be a treasure on its head free for the taking"
    # No fight if player does not have the items from the armory
    elif current_room["has_treasure"] and monster["dead"] == False and items["armory"] == True:
        print("Best not to risk it barehanded. Try the armory for a weapon.")

# Choose the next room
def move_to_next_room(current_room, rooms, treasures):
    # Display available connected rooms.
    print("Available rooms:") 
    # for loop to go through the connected rooms
    for connected_room in current_room["connected_rooms"]:
        if connected_room != current_room["connected_rooms"][-1]:
            # Print connected rooms on the same line and end with a comma
            print(connected_room, end=", ")
        else:
            # if last connected room makes sure there is no comma
            print(connected_room, end=" ")
    print()

    # Get players input
    room_choice = input("Which room do you want to go to next? ") 
    # Checks if input is valid.
    if room_choice in current_room["connected_rooms"]:
        # check if player is in gsate
        if current_room["name"] == "gate":
            if room_choice == "exit":
                # if player wants to move to gate check if they have the requirements aka all treasures false
                if treasures["lair"] == True or treasures["trophy room"] == True or treasures["library"] == True:
                    # conditons not met so player cant move
                    print("You don't have the right number of treasures to leave")
                    return current_room
                else:
                    # conditons met so player can move
                    print("You insert the treasures into the three slots and the gate opens leading to the exit!")
        # clear the board and move the pointer back to the middle to redraw the chosen rooms map
        my_turtle.clear()
        my_turtle.home()
        rooms[room_choice]["draw"](my_turtle, 100)
        # check if player is in exit
        if room_choice == "exit":
            print("You have reached the exit and have won the game congrats!")
        # Return the chosen room's data.
        return rooms[room_choice] 
    else:
         # Handle's invalid input.
        print("Invalid room choice. Please choose a valid room.") 
        # Keeps the player in the current room.
        return current_room 

# makes instructions for player
def instructions():
    print("\nExplore connected rooms, collect treasures, and navigate carefully.")
    print("Once all treasures are collected, head to the gate and insert the treasures into it to leave.")
    print("Use the room menu for actions and navigation.\n")

# main menu/start menu
def main_menu(game_started):
    # loop until player wants to play game
    while True:
        # menu options
        print("\nGame Start Menu")
        print("Select one of the following:")
        # checks if game has started to change option
        if game_started:
            print("1 - Return Back to the Game")
        else:
            print("1 - Play the Game")
        print("2 - Instructions")
        print("3 - Quit")
        # get players choice
        choice = input("Enter your choice: ")
        if choice == "1":
            # ends the loop to continue
            return False
        elif choice == "2":
            # calls the instructions function
            print("You are reading the instructions.")
            instructions()
        elif choice == "3":
            # ends the game
            print("You are ending the game.")
            exit()
        else:
            # handles non valid inputs
            print("You made an Illegal Choice.")

# checks to see if player wins and ends if so
def check_win(treasures, current_room):
    if current_room["name"] == "exit" and treasures["lair"] == False and treasures["trophy room"] == False and treasures["library"] == False:
        exit()

# Main game loop
def main():
    print("Welcome the the Game: Dungeon Explorer")
    # make a variabe to see if game has bee started
    game_started = False
    # call the start menu
    main_menu(game_started)
    # makes the variable true so there is a slight tweek in main menu function now that game started
    game_started = True
    # Initialize room data by calling 'create_rooms'.
    rooms = create_rooms()
    # Initialize treasure data by calling 'create_treasure()' function.
    treasures = create_treasures() 
    # Initialize item data by calling 'create_item()' function.
    items = create_items()
    # Initialize monster data by calling 'create_monster()' function.
    monster = create_monster()
    # Start in the entrance
    current_room = rooms["entrance"] 
    # draw the entrance map
    current_room["draw"](my_turtle, 100)

    # Main game loop
    while True:
        # Display current room details.
        describe_room(current_room)
        # menu funciton for player inputs
        print("\nRoom Menu")
        print("Select one of the following:")
        print("1 - Look for Treasure")
        print("2 - Look for Items")
        print("3 - Move to Another Room")
        print("4 - Fight monster (Not usable unless in lair)")
        print("5 - Return to Game Start Menu")
        # get players input
        choice = input("Enter your choice: ")

        if choice == "1":
            # calls collect treasure
            print("You are looking for treasures.")
            collect_treasure(current_room, treasures, items, monster)
        elif choice == "2":
            # calls collect items
            print("You are looking for items.")
            collect_item(current_room, items)
        elif choice == "3":
            # moves player to chosen room
            print("You are moving to another room.")
            # Move to the next room.
            current_room = move_to_next_room(current_room, rooms, treasures) 
        elif choice == "4":
            # checks if player is in valid room for this option and if so calls fight monster
            if current_room["name"] == "lair":
                fight_monster(current_room, monster, items)
            else:
                print("You are not in the correct room for this to work")
        elif choice == "5":
            # goes back to main menu
            print("You are returning back to the start menu.")
            main_menu(game_started)
        else:
            # handles misinput
            print("You made an Illegal Choice.")
        
        # checks at the end of every loop if player is in exit and has all three treasures to win the game and stops the loop
        check_win(treasures, current_room)

# Start the game
main()