import random

player='o'
opponent='x'


# Choosing which player is 'O' and 'X' randomly
def choose():
    global opponent,player,isMax
    num=random.randint(0,1)
    if num==0:
        opponent='o'
        player='x'
    elif num==1:
        opponent='x'
        player='o'
    return opponent,player


#checks whther there is any available move to make
def possible(board):
    for i in range(3):
        for j in range(3):
            if board[i][j]=='':
                return True
    return False