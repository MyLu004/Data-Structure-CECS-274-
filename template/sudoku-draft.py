import random

# Function to generate a complete 3D Sudoku board
def generate_board():
    board = [[[0 for _ in range(9)] for _ in range(9)] for _ in range(9)]
    numbers = [i for i in range(1, 10)]
    random.shuffle(numbers)
    for i in range(9):
        board[0][0][i] = numbers[i]
    for i in range(1, 9):
        for j in range(9):
            board[0][i][j] = board[0][i - 1][(j + 3) % 9]
    for i in range(1, 9):
        for j in range(9):
            for k in range(9):
                board[i][j][k] = board[i - 1][(j + k // 3) % 9][(k + 3) % 9]
    for i in range(3):
        for j in range(3):
            r = random.randint(1, 3) * 3
            c = random.randint(1, 3) * 3
            for k in range(9):
                row = (i * 3 + k // 3) % 9
                col = (j * 3 + k % 3) % 9
                board[row][col], board[r + k // 3][c + k % 3] = board[r + k // 3][c + k % 3], board[row][col]
    return board

# Function to print the 3D Sudoku board
def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- " * 17)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            for k in range(9):
                if k % 3 == 0 and k != 0:
                    print(" ", end="")
                print(board[i][j][k], end=" ")
            print()
        if i != 8:
            print()

# Function to check if a value is valid in a given cell
def is_valid(board, x, y, z, value):
    for i in range(9):
        if board[x][i][z] == value or board[i][y][z] == value or board[x][y][i] == value:
            return False
    sub_x = (x // 3) * 3
    sub_y = (y // 3) * 3
    sub_z = (z // 3) * 3
    for i in range(sub_x, sub_x + 3):
        for j in range(sub_y, sub_y + 3):
            for k in range(sub_z, sub_z + 3):
                if board[i][j][k] == value:
                    return False
    return True

# Function to solve the 3D Sudoku board using backtracking
def solve_board(board):
    for x in range(9):
        for y in range(9):
            for z in range(9):
                if board[x][y][z] == 0:
                    for k in range(1, 10):
                        if is_valid(board, x, y, z, k):
                            board[x][y][z] = k
                            if solve_board(board):
                                return True
                            board[x][y][z] = 0
