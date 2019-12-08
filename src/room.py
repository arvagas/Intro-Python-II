# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, items, is_light = False,):
        self._name = name
        self._description = description
        self.items = items
        self.is_light = is_light
        self.n_to = {}
        self.s_to = {}
        self.e_to = {}
        self.w_to = {}
    def __str__(self):
        return (
            f'\nName: {self._name}\n'
            f'Description: {self._description}\n'
            f'Available Items: {self.items}\n'
            f'Natural Lighting: {self.is_light}\n'
        )
    
    def loot_dropped(self, item_dropped):
        self.items.append(item_dropped)
    def loot_taken(self, item_taken):
        self.items.remove(item_taken)