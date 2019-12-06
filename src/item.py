# module imports from addons
from colorama import Fore

class Item:
    def __init__(self, name, description):
        self._name = name
        self._description = description
    def __str__(self):
        return f'{self._name}'
        # return (
        #     f'\nName: {self._name}\n'
        #     f'Description: {self._description}\n'
        # )

    def on_take(self):
        print(Fore.GREEN + f'\nYou have picked up {self._name}.')
    def on_drop(self):
        print(Fore.GREEN + f'\nYou have dropped {self._name}.')
    def on_inspect(self):
        print(Fore.GREEN + f'\nYou inspect the {self._name}.')
        print(f'\n{Fore.CYAN + self._name}: {Fore.WHITE + self._description}')

class Treasure(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
    
    def on_drop(self):
        print(Fore.GREEN + f"\nIt's not wise to drop your source of light!")