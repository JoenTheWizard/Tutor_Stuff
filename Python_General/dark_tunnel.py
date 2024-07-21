import random

#You can utilize inheritance here if you want to
#For example, Orc and Boss inherits from Troll
class Troll:
    def __init__(self):
        self.health = 10
        self.power = 5
        self.loot = [Stick(), Mace()]

    def attack(self):
        print("The troll attacks with power", self.power)

    def escape(self):
        print("The troll tries to escape.")

    def perish(self):
        print("The troll perishes. And drops the following")
        for l in loot:
            print("-",type(l).__name__)


class Orc:
    def __init__(self):
        self.health = 25
        self.power = 10
        self.loot = [Mace(), Longsword()]

    def attack(self):
        print("The orc attacks with power", self.power)

    def escape(self):
        print("The orc tries to escape.")

    def perish(self):
        print("The orc perishes. And drops the following")
        for l in loot:
            print("-",type(l).__name__)


class Boss:
    def __init__(self):
        self.health = 50
        self.power = 15
        self.loot = [Staff(), Excalibur()]

    def attack(self):
        print("The boss attacks with power", self.power)

    def escape(self):
        print("The boss tries to escape.")

    def perish(self, user_weapon):
        print("The boss perishes. And drops the following")
        for l in loot:
            print("-",type(l).__name__)


class Stick:
    def __init__(self):
        self.power = 5

    def attack(self, health):
        health -= self.power


class Mace:
    def __init__(self):
        self.power = 10

    def attack(self, health):
        health -= self.power


class Longsword:
    def __init__(self):
        self.power = 15

    def attack(self, health):
        health -= self.power


class Staff:
    def __init__(self):
        self.power = 20

    def attack(self, health):
        health -= self.power


class Excalibur:
    def __init__(self):
        self.power = 25
        self.name = "Excalibur"

    def attack(self, health):
        health -= self.power


class Room:
    def __init__(self, room_name, monsters, chests, left=None, right=None, up=None, down=None, is_start=False, is_finish=False):
        self.room_name = room_name
        self.monsters = monsters
        self.chests = chests
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        self.is_start = is_start
        self.is_finish = is_finish


class Chest:
    def __init__(self, loot):
        self.loot = loot
        self.opened = False

    def open(self):
        if self.opened:
            print("The chest has already been opened.")
        else:
            print("You open the chest and find:")
            for item in self.loot:
                print("-", type(item).__name__)
            self.opened = True


#Create monster objects
monster1 = Troll()
monster2 = Orc()
monster3 = Boss()

#Create weapon objects
stick = Stick()
mace = Mace()
longsword = Longsword()
staff = Staff()
excalibur = Excalibur() 

#Create chest
chest1 = Chest([stick, staff])

#Create room objects. Start at room 1 and end at room 3
room1 = Room("Dungeon room 1", [monster1], [chest1], is_start=True)
room2 = Room("Dungeon room 2", [monster2], [])
room3 = Room("Dungeon room 3", [monster3], [], is_finish=True)

#Set room connections
# R1 -> <- R2 -> <- R3
room1.right = room2
room2.left = room1
room2.right = room3
room3.left = room2

#Initialize game state
current_room = room1
player_health = 100
current_weapon = stick

#Implement your game logic here:
while True:
  pass #Implement your code here
