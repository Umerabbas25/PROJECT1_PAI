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