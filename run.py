# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


import random 

#Board features 
shadow_space = ' '
mines = '*'
flag = 'F'
rows=5
columns=5
mine_size = 20
flag_size = 5


class Minesweeper:

    def __init__(self, rows=5, columns=5, mines=10):  #15/02
        self.rows = rows
        self.flags_found = 0
        self.columns = columns
        self.mines = mines
        self.board = [[flag for j in range(columns)] for i in range(rows)]
        self.mask = [[shadow_space for j in range(columns)] for i in range(rows)]
        self.end_game = False
        self.add_mines_to_board()

    def add_mines_to_board(self):
        for counter in range(0, mine_size + 1):
            random_row = random.randint(0, rows - 1)
            random_column = random.randint(0, columns - 1)
            if self.board[random_row][random_column] == flag:
                self.board[random_row][random_column] = mines

    def print_board(self, board):
        for row in board:
            content_row = ''
            for column in row:
                content_row += f'[{column}]'
            print(f'{content_row}\n')

    def play(self, row, column):                         #15/02
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
        
if __name__ == "__main__":                            #15/02
    game = Minesweeper()
    game.print_board(game.mask)
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
