# The goals for this phase include:
# - Pick out some icons for your game
# - Establish a starting position for each icon
# - Pick a size for your playing space
# - Print your playing space with starting position of each icon

# To make this work, you may have to type this into the terminal --> pip install curses
import curses
import random

game_data = {
    'width': 6,
    'height': 7,
    'player': {"x": 3, "y": 3, "score": 0},
    # 'eagle_pos': {"x": 4, "y": 4},
    'collectibles': [
        {"x": 3, "y": 1, "collected": False, "how many": 0},
    ],
    'hearts': ['live', 'live', 'live', 'live', 'live'],
    'doorways + basics': {
        'basics': [
            {"x": 1-1, "y": 1-1},
            {"x": 1-1, "y": 2-1},
            {"x": 1-1, "y": 5-1},
            {"x": 1-1, "y": 6-1},
            {"x": 2-1, "y": 1-1},
            {"x": 2-1, "y": 2-1},
            {"x": 2-1, "y": 5-1},
            {"x": 2-1, "y": 6-1},
            {"x": 5-1, "y": 1-1},
            {"x": 5-1, "y": 2-1},
            {"x": 5-1, "y": 5-1},
            {"x": 5-1, "y": 6-1},
            {"x": 6-1, "y": 1-1},
            {"x": 6-1, "y": 2-1},
            {"x": 6-1, "y": 5-1},
            {"x": 6-1, "y": 6-1}
        ],
        'block top': [
            {"x": 3-1, "y": 1-1},
            {"x": 4-1, "y": 1-1},
            {"x": 3-1, "y": 2-1},
            {"x": 4-1, "y": 2-1}
        ],
        'block left': [
            {"x": 1-1, "y": 3-1},
            {"x": 2-1, "y": 3-1},
            {"x": 1-1, "y": 4-1},
            {"x": 2-1, "y": 4-1}
        ],
        'block right': [
            {"x": 5-1, "y": 3-1},
            {"x": 6-1, "y": 3-1},
            {"x": 5-1, "y": 4-1},
            {"x": 6-1, "y": 4-1}
        ],
        'block down': [
            {"x": 3-1, "y": 5-1},
            {"x": 4-1, "y": 5-1},
            {"x": 3-1, "y": 6-1},
            {"x": 4-1, "y": 6-1}
        ]
    },
    'rooms': {
        'walls_1': [],
        'walls_2': [],
        'walls_3': [],
        'walls_4': [],
        'walls_5': [],
        'walls_6': [],
        'walls_7': [],
        'walls_8': [],
        'walls_9': [],
        'walls_10': [],
        'walls_11': [],
        'walls_12': [],
        'walls_13': [],
        'walls_14': [],
        'walls_15': []
    },

    # ASCII icons
    'player_icon': "\U0001F422",
    # 'eagle_icon': "\U0001F985",
    'walls': "\U000025FC ",
    'gem': "\U0001F48E",
    'heart-dead': '\U00002764',
    'heart-live': '\U0001F496',
    'empty': "  "
}

