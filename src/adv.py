import textwrap
from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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
player_monty = Player('Monty', 'outside')

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
while True:
    print(f'{player_monty.name} is currently in the {room[player_monty.current_room].name}.')
    print(room[player_monty.current_room].description)

    user_input = input('Where to?: ')

    if user_input == 'n':
        print(f'\n{player_monty.name} attempts to go north...\n')
        if hasattr(room[player_monty.current_room], 'n_to') == True:
            # find the key name of the matching value https://stackoverflow.com/a/13149770
            player_monty.current_room = list(room.keys())[list(room.values()).index(room[player_monty.current_room].n_to)]
        else:
            print(f'{player_monty.name} could not go that way.\n')
    elif user_input == 's':
        print(f'\n{player_monty.name} attempts to go south...\n')
        if hasattr(room[player_monty.current_room], 's_to') == True:
            player_monty.current_room = list(room.keys())[list(room.values()).index(room[player_monty.current_room].s_to)]
        else:
            print(f'{player_monty.name} could not go that way.\n')
    elif user_input == 'e':
        print(f'\n{player_monty.name} attempts to go east...\n')
        if hasattr(room[player_monty.current_room], 'e_to') == True:
            player_monty.current_room = list(room.keys())[list(room.values()).index(room[player_monty.current_room].e_to)]
        else:
            print(f'{player_monty.name} could not go that way.\n')
    elif user_input == 'w':
        print(f'\n{player_monty.name} attempts to go west...\n')
        if hasattr(room[player_monty.current_room], 'w_to') == True:
            player_monty.current_room = list(room.keys())[list(room.values()).index(room[player_monty.current_room].w_to)]
        else:
            print(f'{player_monty.name} could not go that way.\n')
    elif user_input == 'q':
        print('\nThanks for playing!')
        break
    else:
        print('\nYou shall not pass!\n')