# Write your game here

game_data = {
    'portal_spawn': False,
    'rooms': {
        # rooms order: zero closed, one closed, two closed, three closed
        # closed order: top, left, right, bottom
    },
    'starter_room': game_data['rooms'][0],
    'enemies': {
        # whatever we come up with
    },
    'gems': {
        # daimonds, rubies, etc.
    }
    'boss': {
        # boss stats
    }
    'room_details': {
        'plants': {
            'vines': [],
            'bushes': [],
            'grass_patches': []
        },
        'chests': [],
        'dirt_floor': []
    }
}

player_data = {
    'user_name': '',
    'gem_num': 0,
    'health': 5,
    'speed': 1,
    'models': {
        # Whatever models we design. Can be just one.
    },
    'monster_repellent': 0
}

def draw_board(screen):
    # Print the board and all game elements using curses


# Good Luck!