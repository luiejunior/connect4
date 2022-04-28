import numpy as np
import pygame

def empty_board(height, width):
    return np.zeros((height, width))

def enter_move(board, player, row, col):
    return board[row][col] = player

def check_win(board, player, row, col, connect_length):
    # row and col represent the row and column position respectively of the last move

    length = 1
    consecutive = True
    index_row = row
    index_col = col - 1
    while consecutive:
        if index_col < 0:
            consecutive = False
        elif board[index_row][index_col] == player:
            length += 1
            index_col -= 1
        else:
            consecutive = False
    consecutive = True
    index_row = row
    index_col = col + 1
    while consecutive:
        if index_col >= width:
            consecutive = False
        elif board[index_row][index_col] == player:
            length += 1
            index_col += 1
        else:
            consecutive = False
    horizontal = length >= connect_length

    length = 1
    consecutive = True
    index_row = row - 1
    index_col = col
    while consecutive:
        if index_row < 0:
            consecutive = False
        elif board[index_row][index_col] == player:
            length += 1
            index_row -= 1
        else:
            consecutive = False
    consecutive = True
    index_row = row + 1
    index_col = col
    while consecutive:
        if index_row >= height:
            consecutive = False
        elif board[index_row][index_col] == player:
            length += 1
            index_row += 1
        else:
            consecutive = False
    vertical = length >= connect_length

    length = 1
    consecutive = True
    index_row = row - 1
    index_col = col - 1
    while consecutive:
        if index_row < 0 or index_col < 0:
            consecutive = False
        elif board[index_row][index_col] == player:
            length += 1
            index_row -= 1
            index_col -= 1
        else:
            consecutive = False
    consecutive = True
    index_row = row + 1
    index_col = col + 1
    while consecutive:
        if index_row >= height or index_col >= width:
            consecutive = False
        elif board[index_row][index_col] == player:
            length += 1
            index_row += 1
            index_col += 1
        else:
            consecutive = False
    main_diagonal = length >= connect_length

    length = 1
    consecutive = True
    index_row = row - 1
    index_col = col + 1
    while consecutive:
        if index_row < 0 or index_col >= width:
            consecutive = False
        elif board[index_row][index_col] == player:
            length += 1
            index_row -= 1
            index_col += 1
        else:
            consecutive = False
    consecutive = True
    index_row = row + 1
    index_col = col - 1
    while consecutive:
        if index_row >= height or index_col < 0:
            consecutive = False
        elif board[index_row][index_col] == player:
            length += 1
            index_row += 1
            index_col -= 1
        else:
            consecutive = False
    antidiagonal = length >= connect_length

    return horizontal or vertical or main_diagonal or antidiagonal

height = 6
width = 7
connect_length = 4

board = empty_board(height, width)
filled = [height] * width
finish = False
turn = 1

while not finish:

    if turn % 2 == 1:
        player = 1
    else:
        player = 2

    board = enter_move(board, player, row, col)
    if check_win(board, player, row, col, connect_length):
        finish = True
