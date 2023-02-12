# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


import random 

columns = 10
rows = 10
empty_space = '-'
mine = '*'
flag = 'F'

class Minesweeper:
    def __init__ (player, rows=80, columns=24, bombs=50):
        pass

def create_board():  
    board = [[empty_space for j in range (columns)] for i in range(rows)]
    return board 

def add_mines_to_board(board, mine_size):
    for counter in range(0, mine_size + 1):
        random_row = random.randint(0, rows - 1)
        random_column = random.randint(0, columns - 1)
        if board[random_row][random_column] == empty_space:
            board[random_row][random_column] = mine
    return board

def add_flags_to_board(board, flagsize):
    for counter in range(0, flagsize + 1):
        random_row = random.randint(0, rows - 1)
        random_column = random.randint(0, columns - 1)
        if board[random_row][random_column] == empty_space:
            board[random_row][random_column] = flag
    return board

def print_board(board):
    for row in board:
        content_row = ''
        for column in row:
            content_row += f'[{column}]'
        print(f'{content_row}\n')
        