# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, hp, mp, level, location):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.level = level
        self.inventory = []
        self.location = location
    def move_room(self, direction):
        new_room = self.location.__getattribute__(f"{direction}_to")
        if new_room:
            self.location = new_room
        else:
            print("There is no path in that direction.")
    def __str__(self):
        display_inven = []
        for x in self.inventory:
            display_inven.append(x.name)
        return f"Name: {self.name}\nHealth/Mana: {self.hp}/{self.mp}\nLevel: {self.level}\nItems: {display_inven}\nZone: {self.location}"
    def pick_up_item(self, item):
            self.inventory.append(item)

            if len(self.inventory) > 1:
                self.level += 1
        # when added to inventory, also remove from room