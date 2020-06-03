from room import Room
from player import Player

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

intro = False
act1 = False
act2 = False
act3 = False
act4 = False
start = input("Would you like to start a new game? Y/N ")
if start == "Y" or "y":
    intro = True

while intro == True:
    name = input("Welcome to your first quest! What is your name, traveler?\nName: ")
    new_char = Player(name.capitalize(), 100, 100, 1, ["Iron Dagger"], room['outside'])
    print("Welcome," + name.capitalize() + "here's your stats:\n" + new_char.__str__())
    print("After crossing through the dark forest on a quest given to your directly from the King, you finally reach the cave entrance... ", new_char.location)
    pt1 = input("Enter the cave?: Y/N ")
    if pt1 == "Y" or "y":
        intro = False
        act1 = True
    elif pt1 == "N" or "n":
        print("Game over.")
        intro = False
while act1 == True:
        new_char.location = room['outside'].n_to
        print("You enter the cave, ready to face what lies ahead...")
        
