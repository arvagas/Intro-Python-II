# module imports
import textwrap
# module imports from addons
from colorama import Fore
# class imports
from room import Room
from player import Player
from item import Item
from item import Treasure
from item import LightSource

# Declare all items
item = {
    'map':      Item('map',
                    'Hopefully leads you to riches.'),
    'note':     Item('note',
                    '"At least I left you something! -X"'),
    'lockpick': Item('lockpick',
                    'Someone beat me to the punch.'),
    'ruby':     Treasure('ruby',
                    'A tiny, red gem shines brilliantly.'),
    'lamp':     LightSource('lamp',
                    'Gives off a warm glow.'),
}

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons.",
                    [item['lamp']],
                    True),

    'foyer':    Room("Foyer",
                    "Dim light filters in from the south. " \
                    f"Dusty passages run north and east.",
                    []),

    'overlook': Room("Grand Overlook",
                    "A steep cliff appears before you, falling " \
                    f"into the darkness. Ahead to the north, a " \
                    f"light flickers in the distance, but there " \
                    f"is no way across the chasm.",
                    [],
                    True),

    'narrow':   Room("Narrow Passage",
                    "The narrow passage bends here from west to " \
                    f"north. The smell of gold permeates the air.",
                    []),

    'treasure': Room("Treasure Chamber",
                    "You've found the long-lost treasure chamber! " \
                    f"Sadly, it has already been completely " \
                    f"emptied by earlier adventurers. The only " \
                    f"exit is to the south.",
                    [item['note'], item['lockpick'], item['ruby']],
                    True),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
an_input = input('\nWhat is your name, adventurer?: ')
adventurer = Player(an_input, 'outside', [item['map']])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# Check to see if next room is available
def valid_room(ui):
    dir_to = f'{ui}_to'
    if getattr(room[adventurer.current_room], dir_to) != {}:
        new_room = getattr(room[adventurer.current_room], dir_to)
        # find the key name of the matching value https://stackoverflow.com/a/13149770
        adventurer.current_room = list(room.keys())[list(room.values()).index(new_room)]
        # print(f'You enter the {room[adventurer.current_room]._name}.')
    else:
        print(Fore.RED + '\nYou could not go that way.')

# Check to see if a lightsource exists in inventory
def ls_check(source):
    check = False
    for i in source:
        if isinstance(i, LightSource) == True:
            check = True
    return check

while True:
    lit_room = False

    # Check to see if any light source is available
    if room[adventurer.current_room].is_light == True \
        or ls_check(room[adventurer.current_room].items) == True \
        or ls_check(adventurer.items) == True:
        # Update the variable
        lit_room = True
        # Display where the player is
        print(Fore.CYAN + f'\n{room[adventurer.current_room]._name}')
        # Description of room; defaults text width to 70 characters
        room_desc = textwrap.wrap(f'{room[adventurer.current_room]._description}')
        for i in room_desc:
            print(Fore.WHITE + f'{i}')
        # Display items in the room, if available
        if room[adventurer.current_room].items == []:
            print(Fore.RED + 'There are no items to be found.')
        else:
            item_list = ''
            for i in room[adventurer.current_room].items:
                item_list += f'{i} '
            print(f'You see the following items: {Fore.YELLOW + item_list}')
    else:
        print(Fore.WHITE + "\nIt's pitch black!")

    # Wait for user input before proceeding
    user_input = input(Fore.WHITE + '\nWhat do you do next?: ')
    ui_list = user_input.split()

    # Start of one word actions
    if len(ui_list) == 1:
        # Move in a direction
        if user_input in ['n', 's', 'e', 'w']:
            if user_input == 'n':
                direction = 'north'
            elif user_input == 's':
                direction = 'south'
            elif user_input == 'e':
                direction = 'east'
            elif user_input == 'w':
                direction = 'west'
            print(Fore.GREEN + f'\nYou attempt to go {direction}...')
            valid_room(user_input)
        # Check inventory
        elif user_input in ['i', 'inventory']:
            if adventurer.items == []:
                print(Fore.RED + '\nYou are currently not holding anything.')
            else:
                item_list = ''
                for i in adventurer.items:
                    item_list += f'{i} '
                print(Fore.GREEN + f'\nYou are currently holding: {item_list}')
        # Quit game
        elif user_input in ['q', 'quit']:
            print(Fore.GREEN + '\nGoodbye, for now...')
            break
        else:
            print(Fore.RED + '\nYou twiddle your thumbs in silence.')
    # Start of two word actions
    elif len(ui_list) == 2:
        # Take items
        if ui_list[0] in ['get', 'take']:
            if lit_room == True:
                if item[ui_list[1]] in room[adventurer.current_room].items:
                    adventurer.items.append(item[ui_list[1]])
                    room[adventurer.current_room].loot_taken(item[ui_list[1]])
                    item[ui_list[1]].on_take()
                else:
                    print(Fore.RED + '\nThat item is not available here.')
            else:
                print(Fore.GREEN + '\nGood luck finding that in the dark!')
        # Drop items
        elif ui_list[0] == 'drop':
            if item[ui_list[1]] in adventurer.items:
                adventurer.items.remove(item[ui_list[1]])
                room[adventurer.current_room].loot_dropped(item[ui_list[1]])
                item[ui_list[1]].on_drop()
            else:
                print(Fore.RED + '\nYou are not carrying that item.')
        # Inspect items
        elif ui_list[0] == 'inspect':
            if item[ui_list[1]] in adventurer.items \
                or item[ui_list[1]] in room[adventurer.current_room].items:
                item[ui_list[1]].on_inspect()
            else:
                print(Fore.RED + '\nThat item is no where to be found.')
        else:
            print(Fore.RED + '\nYou twiddle your thumbs in silence.')
    else:
        print(Fore.RED + '\nYou twiddle your thumbs in silence.')