import textwrap
from room import Room
from player import Player
from item import Item

# Declare all items
item = {
    'lamp':             Item('lamp',
                            'Gives off a warm glow.'),
    'map':              Item('map',
                            'Hopefully leads you to riches.'),
    'note':             Item('note',
                            '"Better luck next time!"'),
    'broken_glasses':   Item('broken_glasses',
                            'Looks like someone lost. Badly.'),
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     ['lamp']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage","""The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ['note', 'broken_glasses']),
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
brave_adventurer_name = input('\nWhat is your name, brave adventurer?: ')
brave_adventurer = Player(brave_adventurer_name, 'outside', ['map'])

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

def valid_room(ui):
    dir_to = f'{ui}_to'
    if hasattr(room[brave_adventurer.current_room], dir_to) == True:
        new_room = getattr(room[brave_adventurer.current_room], dir_to)
        # find the key name of the matching value https://stackoverflow.com/a/13149770
        brave_adventurer.current_room = list(room.keys())[list(room.values()).index(new_room)]
        print(f'{brave_adventurer.name} enters the {room[brave_adventurer.current_room].name}.')
    else:
        print(f'{brave_adventurer.name} could not go that way.')

while True:
    print(f'\n{brave_adventurer.name} is currently in the {room[brave_adventurer.current_room].name}.')
    print(room[brave_adventurer.current_room].description)

    if room[brave_adventurer.current_room].items == []:
        print('There are no items to be found.')
    else:
        item_list = ''
        for i in room[brave_adventurer.current_room].items:
            item_list += f'{i} '
        print(f'{brave_adventurer.name} sees the following items: {item_list}')

    user_input = input('\nWhat next?: ')
    ui_list = user_input.split()

    if len(ui_list) == 1:
        if user_input in ['n', 's', 'e', 'w']:
            if user_input == 'n':
                direction = 'north'
            elif user_input == 's':
                direction = 'south'
            elif user_input == 'e':
                direction = 'east'
            elif user_input == 'w':
                direction = 'west'
            print(f'\n{brave_adventurer.name} attempts to go {direction}...\n')
            valid_room(user_input)
        elif user_input in ['i', 'inventory']:
            if brave_adventurer.items == []:
                print(f'\n{brave_adventurer.name} is currently not holding anything.')
            else:
                item_list = ''
                for i in brave_adventurer.items:
                    item_list += f'{i} '
                print(f'\n{brave_adventurer.name} is currently holding: {item_list}')
        elif user_input in ['q', 'quit']:
            print('\nGoodbye, for now...')
            break
        else:
            print(f'\n{brave_adventurer.name} twiddles their thumbs in silence.')
    elif len(ui_list) == 2:
        if ui_list[0] in ['get', 'take']:
            if ui_list[1] in room[brave_adventurer.current_room].items:
                brave_adventurer.items.append(ui_list[1])
                room[brave_adventurer.current_room].items.remove(ui_list[1])
                item[ui_list[1]].on_take()
            else:
                print('\nThat item is not available here.')
        elif ui_list[0] == 'drop':
            if ui_list[1] in brave_adventurer.items:
                brave_adventurer.items.remove(ui_list[1])
                room[brave_adventurer.current_room].items.append(ui_list[1])
                item[ui_list[1]].on_take()
            else:
                print('\nYou are not carrying that item.')
        else:
            print(f'\n{brave_adventurer.name} twiddles their thumbs in silence.')
    else:
        print(f'\n{brave_adventurer.name} twiddles their thumbs in silence.')