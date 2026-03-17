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
    'height': 8,
    'player': {"x": 3, "y": 3, "score": 0},
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
    'room_#': 1,
    'portal_data': {
        'access': False,
        'location': (2, 3)
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

def update_game_data():
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
update_game_data()

def draw_board(stdscr, room):
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, -1)

    stdscr.clear()
   
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
            if y == 7:
               row += ("Items Collected:" + " " + str(game_data['collectibles'][0]['how many']))
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
            game_data['player']["x"] == game_data["collectibles"]["x"] and
            game_data['player']["y"] == game_data["collectibles"]["y"]):

            c["collected"] = True
            game_data['collectibles']['how many'] += 1

def move_player(key):
    x = game_data['player']['x']
    y = game_data['player']['y']

    new_x, new_y = x, y
    key = key.lower()

    if key == "w":
        new_y -= 1
    elif key == "s":
        new_y += 1
    elif key == "a":
        new_x -= 1
    elif key == "d":
        new_x += 1
    # else:
    #     return  # Invalid key or move off board

    if x not in range(0, 6) or y not in range(0, 6):
                if x > 5:
                    x = 0
                elif x < 0:
                    x = 5
                elif y > 5:
                    y = 0
                elif y < 0:
                    y = 5
               
                while True:
                    game_data['room_#'] = random.randint(1, 15)
                    if (game_data['player']['x'] in range(3, 5) and game_data['player']['y'] == 0) and game_data['room_#'] in [2, 6, 7, 8, 12, 13, 14]:
                        continue
                    elif (game_data['player']['x'] in range(3, 5) and game_data['player']['y'] == 5) and game_data['room_#'] in [5, 8, 10, 11, 13, 14, 15]:
                        continue
                    elif (game_data['player']['y'] in range(3, 5) and game_data['player']['x'] == 0) and game_data['room_#'] in [3, 6, 9, 10, 12, 13, 15]:
                        continue
                    elif (game_data['player']['y'] in range(3, 5) and game_data['player']['x'] == 5) and game_data['room_#'] in [4, 7, 9, 11, 12, 14, 15]:
                        continue
                    else:
                        break

    # Check for obstacles
    if any(o['x'] == new_x and o['y'] == new_y for o in game_data['rooms'][f'walls_{game_data['room_#']}']):
        return

   
    # Update position and increment score
    game_data['player']['x'] = new_x
    game_data['player']['y'] = new_y
    game_data['player']['score'] += 1

def spawn_gem():
    while True:
        x = random.randint(0, game_data['width'] - 1)
        y = random.randint(0, game_data['height'] - 1)

        if (x == game_data['player']["x"] and y == game_data['player']["y"]):
            continue

        if any(o["x"] == x and o["y"] == y for o in game_data['obstacles'][f'room{game_data['room_#']}']):
            continue

        # Valid location found
        game_data['collectibles'][0]['x'] = x
        game_data['collectibles'][0]['y'] = y
        game_data['collectibles'][0]['collected'] = False
        game_data['collectibles'][0]['how many'] += 1
        break

def main(stdscr):
    global game_data
    curses.curs_set(0)
    stdscr.nodelay(True)

    draw_board(stdscr, game_data['room_#'])

    while True:
        try:
            key = stdscr.getkey()
        except:
            key = None

        if key:
            if key.lower() == "q":
                break

            moved = move_player(key)
            if moved:
                check_collectibles()
            draw_board(stdscr, game_data['room_#'])


curses.wrapper(main)