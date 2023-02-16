import random

# Variables #
shadow_space = ' '
mines = '*'
flag = 'F'
rows = 5
columns = 5
mine_size = 20
flag_size = 5


# Minesweeper class contains all of the functions
# partaining to initialisation, adding mines and
# flags to the board
class Minesweeper:  # 15/02
    def __init__(self, rows=5, columns=5, mines=10):
        self.rows = rows
        self.flags_found = 0
        self.columns = columns
        self.mines = mines
        self.board = [[flag for j in range(columns)] for i in range(rows)]
        self.mask = [[shadow_space for j
                      in range(columns)] for i in range(rows)]
        self.end_game = False
        self.add_mines_to_board()

    def add_mines_to_board(self):
        for counter in range(0, mine_size + 1):
            random_row = random.randint(0, rows - 1)
            random_column = random.randint(0, columns - 1)
            if self.board[random_row][random_column] == flag:
                self.board[random_row][random_column] = mines

# print_board and play functions display board only if the user finds mines
# instead of flag. Also, the win/ loss conditions are implemented within
# "play" function

    def print_board(self, board):
        for row in board:
            content_row = ''
            for column in row:
                content_row += f'[{column}]'
            print(f'{content_row}\n')

    def play(self, row, column):                         # 15/02
        if self.end_game:
            return
        if self.board[row][column] == '*':
            self.end_game = True
            print("Game Over")
            self.print_board(self.board)
        else:
            self.mask[row][column] = flag
            self.print_board(self.mask)
            self.flags_found += 1
            if self.flags_found == flag_size:
                self.end_game = True
                print("You Win!")

# Welcome message is displayed to users when programme is re/ started


if __name__ == "__main__":     # 15/02
    username = input("Enter username: \n")

    print("Hello " + username, ", welcome to Minesweeper! \n")
    print("----------------------------------------------- \n")
    print("Before you get started, there are a few things you must know: \n")
    print("In order to win, you must accurately find the hidden flags via \n")
    print("the coordinates system. \n")
    print("If you find a flag, you may continue inputting coordinates. \n")
    print("If you find 5, you win! \n")
    print("If you find a mine, however, you lose! \n")
    print("Goodluck! \n")
    print("----------------------------------------------- \n")

    game = Minesweeper()
    game.print_board(game.mask)

# While loop ensures that users input row/ column
# as long as mines are not found.
# The loop also ensures that the correct data has been inputted

    while game.end_game is False:
        try:
            row = int(input(f"Enter row 0 - {rows - 1}: "))
            while row not in range(rows):
                print(f"{row} is not a valid option")
                row = int(input("Enter row: "))
            column = int(input(f"Enter column 0 - {columns - 1}: "))
            while column not in range(columns):
                print(f"{column} is not a valid option")
                column = int(input("Enter column: "))
            game.play(row, column)
        except ValueError:
            print("Invalid input")

# Restart option presented via loop at the end of the game.

play_again = input("Do you want to restart? Yes or No\n")

if play_again == "Yes":
    exec(open("./run.py").read())
else:
    exit()