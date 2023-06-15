import math
import copy

X = "X"
O = "O"
EMPTY = None

oboard = [[EMPTY for j in range(3)] for i in range(3)]

choice = input('X or O? ')
if choice == 'X':
    ai = 'O'
else:
    ai = 'X'


def player(board):

    if terminal(board) == False:
        count = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] in [X, O]:
                    count += 1
        if count % 2 == 0:
            return X
        else: 
            return O
    else:
        return 404


def actions(board):

    action = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action.append([i, j])
    if action:
        return action
    else: 
        return 404


def result(board, action):

    boardcopy = copy.deepcopy(board)
    if (terminal(boardcopy) == False) and (action[0] in range(3)) and (action[1] in range(3)):
        for i in range(3):
            for j in range(3):
                if i == action[0] and j == action[1]:
                    boardcopy[i][j] = player(boardcopy)
        return boardcopy
    else:
        raise Exception('Invalid')

def winner(board):

    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == X:
            return X
        elif board[0][i] == board[1][i] == board[2][i] == O:
            return O
        
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == X:
            return X
        elif board[i][0] == board[i][1] == board[i][2] == O:
            return O
        
    if board[1][1] == board[0][0] == board[2][2] == X:
        return X
    if board[1][1] == board [0][2] == board[2][0] == X:  
        return X 
    if board[1][1] == board[0][0] == board[2][2] == O:
        return O
    if board[1][1] == board [0][2] == board[2][0] == O:  
        return O
    
    return None


def terminal(board):
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                count += 1
    if (count == 0) or (winner(board) != None):
        return True
    else:
        return False


def utility(board):
    win = winner(board)
    if win == X and choice == O:
        return 1
    elif win == X and choice == X:
        return -1
    elif win == O and choice == X:
        return 1
    elif win == O and choice == O:
        return -1
    elif win == None: 
        return 0

def maxvalue(board):
    if terminal(board):
        return utility(board)
    v = -1
    for action in actions(board):
        v = max(v, minvalue(result(board, action)))
    return v

def minvalue(board):
    if terminal(board):
        return utility(board)
    v = 1
    for action in actions(board):
        v = min(v, maxvalue(result(board, action)))
    return v
    

def minimax(board):
    act = actions(board)
    moves = [None for i in range(len(act))]
    for i in range(len(act)):
        moves[i] = [act[i], None] 
    for i in range(len(moves)):
        moves[i][1] = minvalue(result(board, moves[i][0])) 
    
    next = moves[0][0]
    v = -1
    for i in range(len(moves)):
        if moves[i][1] > v:
            next = moves[i][0]
    
    return next

def display(board):
    for i in range(3):
        for j in range(3):
            print('|', end='')
            if board[i][j] == EMPTY:
                print(' ', end='')
            else:
                print(board[i][j], end='')
        print('|')
    print()


def play():
    global oboard
    if player(oboard) == choice:
        cord = [-1, -1]
        while (cord not in actions(oboard)) or (cord[0] not in range(3)) or (cord[1] not in range(3)):
            cord = list(input('Enter position (x, y) as \'xy\': '))
            temp = int(cord[0]) - 1
            cord[0] = int(cord[1]) - 1 #technical issue
            cord[1] = temp
        oboard[cord[0]][cord[1]] = choice
    else:
        cord = minimax(oboard)
        oboard[cord[0]][cord[1]] = ai


while terminal(oboard) != True:
    display(oboard)
    play()

display(oboard) 
champ = winner(oboard)
if champ != None:
    print(f"Winner: {champ}")
else: 
    print("Winner: TIE")
