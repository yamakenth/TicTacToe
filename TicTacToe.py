# create an empty grid 
grid = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]
# keep track of number of turns
turn = 0
# keep track of played moves 
played_moves = []


# print current grid with borders 
def print_grid(current_grid):
    for row in grid:
        new_row = "|"
        for col in row:
            new_row += ( " " + col + " |")
        print(new_row)

# check if input is invalid 
def is_invalid_input(current_move):
    is_invalid = False
    if not current_move.isnumeric():
        is_invalid = True
    elif (int(current_move) < 1) or (int(current_move) > 9):
        is_invalid = True
    elif int(current_move) in played_moves:
        is_invalid = True
    return is_invalid

# update grid and return new grid 
def update_grid(user_input, mark):
    num = int(user_input)
    row = int((num - 1) / 3)
    col = (num - 1) % 3
    grid[row][col] = mark
    return grid


# run program 
# greet user/s
print("Hello, this is a Tic-tac-toe game. \nType \"q\" if you'd like to quit the game.")
# print initial grid 
print_grid(grid)
# while (no winner) or (grid is not full) or (user wants to quit) prompt user for input 
is_win = False
is_quit = False
while (is_win == False) and (len(played_moves) != 9) and (is_quit == False):
    turn += 1
    player = ""
    mark = ""

    if turn % 2 != 0:
        player = 1
        mark = "O"
    else:
        player = 2
        mark = "X"
    
    while True:
        current_move = input(
            "Turn {}: Player {}, place {} in an emtpy space. ".format(turn, player, mark)
            + "Type a number between 1 and 9.  "
        )
        if (current_move == "q"):
            is_quit = True
            break 
        elif is_invalid_input(current_move):
            print("Sorry, your input is invalid. Please type a number between 1 and 9.")
        else:
            played_moves.append(int(current_move))
            break


    # new_grid = update_grid(current_move, mark)
    # print_grid(new_grid)

# print message (if grid is full or winner is determined)
print("No more grids to play. The game is a tie.")
