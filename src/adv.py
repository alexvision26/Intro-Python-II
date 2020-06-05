from room import Room
from player import Player
from item import Item
import os

# Declare all the rooms..

iron_dagger = Item("Iron Dagger", "Pointy!")
wizard_staff = Item("Wizard Staff", "A large wooden staff with a magical aura!")
wooden_plank = Item("Wooden Plank", "A wooden plank. Maybe this can help me cross the chasm...")
wooden_shield = Item("Wooden Shield", "Slightly damaged, but solid shield made out of wood.")
family_crest_ring = Item("Family Crest Signet Ring", "This looks important... It appears someone may have dropped this accidentally.")

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [wooden_plank]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [iron_dagger, wooden_shield]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [wooden_plank]),

    'tunnel': Room("Dark Chasm", "You've crossed the dark chasm with the wooden planks. You barely make it as the planks fall into the abyss. Ahead to the north lies a narrow, dimly lit tunnel.")
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

# room['overlook'].n_to = room['tunnel']

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

unlock = True

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
    new_char = Player(name.capitalize(), 100, 100, 1, room['outside'])
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
        next_move = input("\nWhich direction will you go? \nControls available:\nDirections: N / E / S / W\nSearch room: L\nView your stats: P\nQuit: Q\nWhere would you like to go? ")
        #Check here if player inventory includes 2 planks to cross chasm, then allow north travel across chasm:
        has_planks = [p.name for p in new_char.inventory]
        if has_planks.count("Wooden Plank") == 2:
            if unlock == True:
                clear()
                input("I could use these planks to cross the chasm!\nPress Enter to continue...")
                unlock = False
            room['overlook'].n_to = room['tunnel']
        if next_move in ['n','s','e', 'w']:
            clear()
            new_char.move_room(next_move)
        elif next_move in ['l', 'L']:
            clear()
            print('You begin searching around the room...')
            if len(new_char.location.items) > 0:
                new_char.location.curr_items()
                take_items = input('Take items? Y/N ')
                if take_items in ['y','Y']:
                    for x in new_char.location.items:
                        new_char.pick_up_item(x)
                        new_char.location.remove_item()
                    input('Press enter to continue...')
                    clear()
            else:
                input("Couldn't find any items in current room. Press enter to continue...")
                clear()
        elif next_move in ['p','P']:
            clear()
            print("Here is a look at your stats:\n")
            print(new_char.__str__())
            input("Press enter to continue...")
            clear()
        elif next_move in ['q', 'Q']:
            intro = False
            act1= False
            clear()
            print("Thanks for playing!")
        else:
            print("Not a valid direction.")
            input("Press enter to return to the last checkpoint...")
