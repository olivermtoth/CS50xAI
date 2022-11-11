"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

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
    for i in range(3):
      for j in range(3):
        if board[i][j] == EMPTY:
          actions.append((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY:
      raise Exception("ILLEGEAL MOVE")
    playboard = deepcopy(board)
    playboard[action[0]][action[1]] = player(board)
    return playboard
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0] :
        return board[1][1]
    
    for row in board:
      if row[0] == row[1] == row[3]:
        return row[0]
    
    for x in range(3):
      if board[0][x] == board[1][x] == board[2][x]:
        return board[0][x]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None and EMPTY not in board:
      return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    return 1 if winner(board) == X else -1 if winner(board) == O else 0

def max_value(board):
  if terminal(board):
    return utility(board)
  value = -1*math.inf
  for action in actions(board):
    value = max(value, min_value(result(board, action)))
  return value

def min_value(board):
  if terminal(board):
    return utility(board)
  value = math.inf
  for action in actions(board):
    value = min(value, max_value(result(board, action)))
  return value

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
      return None
    optimal_action = None
    value = -1*math.inf
    for action in action(board):
      current_value = max_value(result(board, action))
      if current_value > value:
        optimal_action = action
        value = current_value
    return optimal_action
    
