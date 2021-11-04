# creates an empty grid for beginning of game
grid = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]
# keeps track of number of turns
turn = 0
# keeps track of played moves, list that holds 1-9
played_moves = []


# prints current grid with borders 
# takes in current_grid to print 
# prints formatted grid 
def print_grid(current_grid):
    for row in grid:
        new_row = "|"
        for col in row:
            new_row += ( " " + col + " |")
        print(new_row)

# checks if input is invalid 
# takes in current_move (user input) as str 
# returns True if input is INVALID, false otherwise
def is_invalid_input(current_move):
    is_invalid = False
    # input is not number 
    if not current_move.isnumeric():
        is_invalid = True
    # input is outside of range 
    elif (int(current_move) < 1) or (int(current_move) > 9):
        is_invalid = True
    # input move has already been played 
    elif int(current_move) in played_moves:
        is_invalid = True
    return is_invalid

# updates grid with user input 
# takes in user_input as int, mark (X/O)
# updates grid, no return 
def update_grid(user_input, mark):
    row = int((user_input - 1) / 3)
    col = (user_input - 1) % 3
    grid[row][col] = mark

# determines a winner or if game is a tie 
# takes in current_player
# prints message (tie/win)
# returns boolean where True = end of game, False = continue playing 
def determine_winner_or_tie(current_player):
    # checks if tie 
    if len(played_moves) == 9:
        print("No more grids to play. The game is a tie.")
        return True
    
    # checks if win 
    horizontal_win_bool = is_horizontal_win()
    vertical_win_bool = is_vertical_win()
    diagonal_win_bool = is_diagonal_win()
    if horizontal_win_bool or vertical_win_bool or diagonal_win_bool:
        print("Player {} won!".format(current_player))
        return True

    # returns False if no conditions are met 
    return False

# checks for horizontal win 
# returns True if win, False otherwise
def is_horizontal_win():
    for row in grid:
        if is_same_element_in_list(row):
            return True 
    return False

# checks for veritcal win 
# returns True if win, False otherwise
def is_vertical_win():
    for i in range(3):
        col = []
        for j in range(3):
            col.append(grid[j][i])
        if is_same_element_in_list(col):
            return True 
    return False

# checks for diagonal win 
# returns True if win, False otherwise
def is_diagonal_win():
    diag1 = [grid[0][0], grid[1][1], grid[2][2]]
    diag2 = [grid[0][2], grid[1][1], grid[2][0]]
    is_diag1_win = is_same_element_in_list(diag1)
    is_diag2_win = is_same_element_in_list(diag2)
    return is_diag1_win or is_diag2_win

# checks if elements in a list are the same 
# also checks if first grid is not empty 
# returns True if element in list is same, False otherwise 
def is_same_element_in_list(lst):
    if (lst[0] != "-") and (all(element == lst[0] for element in lst)):
        return True
    return False


# runs program 

# greets user
print("Hello, this is a Tic-tac-toe game. \nType \"q\" if you'd like to quit the game.")
# prints initial grid 
print_grid(grid)

# while (no winner) or (grid is not full) prompts user for input 
is_end = False
while not is_end:
    # increments number of turns 
    # determines which player is playing 
    turn += 1
    player = ""
    mark = ""
    if turn % 2 != 0:
        player = 1
        mark = "O"
    else:
        player = 2
        mark = "X"
    
    # while user input is invalid, keeps asking for input 
    # if input = "q" then quits program 
    while True:
        current_move = input(
            "Turn {}: Player {}, place {} in an emtpy space. ".format(turn, player, mark)
            + "Type a number between 1 and 9.  "
        )
        if current_move == "q":
            exit() 
        elif is_invalid_input(current_move):
            print("Sorry, your input is invalid. Please type a number between 1 and 9.")
        else:            
            break
    
    # adds current move to list of moves that are played 
    played_moves.append(int(current_move))
    
    # updates and print new grid 
    update_grid(int(current_move), mark)
    print_grid(grid)

    # checks if game should continue 
    # prints message if end of game 
    is_end = determine_winner_or_tie(player)

# prints message at the end 
print("Good game!")
