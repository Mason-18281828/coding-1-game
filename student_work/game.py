# The goals for this phase include:
# - Pick out some icons for your game
# - Establish a starting position for each icon
# - Pick a size for your playing space
# - Print your playing space with starting position of each icon

# To make this work, you may have to type this into the terminal --> pip install curses
import curses

game_data = {
    'width': 6,
    'height': 7,
    'player': {"x": 3, "y": 3, "score": 0},
    # 'eagle_pos': {"x": 4, "y": 4},
    'collectibles': [
        {"x": 3, "y": 1, "collected": False},
    ],
    'hearts': ['live', 'live', 'live', 'live', 'live'],
    'rooms': {
        'walls_1': [
            {"x": 1, "y": 1},
            {"x": 1, "y": 2},
            {"x": 1, "y": 5},
            {"x": 1, "y": 6},
            {"x": 2, "y": 1},
            {"x": 2, "y": 2},
            {"x": 2, "y": 5},
            {"x": 2, "y": 6},
            {"x": 5, "y": 1},
            {"x": 5, "y": 2},
            {"x": 5, "y": 5},
            {"x": 5, "y": 6},
            {"x": 6, "y": 1},
            {"x": 6, "y": 2},
            {"x": 6, "y": 5},
            {"x": 6, "y": 6},
        ]
    },

    # ASCII icons
    'player': "\U0001F422",
    # 'eagle_icon': "\U0001F985",
    'walls': "\U000025F6",
    'gem': "\U0001F48E",
    'heart-dead': '\U00002764',
    'heart-live': '\U0001F496',
    'empty': "  "
}

def draw_board(stdscr):
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, -1)

    stdscr.clear()
    room = 1
    for y in range(game_data['height']):
        row = ""
        for x in range(game_data['width']):
            if y == 6:
                for hearts in range(6):
                    if game_data['hearts'][hearts] == 'live':
                        row += game_data["heart-live"]
                    else:
                        row += game_data["heart-dead"]
                row += game_data["empty"]
                break
            # Player
            if x == game_data['player']['x'] and y == game_data['player']['y']:
                row += game_data['player']
            # Obstacles
            elif any(o['x'] == x and o['y'] == y for o in game_data['rooms'][f'walls_{room}']):
                row += game_data['walls']
            # Collectibles
            elif any(c['x'] == x and c['y'] == y and not c['collected'] for c in game_data['collectibles']):
                row += game_data['gem']
            else:
                row += game_data['empty']
        stdscr.addstr(y, 0, row, curses.color_pair(1))

    stdscr.refresh()
    stdscr.getkey()  # pause so player can see board

curses.wrapper(draw_board)
