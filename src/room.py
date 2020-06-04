# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, room, desc, items=[], n_to=None, s_to=None, e_to=None, w_to=None):
        self.room = room
        self.desc = desc
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.items = items
    def __str__(self):
        return f"{self.room}: {self.desc}."
    def curr_items(self):
        print("You find:")
        # for x in self.items: print(x.name)
        print(self.items[0].name)
    def remove_item(self):
        self.items.pop(0)
