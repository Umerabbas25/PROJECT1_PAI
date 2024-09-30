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


# bake cake
def bake_cake(game_state):
    if game_state['current_room'] != 'Kitchen':
        print("You need to be in the Kitchen to bake a cake.")
        return
    ingredients_needed = ['flour', 'water', 'yeast']
    if all(ingredient in game_state['inventory'] for ingredient in ingredients_needed):
        print("You have baked a cake!")
        game_state['inventory'].append('cake')
        game_state['cake_baked'] = True
        for ingredient in ingredients_needed:
            game_state['inventory'].remove(ingredient)
    else:
        print("You don't have the necessary ingredients to bake a cake.")

# match symbol        
def match_symbols(game_state):
    print("You need to enter a combination of symbols to activate the lever.")
    print("Symbols available: triangle (T), circle (C), square (S), oval (O)")
    print("You can combine them using + for addition and * for multiplication and - for subtraction")

    user_input = input("Enter your symbols: ").strip().lower()

    # Correct combination
    correct_combination = "t+c-o*s"   

    # Evaluate the user's input and compare with the correct combination
    if user_input.replace(' ', '') == correct_combination.replace(' ', ''):
        print("You matched the symbols correctly! The lever activates.")
        return True
    else:
        print("Your combination is incorrect. Try again. Hint: Use basic arithmetic.")
        return False
# riddle 
def solve_riddle(game_state):
    if game_state['current_room'] != 'Gallery':
        print("You need to be in the Gallery to solve the riddle.")
        return
    if game_state['riddle_solved']:
        print("You have already solved the riddle.")
        return
    answer = input("What has many keys but can’t open a single door? ").lower()
    if answer == rooms['Gallery']['riddle_answer']:
        print("You solved the riddle! The Hidden Passage is now unlocked.")
        game_state['riddle_solved'] = True
    else:
        print("Incorrect answer. Try again. Hint: Think of something musical.")




# Function to display the available commands
def help_menu():
    print("""
    COMMANDS:
    - move [direction] (north, south, east, west)
    - look: Describe the current room
    - take [item]: Pick up an item
    - drop [item]: Drop an item from your inventory
    - show: Show your inventory
    - bake: Bake a cake in the kitchen
    - riddle: Solve the riddle in the gallery
    - save: Save the current game state
    - load: Load a saved game state
    - help: Show this help menu
    - quit: Exit the game
    """)

# file handling
def save_game(game_state):
    try:
        with open('game_state.json', 'w') as save_file:
            json.dump(game_state, save_file)
            print("Game saved successfully!")
    except Exception as e:
        print(f"An error occurred while saving the game: {e}")

def load_game():
    try:
        with open('game_state.json', 'r') as load_file:
            game_state = json.load(load_file)
            print("Game loaded successfully!")
            describe_room(game_state['current_room'])
            return game_state
    except FileNotFoundError:
        print("No saved game found.")
        return None
    except Exception as e:
        print(f"An error occurred while loading the game: {e}")
        return None



def main():
    print("Welcome to 'The Mysterious Castle Adventure'!")
    help_menu()
    while True:
        command = input("\nEnter a command: ").lower().split()
        if not command:
            print("Please enter a command.")
            continue

        action = command[0]
        if action == 'move' and len(command) > 1:
            move(game_state, command[1])
        elif action == 'look':
            look(game_state)
        elif action == 'take' and len(command) > 1:
            take_item(game_state, ' '.join(command[1:]))
        elif action == 'drop' and len(command) > 1:
            drop_item(game_state, ' '.join(command[1:]))
        elif action == 'show':
            show_item(game_state)
        elif action == 'bake':
            bake_cake(game_state)
        elif action == 'riddle':
            solve_riddle(game_state)
        elif action == 'save':
            save_game(game_state)
        elif action == 'load':
            loaded_state = load_game()
            if loaded_state:
                game_state.update(loaded_state)
        elif action == 'help':
            help_menu()
        elif action == 'quit':
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid command. Type 'help' for a list of commands.")



if __name__ == "main":
    main()

main()