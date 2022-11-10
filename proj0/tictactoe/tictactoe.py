"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x, o = 0, 0
    for row in board:
      for cell in row:
        if cell == X:
          x += 1
        elif cell == O:
            o += 1
    return X if x == o else O
  

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    action_board = [[EMPTY, EMPTY, EMPTY],
                    [EMPTY, EMPTY, EMPTY],
                    [EMPTY, EMPTY, EMPTY]]
    for i in range(3):
      for j in range(3):
        if board[i][j] == EMPTY:
          action_board[i][j] = player
          actions.append(action_board)
          action_board[i][j] = EMPTY
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    for i in range(3):
      for j in range(3):
        if action[i][j] != EMPTY:
          board[i][j] = action[i][j]
          return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0] :
        return board[1][1]
    
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
