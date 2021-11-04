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

# update grid
def update_grid(user_input, mark):
    row = int((user_input - 1) / 3)
    col = (user_input - 1) % 3
    grid[row][col] = mark

# determine winner or tie 
# return boolean is_end
# print if winner or tie 
def determine_winner_or_tie(current_player):
    tie_bool = is_tie(current_player)
    horizontal_win_bool = is_horizontal_win(current_player)
    vertical_win_bool = is_vertical_win(current_player)
    diagonal_win_bool = is_diagonal_win(current_player)
    # if at least one condition is met then return true 
    return horizontal_win_bool or tie_bool or vertical_win_bool or diagonal_win_bool

# check for tie 
# print message and return is_end boolean 
def is_tie(current_player):
    if (len(played_moves) == 9):
        print("No more grids to play. The game is a tie.")
        return True

# check for horizontal win 
# print message and return is_end boolean 
def is_horizontal_win(current_player):
    for row in grid:
        if (row[0] != "-") and (all(element == row[0] for element in row)):
            print("Player {} won!".format(current_player))
            return True
    return False

# check for veritcal win 
# print message and return is_end boolean 
def is_vertical_win(current_player):
    for i in range(3):
        col = []
        for j in range(3):
            col.append(grid[j][i])
        if (col[0] != "-") and (all(element == col[0] for element in col)):
            print("Player {} won!".format(current_player))
            return True
    return False

# check for diagonal win 
# print message and return is_end boolean 
def is_diagonal_win(current_player):
    diag1 = [grid[0][0], grid[1][1], grid[2][2]]
    diag2 = [grid[0][2], grid[1][1], grid[2][0]]
    if (diag1[0] != "-") and (all(element == diag1[0] for element in diag1)):
        print("Player {} won!".format(current_player))
        return True
    if (diag2[0] != "-") and (all(element == diag2[0] for element in diag2)):
        print("Player {} won!".format(current_player))
        return True
    return False


# run program 

# greet user/s
print("Hello, this is a Tic-tac-toe game. \nType \"q\" if you'd like to quit the game.")
# print initial grid 
print_grid(grid)

# while (no winner) or (grid is not full) prompt user for input 
is_end = False
while not is_end:
    # increment number of turns 
    # determine which player is playing 
    turn += 1
    player = ""
    mark = ""
    if turn % 2 != 0:
        player = 1
        mark = "O"
    else:
        player = 2
        mark = "X"
    
    # while user input is invalid, keep asking for input 
    # if input = "q" then quit program 
    while True:
        current_move = input(
            "Turn {}: Player {}, place {} in an emtpy space. ".format(turn, player, mark)
            + "Type a number between 1 and 9.  "
        )
        if (current_move == "q"):
            exit() 
        elif is_invalid_input(current_move):
            print("Sorry, your input is invalid. Please type a number between 1 and 9.")
        else:            
            break
    
    # add current move to list of moves that are played 
    played_moves.append(int(current_move))
    
    # update and print new grid 
    update_grid(int(current_move), mark)
    print_grid(grid)

    # check if game should continue 
    # print message if end of game 
    is_end = determine_winner_or_tie(player)

# print message at the end 
print("Good game!")
