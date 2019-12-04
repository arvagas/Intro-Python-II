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