game_data["rooms"]["walls_1"] = [a for a in game_data['doorways + basics']['basics']]
game_data["rooms"]["walls_2"] = [a for a in game_data['doorways + basics']['basics'] + game_data['doorways + basics']['block top']]
game_data["rooms"]["walls_3"] = [a for a in game_data['doorways + basics']['basics'] + game_data['doorways + basics']['block left']]
game_data["rooms"]["walls_4"] = [a for a in game_data['doorways + basics']['basics'] + game_data['doorways + basics']['block right']]
game_data["rooms"]["walls_5"] = [a for a in game_data['doorways + basics']['basics'] + game_data['doorways + basics']['block down']]
game_data["rooms"]["walls_6"] = [a for a in game_data['doorways + basics']['basics'] + game_data['doorways + basics']['block top'] + game_data['doorways + basics']['block left']]
game_data["rooms"]["walls_7"] = [a for a in game_data['doorways + basics']['basics'] + game_data['doorways + basics']['block top'] + game_data['doorways + basics']['block right']]
game_data["rooms"]["walls_8"] = [a for a in game_data['doorways + basics']['basics'] + game_data['doorways + basics']['block top'] + game_data['doorways + basics']['block down']]
game_data["rooms"]["walls_9"] = [a for a in game_data['doorways + basics']['basics'] + game_data['doorways + basics']['block left'] + game_data['doorways + basics']['block right']]
game_data["rooms"]["walls_10"] = [a for a in game_data['doorways + basics']['basics'] + game_data['doorways + basics']['block left'] + game_data['doorways + basics']['block down']]
game_data["rooms"]["walls_11"] = [a for a in game_data['doorways + basics']['basics'] + game_data['doorways + basics']['block right'] + game_data['doorways + basics']['block down']]
game_data["rooms"]["walls_12"] = [a for a in game_data['doorways + basics']['basics'] + game_data['doorways + basics']['block top'] + game_data['doorways + basics']['block left'] + game_data['doorways + basics']['block right']]
game_data["rooms"]["walls_13"] = [a for a in game_data['doorways + basics']['basics'] + game_data['doorways + basics']['block top'] + game_data['doorways + basics']['block left'] + game_data['doorways + basics']['block down']]
game_data["rooms"]["walls_14"] = [a for a in game_data['doorways + basics']['basics'] + game_data['doorways + basics']['block top'] + game_data['doorways + basics']['block right'] + game_data['doorways + basics']['block down']]
game_data["rooms"]["walls_15"] = [a for a in game_data['doorways + basics']['basics'] + game_data['doorways + basics']['block left'] + game_data['doorways + basics']['block right'] + game_data['doorways + basics']['block down']]

def draw_board(stdscr):
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, -1)

    stdscr.clear()
    room = random.randint(1, 9)
    for y in range(game_data['height']):
        row = ""
        for x in range(game_data['width']):
            if y == 6:
                for hearts in range(5):
                    if game_data['hearts'][hearts] == 'live':
                        row += game_data["heart-live"]
                    else:
                        row += game_data["heart-dead"]
                row += game_data["empty"]
                break
            # Player
            if x == game_data['player']['x'] and y == game_data['player']['y']:
                row += game_data['player_icon']
            # Obstacles
            elif any(o['x'] == x and o['y'] == y for o in game_data['rooms'][f'walls_{room}']):
                row += game_data['walls']
            # Collectibles
            elif any(c['x'] == x and c['y'] == y and not c['collected'] for c in game_data['collectibles']):
                row += game_data['gem']
            else:
                row += game_data['empty']
        stdscr.addstr(y, 0, row, curses.color_pair(1))

    
def check_collectibles():
    for c in game_data['collectibles']:
        if (not c["collected"] and
            game_data['player']["x"] == c["x"] and
            game_data['player']["y"] == c["y"]):

            c["collected"] = True
            game_data['collectibles']['how many'] += 1

def move_player(key):
    x = game_data['player']['x']
    y = game_data['player']['y']

    new_x, new_y = x, y
    key = key.lower()

    if key == "w" and y > 0:
        new_y -= 1
    elif key == "s" and y < game_data['height'] - 1:
        new_y += 1
    elif key == "a" and x > 0:
        new_x -= 1
    elif key == "d" and x < game_data['width'] - 1:
        new_x += 1
    else:
        return  # Invalid key or move off board

    # Check for obstacles
    if any(o['x'] == new_x and o['y'] == new_y for o in game_data['rooms']['walls_1']):
        return

    # Update position and increment score
    game_data['player']['x'] = new_x
    game_data['player']['y'] = new_y
    game_data['player']['score'] += 1

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)

    draw_board(stdscr)

    while True:
        try:
            key = stdscr.getkey()
        except:
            key = None

        if key:
            if key.lower() == "q":
                break

            # put collectables here?

            move_player(key)
            draw_board(stdscr)

curses.wrapper(main)