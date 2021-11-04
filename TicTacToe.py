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
# print message
def determine_winner_or_tie(current_player):
    # check if tie 
    if (len(played_moves) == 9):
        print("No more grids to play. The game is a tie.")
        return True
    
    # check if win 
    horizontal_win_bool = is_horizontal_win()
    vertical_win_bool = is_vertical_win()
    diagonal_win_bool = is_diagonal_win()
    if (horizontal_win_bool or vertical_win_bool or diagonal_win_bool):
        print("Player {} won!".format(current_player))
        return True

    # if at least one condition is met then return true 
    return False

# check for horizontal win 
# print message and return is_win boolean 
def is_horizontal_win():
    for row in grid:
        if is_same_element_in_list(row):
            return True 
    return False

# check for veritcal win 
# print message and return is_win boolean 
def is_vertical_win():
    for i in range(3):
        col = []
        for j in range(3):
            col.append(grid[j][i])
        if is_same_element_in_list(col):
            return True 
    return False

# check for diagonal win 
# print message and return is_win boolean 
def is_diagonal_win():
    diag1 = [grid[0][0], grid[1][1], grid[2][2]]
    diag2 = [grid[0][2], grid[1][1], grid[2][0]]
    is_diag1_win = is_same_element_in_list(diag1)
    is_diag2_win = is_same_element_in_list(diag2)
    return is_diag1_win or is_diag2_win

# return true if element in list is same 
# also check if first grid is not empty 
def is_same_element_in_list(lst):
    if (lst[0] != "-") and (all(element == lst[0] for element in lst)):
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
