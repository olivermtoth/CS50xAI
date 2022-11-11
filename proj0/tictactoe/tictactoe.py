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
    actions = set()
    for i in range(3):
      for j in range(3):
        if board[i][j] == None:
          actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i = action[0]
    j = action[1]
    if board[i][j] != EMPTY:
      raise Exception("ILLEGAL MOVE")
    playboard = deepcopy(board)
    playboard[i][j] = player(board)
    return playboard
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for player in [X,O]:

      for row in board:
        if row == [player]*3:
          return player
      
      for i in range(3):
        column = [board[x][i] for x in range(3)]
        if column == [player]*3:
          return player
    
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0] :
      return board[1][1]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
      return True
    
    for row in board:
      for cell in row:
        if EMPTY in row:
          return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w == X:
      return 1
    elif w == O:
      return -1
    else:
      return 0

def max_value(board):
  optimal_action = ()
  if terminal(board):
    return utility(board), optimal_action
  value = -1*math.inf
  for action in actions(board):
    # value = max(value, min_value(result(board, action)))
    current_value = min_value(result(board, action))[0]
    if current_value > value:
      value = current_value
      optimal_action = action
  return value, optimal_action

def min_value(board):
  optimal_action = ()
  if terminal(board):
    return utility(board), optimal_action
  value = math.inf
  for action in actions(board):
    # value = min(value, max_value(result(board, action)))
    current_value = max_value(result(board, action))[0]
    if current_value < value:
      value = current_value
      optimal_action = action
  return value, optimal_action

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
      return None

    current_player = player(board)
    if current_player == X:
      return max_value(board)[1]
    else:
      return min_value(board)[1] 
    
