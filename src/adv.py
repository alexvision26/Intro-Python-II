from room import Room
from player import Player
from item import Item
import os

# Declare all the rooms..

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# gandalf = Player("Gandalf", 100, 100, 1, ["Magic Staff"], room['outside'])
# print(gandalf.__str__())

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def clear():
    os.system('cls')

iron_dagger = Item("Iron Dagger", "Pointy!")

intro = False
act1 = False
act2 = False
act3 = False
act4 = False
start = input("Would you like to begin your journey? Y/N ")
clear()
if start in ['y', 'Y']:
    intro = True
elif start in ['n', 'N']:
    print("Returning to the main menu...")
    clear()

while intro == True:
    name = input("Welcome to your first quest! What is your name, traveler?\nEnter your name: ")
    new_char = Player(name.capitalize(), 100, 100, 1, [], room['outside'])
    clear()
    print("Here is a look at your stats:\n")
    print(new_char.__str__())
    input("Press enter to continue...")
    clear()
    print("You begin your quest", new_char.location)
    fwd = input("Continue into the dark cave? Y/N ")
    if start in ['y', 'Y']:
        new_char.move_room('n')
        act1 = True
        clear()
    elif start in ['n', 'N']:
        input("Returning to the main menu... Press enter to continue")
        intro = False
        clear()
    while act1 == True:
        print("You enter the",new_char.location)
        next_move = input("Which direction will you go? ")
        if next_move in ['n','s','e', 'w']:
            clear()
            new_char.move_room(next_move)
        else:
            print("Not a valid direction.")
            input("Press enter to return to the last checkpoint! ")


# while intro == True:
#     name = input("Welcome to your first quest! What is your name, traveler?\nName: ")
#     new_char = Player(name.capitalize(), 100, 100, 1, ["Iron Dagger"], room['outside'])
#     print(new_char.location)
#     input("Press enter to see your stats... \r")
#     clear()
#     print("\nHere's a look at your current stats:\n" + new_char.__str__())
#     pt1 = input("Enter the cave?: Y/N ")
#     if pt1 == "Y" or "y":
#         intro = False
#         act1 = True
#     elif pt1 == "N" or "n":
#         print("Game over.")
#         intro = False
#     else:
#         input("Invalid input. Press enter to return...")
# while act1 == True:
#         new_char.location = room['outside'].n_to
#         print("You enter the cave, ready to face what lies ahead...")
#         print("You are now in the", new_char.location, ".")
#         next_move = input("Which way will you go...? ")
#         if next_move in ['n','s','e', 'w']:
#             new_char.move_room(next_move)
#             print(new_char.location)
#             input("test")
#         else:
#             print("Not a valid direction.")
#             input("Press enter to return to the last checkpoint! ")

# Finding an item script
# print('You find the remains of a fallen adventurer and a small, iron dagger.')
#             get_item = input('Pick up the iron dagger? Y/N ')
#             if get_item in ['y','Y']:
#                 new_char.pick_item(iron_dagger.name)
#                 input("Press enter to view your inventory")
#                 clear()
#                 print(new_char.__str__())
#                 input("Press enter to continue...")
#                 clear()
#             elif get_item in ['n', 'N']:
#                 input("You leave the dagger. Press enter to continue...")
#                 clear()
