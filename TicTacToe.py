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



# run program 
# greet user/s
print("Hello, this is a Tic-tac-toe game.")
# print initial grid 
print_grid(grid)
# while (no winner) or (grid is not full) or (user wants to quit)
    # prompt user1 for input 
    # prompt user2 for input 
# print message (if grid is full or winner is determined)
