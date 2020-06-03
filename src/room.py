# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, room, desc):
        self.room = room
        self.desc = desc
    def __str__(self):
        return f"{self.room}: {self.desc}"
    def n_to(self):
        return f"Traveling North to, {self.room}. {self.desc}"
    # def w_to(self):
    # def s_to(self):
    # def e_to(self):
