import json

# ROOMS DICTIONARY
rooms = {
    'Entrance': {
        'description': 'You are at the entrance of the castle. Wooden doors behind you creak ominously.',
        'exits': {'north': 'Grand Hall'},
        'items': []
    },
    'Grand Hall': {
        'description': 'The Grand Hall is filled with ancient tapestries and a chandelier. Exits lead in all directions.',
        'exits': {'south': 'Entrance', 'east': 'Dining Room', 'west': 'Armory', 'north': 'Gallery'},
        'items': ['sword']
    },
    'Dining Room': {
        'description': 'The Dining Room has a long table with a feast long forgotten.',
        'exits': {'west': 'Grand Hall', 'north': 'Kitchen'},
        'items': ['candle', 'fork', 'plate']
    },
    'Kitchen': {
        'description': 'The Kitchen smells of old bread. Pots and pans are scattered about. There is also a task here.',
        'exits': {'south': 'Dining Room'},
        'items': ['flour', 'water', 'yeast']
    },
    'Armory': {
        'description': 'The Armory contains rusty weapons and shields. There is a door to the Dungeon outside of which a monster is blocking the door',
        'exits': {'east': 'Grand Hall', 'north': 'Dungeon'},
        'items': ['battle axe', 'armor', 'helmet']
    },
    'Dungeon': {
        'description': 'The Dungeon is dark and damp, with the sound of chains rattling.',
        'exits': {'south': 'Armory'},
        'items': ['bronze key']
    },
    'Gallery': {
        'description': 'The Gallery has walls adorned with paintings of people long forgotten. There is a riddle to solve.',
        'exits': {'south': 'Grand Hall', 'north': 'Hidden Passage'},
        'items': ['painting', 'statue'],
        'puzzle': 'Solve the riddle to unlock the Hidden Passage: "What has many keys but can’t open a single door?"',
        'riddle_answer': 'piano'
    },
    'Hidden Passage': {
        'description': 'A narrow passage hidden behind a painting. It leads to the Tower.',
        'exits': {'south': 'Gallery', 'north': 'Tower'},
        'items': []
    },
    'Tower': {
        'description': 'The Tower is tall and overlooks the entire castle. A symbol-matching puzzle blocks the final door.',
        'exits': {'south': 'Hidden Passage', 'north': 'Courtyard'},
        'puzzle': 'Match the correct symbols to activate the lever and open the final door.',
        'items': [],
        'locked': True
    },
    'Courtyard': {
        'description': 'YOU WON ,The Courtyard is bright and filled with greenery. You have escaped the castle!',
        'exits': {},
        'items': []
    }
}
# GAME STATE
game_state = {
    'current_room': 'Entrance',
    'inventory': [],
    'symbol_puzzle_solved': False,
    'riddle_solved': False,
    'cake_baked': False,
    'candle_taken': False,
    'bag_limit': 7
}

def move(game_state, direction):
    try:
        current_room = game_state['current_room']
        if direction in rooms[current_room]['exits']:
            next_room = rooms[current_room]['exits'][direction]

            # Check if entering the Dungeon
            if next_room == 'Dungeon':
                if not game_state['cake_baked']:
                    print("A monster is blocking the way!")
                    return
                if not game_state['candle_taken']:
                    print("It's too dark to see! You need a light to enter the Dungeon.")
                    return
                else:
                    print("The Monster is happy with the cake and lets you through!")

            # Check if entering the Hidden Passage
            if next_room == 'Hidden Passage':
                if not game_state['riddle_solved']:
                    print("You need to solve the riddle to unlock the Hidden Passage.")
                    return

            # Check if entering the Tower
            if next_room == 'Tower':
                if 'bronze key' not in game_state['inventory']:
                    print("You need to find the bronze key to enter the Tower.")
                    return

            game_state['current_room'] = next_room
            print(f'You move {direction} to the {next_room}.')

            # Now, check the current room after moving
            if next_room == 'Tower':
                if not game_state['symbol_puzzle_solved']:
                    print(rooms[next_room]['description'])
                    if match_symbols(game_state):
                        game_state['symbol_puzzle_solved'] = True
                        print("The door to the Courtyard is open!")
                    else:
                        print("You must solve the puzzle to proceed.")
                        game_state['current_room'] = 'Hidden Passage'
                else:
                    print("You can now proceed to the Courtyard.")
                    print("AND YOU HAVE EXITED")

            else:
                describe_room(game_state['current_room'])
        else:
            print(f"You can't go {direction} from here.")
    except KeyError:
        print("Error: The room or direction does not exist.")


# inventory managment            
def describe_room(room):
    print(rooms[room]['description'])
    print("Exits: " + ", ".join(rooms[room]['exits'].keys()))
    if rooms[room]['items']:
        print("Items here: " + ", ".join(rooms[room]['items']))

def look(game_state):
    describe_room(game_state['current_room'])

def drop_item(game_state, item):
    item = item.lower()
    if item in game_state['inventory']:
        game_state['inventory'].remove(item)
        rooms[game_state['current_room']]['items'].append(item)
        print(f"You have dropped the {item}.")
    else:
        print(f"You don't have {item} in your inventory.")

def show_item(game_state):
    if game_state['inventory']:
        print("You are carrying: " + ", ".join(game_state['inventory']))
    else:
        print("You don't have anything in your bag.")


# take item         
def take_item(game_state, item):
    item = item.lower()
    if len(game_state['inventory']) >= game_state['bag_limit']:
        print("Your bag is full! You can't carry any more items.")
        return
    for room_item in rooms[game_state['current_room']]['items']:
        if item in room_item.lower():
            game_state['inventory'].append(room_item)
            rooms[game_state['current_room']]['items'].remove(room_item)
            print(f"You have taken the {room_item}.")
            if room_item == 'candle':
                game_state['candle_taken'] = True
            return
    print(f"{item} is not here.")


# puzzle
# TO BE IMPLEMNETED BY ADEEL TAHIR
def bake_cake(game_state):
    pass

# TO BE IMPLEMNETED BY ADEEL TAHIR
def match_symbols(game_state):
    pass

# TO BE IMPLEMNETED BY ADEEL TAHIR
def solve_riddle(game_state):
    pass



# TO BE IMPLEMNETED BY SHOAIB SHAHID
def help_menu():
    pass

# TO BE IMPLEMNETED BY SHOAIB SHAHID
def save_game(game_state):
    pass

def load_game():
    pass
