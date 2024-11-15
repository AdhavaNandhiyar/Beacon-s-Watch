import turtle

def draw_square(t, length):
   """Draws a square with the given turtle and side length."""
   for _ in range(2):                  #Draws rectangle with side length of length/2
       t.forward(length/2)
       t.left(90)
       t.forward(2*length)
       t.left(90)

def draw_circle(t, radius):
   """Draws a circle with the given turtle and radius."""
   t.circle(radius)

def draw_circle(t, radius):
   """Draws a circle with the given turtle and radius."""
   t.circle(radius)                    #Draws Circle for room
   t.penup()
   t.goto(0,200)
   t.pendown()
   t.circle(radius*.6)

def draw_square(t, length):
   """Draws a square with the given turtle and side length."""
   t.goto(-100,0)                      #Centers turtle on screen
   for _ in range(4):                  #Makes a square with side length of 2xlength
       t.forward(length*2)
       t.left(90)
   t.penup()
   t.goto(0,200)                       #Picks up pen, moves, puts pen down
   t.pendown()
   t.circle(50)  

def draw_square(t, length):
   """Draws a square with the given turtle and side length."""
   t.goto(-100, 0)                 #Center turtle on screen
   for _ in range(4):              #Draws Square with side length of 2xlength
       t.forward(length * 2)
       t.left(90)
   t.penup()                       #Picks pen up
   t.goto(-5,200)                  #Moves pen
   t.pendown()                     #Drops pen
   for _ in range(2):              #Draws small rectangle
       t.forward(10)
       t.left(90)
       t.forward(20)
       t.left(90)
   t.penup()                       #Picks Pen up
   t.goto(2.5,220)                 #Moves Pen
   t.pendown()                     #Drops pen
   t.circle(50)    

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
