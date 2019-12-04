import textwrap
from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     ['lamp']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ['lamp']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ['lamp', 'note', 'broken_glasses']),
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
player_monty = Player('Monty', 'outside', ['map'])

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
    if hasattr(room[player_monty.current_room], dir_to) == True:
        new_room = getattr(room[player_monty.current_room], dir_to)
        # find the key name of the matching value https://stackoverflow.com/a/13149770
        player_monty.current_room = list(room.keys())[list(room.values()).index(new_room)]
        print(f'{player_monty.name} enters the {room[player_monty.current_room].name}.\n')
    else:
        print(f'{player_monty.name} could not go that way.\n')

while True:
    print(f'{player_monty.name} is currently in the {room[player_monty.current_room].name}.')
    print(room[player_monty.current_room].description)

    if room[player_monty.current_room].items == []:
        print('There are no items to be found.')
    else:
        item_list = ''
        for i in room[player_monty.current_room].items:
            item_list += f'{i} '
        print(f'{player_monty.name} sees the following items: {item_list}')

    user_input = input('What next?: ')

    if user_input in ['n', 's', 'e', 'w']:
        if user_input == 'n':
            direction = 'north'
        elif user_input == 's':
            direction = 'south'
        elif user_input == 'e':
            direction = 'east'
        elif user_input == 'w':
            direction = 'west'
        print(f'\n{player_monty.name} attempts to go {direction}...\n')
        valid_room(user_input)
    elif user_input in ['i', 'inventory']:
        if player_monty.items == []:
            print(f'\n{player_monty.name} is currently not holding anything.\n')
        else:
            item_list = ''
            for i in player_monty.items:
                item_list += f'{i} '
            print(f'\n{player_monty.name} is currently holding: {item_list}\n')
    elif user_input == 'q':
        print('\nGoodbye, for now...')
        break
    else:
        print(f'\n{player_monty.name} twiddles their thumbs in silence.\n')