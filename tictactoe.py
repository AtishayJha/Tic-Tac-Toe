"""
Tic Tac Toe Player
"""
import sys
from copy import deepcopy
sys.setrecursionlimit(255168)


X = "X"
O = "O"
EMPTY = None
playerlist = [X, O]


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
    result = X
    movecount = [board[0].count(X)+board[1].count(X)+board[2].count(X), 
    board[0].count(O)+board[1].count(O)+board[2].count(O)]
    if movecount[0]>movecount[1]:
        result = O
    return result
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actionlist = []
    for i in range(3):
        for j in range(3):
            if board[i][j]==None:
                actionlist.append([i, j])
    return actionlist
def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    resultboard = deepcopy(board)
    if action is not None:
        if type(action)!=list:
            action = list(action)
        if board[action[0]][action[1]]==X or board[action[0]][action[1]]==O:
            raise ValueError("Invalid action")
        else:
            resultboard[action[0]][action[1]]=player(resultboard)  
    return resultboard
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0]==board[i][1] and board[i][1]==board[i][2] and board[i][0]!=EMPTY:
            return board[i][0]
        elif board[0][i]==board[1][i] and board[1][i]==board[2][i] and board[0][i]!=EMPTY:
            return board[0][i]
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[0][0]!=EMPTY:
        return board[0][0]
    if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[0][2]!=EMPTY:
        return board[0][2]
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    gamefinished=winner(board)
    if gamefinished is None:
        if None not in board[0]+board[1]+board[2]:
            return True
        else:
            return False
    elif gamefinished==X or gamefinished==O:
        return True
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    returnvalue = 0
    if winner(board)==X:
        returnvalue = 1
    elif winner(board)==O:
        returnvalue = -1

    return returnvalue
def scoreof(board, starting):
    '''
    A helper function to find the best possible score on a given board.
    It gives as output the best possible score and and all the possible
    scores which can be attained
    '''
    Newboard = deepcopy(board)
    optimalactionlist = []
    if terminal(Newboard):
        return [utility(Newboard), optimalactionlist]
    if player(Newboard)==X:
        v = -float('inf')
        for action in actions(board):
            best = scoreof(result(Newboard, action), 0)[0]
            v = max(v, best)
            if starting==1:
                optimalactionlist.append(best)
        return [v, optimalactionlist]
    else:
        v = float('inf')
        for action in actions(board):
            best = scoreof(result(Newboard, action), 0)[0]
            v = min(v, best)
            if starting==1:
                optimalactionlist.append(best)
        return [v, optimalactionlist]
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """  
    Newboard = deepcopy(board)
    if Newboard==initial_state():
        '''
        In order to decrease the total time taken to take the decision
        when the board is completely empty (as this script is not using
        alpha-beta pruning), the list of score in (only) the particular
        case is already provided to the script
        '''
        optimalactionlist = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    else:
        optimalactionlist = deepcopy(scoreof(Newboard, 1)[1])
    Newboard = deepcopy(board)
    if player(Newboard)==X:
        return actions(Newboard)[optimalactionlist.index(max(optimalactionlist))]
    else:
        return actions(Newboard)[optimalactionlist.index(min(optimalactionlist))]
                
                
                
                
                
                
                
                
                
