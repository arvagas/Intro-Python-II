# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __str__(self):
        return f'{self.name}: {self.description}'

    def n_to(self, north_room):
        self.n_to = north_room
    def s_to(self, south_room):
        self.s_to = south_room
    def e_to(self, east_room):
        self.e_to = east_room
    def w_to(self, west_room):
        self.w_to = west_room