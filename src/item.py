class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __str__(self):
        return (
            f'\nName: {self.name}\n'
            f'Description: {self.description}\n'
        )

    def on_take(self):
        print(f'\nYou have picked up {self.name}.')
    def on_drop(self):
        print(f'\nYou have dropped {self.name}.')
    def on_inspect(self):
        print(f'\n{self.name}: {self.description}')

class Treasure(Item):
    def __init__(self, name, description, power):
        self.power = power
        super().__init__(name, description)
    def __str__(self):
        return (
            f'\nName: {self.name}\n'
            f'Description: {self.description}\n'
            f'Power: {self.power}\n'
        )