def print_board(board):
    print("-"*37)
    for i, row in enumerate(board):
        print(("|" + " {}   {}   {} |"*3).format(*[x if x != 0 else " " for x in row]))
        if i == 8:
            print("-"*37)
        elif i % 3 == 2:
            print("|" + "---,"*8 + "---|")
        else:
            print("|" + "   ,"*8 + "   |")


def is_valid_move(grid, row, col, number):
    for i in range(9):
        if grid[row][i] == number:
            return False
    for j in range(9):
        if grid[j][col] == number:
            return False

    corner_row = row - row % 3
    corner_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if grid[corner_row + i][corner_col + j] == number:
                return False

    return True


def solve(grid, row, col):
    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0
    if grid[row][col] > 0:
        return solve(grid, row, col + 1)

    for num in range(1, 10): # 1..9
        if is_valid_move(grid, row, col, num):

            grid[row][col] = num

            if solve(grid, row, col + 1):
                return True

        grid[row][col] = 0

    return False

grid = [
        [4, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 9, 8],
        [3, 0, 0, 0, 8, 2, 4, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 8, 0],
        [9, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 6, 7, 0],
        [0, 5, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 9, 0, 7],
        [6, 4, 0, 3, 0, 0, 0, 0, 0],]

print("ORG:")
print_board(grid)
print()
print("Solving...")
if solve(grid, 0, 0):
    print_board(grid)
else:
    print("No Solution for this grid")
