#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""Module model: the cellular automaton modelizing a pandemia.
"""


import random

def create_board(width, height):
    board = []
    for y in range(height):
        board.append([None] * width)
    random_board(board, width, height)
    return board

def random_state(immunePercent):
    val = random.randrange(1000)
    if val < immunePercent*10:
        return "immune"
    else:
        return "healthy"

def random_board(board, width, height, immunePercent=20):
    for l in range(height):
        for c in range(width):
            board[l][c] = random_state(immunePercent)


def healthy_board(board, width, height):
    for l in range(height):
        for c in range(width):
            board[l][c] = "healthy"


def print_board(board, width, height, symbols):
    """ show the board in text mode on the standard output. """
    for l in range(height):
        line = ""
        for c in range(width):
            this_cell = board[l][c]
            line = line + symbols[this_cell] + " "
        print(line)
    print()

def compute_stats(board, width, height, mortality):
    """ gives the percentage of the population killed by the pandemia """
    count= 0 # number of cells that were touched by the pandemia
    for l in range(height):
        for c in range(width):
            if board[l][c] == "touched":
                count = count + 1
    return count * mortality / (height*width)
        

def board_copy (board, width, height):
    """ Returns a "deep" copy of the board. """
    new_board = []
    for l in range(height):
        new_board.append(board[l].copy())
    return new_board

def neighbors(board, width, height, l, c):
    """ Returns a list of 8-neighbors (less on the borders)."""
    L = []
    for dl in range(- 1, 2):
        for dc in range(- 1, 2):
            if (0 <= c + dc < width and 0 <= l + dl < height):
                L.append(board[l + dl][c + dc])
    return L

def get_cell(board, l, c):
    return board[l][c]
    
def set_cell(board, l, c, state):
    board[l][c] = state

def compute_step(board, width, height):
    """ Applies one step to each cell of the board.

    Returns True if at least one cell changed state.
    """
    copy = board_copy(board, width, height)
    changed = False
    for l in range(height):
        for c in range(width):
            neig = neighbors(copy, width, height, l, c)
            new_cell, chgd = next_state(board[l][c], neig)

            if chgd:
                board[l][c] = new_cell
                changed = True
    return changed

    
def next_state(initialState, neighbors):
    """Applies one step of evolution.

    Returns state, bool where
    state is the new state and
    bool is True iff the state changed.
    """
    if initialState == "sick":
        return "touched", True
    elif initialState == "healthy":
        for i in neighbors:
            if i == "sick":
                return "sick", True
    return initialState, False

if __name__ == '__main__':

    from time import sleep

    symbols = {"sick":"#", "healthy":"+", "touched":".", "immune":" "}
    w = 10
    h = 5
    pandemia = create_board(w, h)
    random_board(pandemia, w, h, 50)
    set_cell(pandemia, 2, 5, 'sick')
    set_cell(pandemia, 1, 1, 'sick')
    set_cell(pandemia, 4, 9, 'sick')

    print_board(pandemia, w, h, symbols)
    changed = True

    while(changed):
        changed = compute_step(pandemia, w, h)
        sleep(1)
        print_board(pandemia, w, h, symbols)

    print("Finished!")
        
