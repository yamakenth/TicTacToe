# creating an empty grid 
grid = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

# print current grid with borders 
def print_grid(current_grid):
    for row in grid:
        new_row = "|"
        for col in row:
            new_row += ( " " + col + " |")
        print(new_row)

# update grid and return new grid 
def update_grid(user_input):
    num = int(user_input)
    row = int((num - 1) / 3)
    col = (num - 1) % 3
    grid[row][col] = "O"
    return grid


# run program 
# greet user/s
print("Hello, this is a Tic-tac-toe game. \nType \"q\" if you'd like to quit the game.")
# print initial grid 
print_grid(grid)
# while (no winner) or (grid is not full) or (user wants to quit)
    # prompt user1 for input 
    # prompt user2 for input 
is_win = False
is_no_space = False
is_quit = False
while (is_win == False) and (is_no_space == False) and (is_quit == False):
    p1_move = input("Player 1, place \"O\" in an emtpy space. Type \"1\" to \"9\".  ")
    if (p1_move == "q"):
        is_quit = True
        break
    new_grid = update_grid(p1_move)
    print_grid(new_grid)

# print message (if grid is full or winner is determined)
