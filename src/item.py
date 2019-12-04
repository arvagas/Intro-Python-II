class Item:
    def __init__(self, name, description):
        self._name = name
        self._description = description
    def __str__(self):
        return (
            f'\nName: {self._name}\n'
            f'Description: {self._description}\n'
        )

    def on_take(self):
        print(f'\nYou have picked up {self._name}.')
    def on_drop(self):
        print(f'\nYou have dropped {self._name}.')
    def on_inspect(self):
        print(f'\n{self._name}: {self._description}')

class Treasure(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
    
    def on_drop(self):
        print(f"\nIt's not wise to drop your source of light!")