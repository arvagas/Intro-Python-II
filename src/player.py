# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, items = []):
        self.name = name
        self.current_room = current_room
        self.items = items
    def __str__(self):
        return (
            f'\nName: {self.name}\n'
            f'Current Room: {self.current_room}\n'
            f'Items Holding: {self.items}\n'
        )