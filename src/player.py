# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, hp, mp, level, inventory, location):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.level = level
        self.inventory = inventory
        self.location = location
    def __str__(self):
        return f"Name: {self.name}\nHealth/Mana: {self.hp}/{self.mp}\nLevel: {self.level}\nItems: {self.inventory}\nZone: {self.location}"