import textwrap
from room import Room
from player import Player
from item import Item
from item import Treasure
from item import LightSource

# Declare all items
item = {
    'map':              Item('map',
                            'Hopefully leads you to riches.'),
    'note':             Item('note',
                            '"Better luck next time!"'),
    'broken_glasses':   Item('broken_glasses',
                            'Looks like someone lost. Badly.'),
    'ruby_ring':        Treasure('ruby_ring',
                                'A beautiful red gem right in center'),
    'lamp':             LightSource('lamp',
                                    'Gives off a warm glow.'),
}

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons.",
                    ['lamp']),

    'foyer':    Room("Foyer",
                    "Dim light filters in from the south. " \
                    f"Dusty passages run north and east."),

    'overlook': Room("Grand Overlook",
                    "A steep cliff appears before you, falling " \
                    f"into the darkness. Ahead to the north, a " \
                    f"light flickers in the distance, but there " \
                    f"is no way across the chasm."),

    'narrow':   Room("Narrow Passage",
                    "The narrow passage bends here from west to " \
                    f"north. The smell of gold permeates the air."),

    'treasure': Room("Treasure Chamber",
                    "You've found the long-lost treasure chamber! " \
                    f"Sadly, it has already been completely " \
                    f"emptied by earlier adventurers. The only " \
                    f"exit is to the south.",
                    ['note', 'broken_glasses', 'ruby_ring']),
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
adventurer = Player(an_input, 'outside', ['map'])

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
        print(f'{adventurer.name} enters the {room[adventurer.current_room].name}.')
    else:
        print(f'{adventurer.name} could not go that way.')

while True:
    # Display where the player is
    print(f'\n{adventurer.name} is currently in the {room[adventurer.current_room].name}.')
    # Description of room; defaults text width to 70 characters
    room_desc = textwrap.wrap(f'{room[adventurer.current_room].description}')
    for i in room_desc:
        print(f'{i}')
    # Display items in the room, if available
    if room[adventurer.current_room].items == []:
        print('There are no items to be found.')
    else:
        item_list = ''
        for i in room[adventurer.current_room].items:
            item_list += f'{i} '
        print(f'{adventurer.name} sees the following items: {item_list}')

    # Wait for user input before proceeding
    user_input = input('\nWhat next?: ')
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
            print(f'\n{adventurer.name} attempts to go {direction}...\n')
            valid_room(user_input)
        # Check inventory
        elif user_input in ['i', 'inventory']:
            if adventurer.items == []:
                print(f'\n{adventurer.name} is currently not holding anything.')
            else:
                item_list = ''
                for i in adventurer.items:
                    item_list += f'{i} '
                print(f'\n{adventurer.name} is currently holding: {item_list}')
        # Quit game
        elif user_input in ['q', 'quit']:
            print('\nGoodbye, for now...')
            break
        else:
            print(f'\n{adventurer.name} twiddles their thumbs in silence.')
    # Start of two word actions
    elif len(ui_list) == 2:
        # Take items
        if ui_list[0] in ['get', 'take']:
            if ui_list[1] in room[adventurer.current_room].items:
                adventurer.items.append(ui_list[1])
                room[adventurer.current_room].items.remove(ui_list[1])
                item[ui_list[1]].on_take()
            else:
                print('\nThat item is not available here.')
        # Drop items
        elif ui_list[0] == 'drop':
            if ui_list[1] in adventurer.items:
                adventurer.items.remove(ui_list[1])
                room[adventurer.current_room].items.append(ui_list[1])
                item[ui_list[1]].on_drop()
            else:
                print('\nYou are not carrying that item.')
        # Inspect items
        elif ui_list[0] == 'inspect':
            if ui_list[1] in adventurer.items or \
                ui_list[1] in room[adventurer.current_room].items:
                item[ui_list[1]].on_inspect()
            else:
                print('\nThat item is no where to be found.')
        else:
            print(f'\n{adventurer.name} twiddles their thumbs in silence.')
    else:
        print(f'\n{adventurer.name} twiddles their thumbs in silence.')