# Importation
from flask import Flask,render_template,jsonify
from utils import choose,possible
from tictactoe import *
from mcarlo import *


app = Flask(__name__)


#initialization of all required variables
#################################
board = [["","",""],["","",""],["","",""]]
player='o'
opponent='x'
mcts = Mcts()
mcboard = Board()
########################################


#Routing to home.html
@app.route('/')
def index():
    return render_template('home.html')


#this assigns x and o for ai and player randomly 
#if ai is x then ai makes the move first
@app.route("/start")
def start():
    global mcts,mcboard,board,opponent,player
    board = [["","",""],["","",""],["","",""]]
    opponent,player=choose()

    mcboard = Board()
    #ai makes its first move
    if player=='x':
        best = mcts.search(mcboard)
        mcboard = best.board
        board=mcboard.get_board_format()
    return render_template('index.html', opponent=opponent, player=player,board=board)


#making the player move
@app.route('/move/<string:index>')
def move(index):
    #index is received from the javascript file
    global board,mcboard
    if len(index)==1:
        i=0
    else:
        i=int(index[0])
    j = int(index[-1]) #i,j -> move in row and col in the board 
    if board[i][j] == '':
        #making the player's move in the board
        mcboard=mcboard.make_move(i,j)
        board=mcboard.get_board_format()
        winner=mcboard.winner()

        #check whether player is winner
        if winner==opponent: #opponent -> human 
            return jsonify({'cell_values': board, "oppo":True, "play": False , "tie": False}) #play -> ai
        
        #check the Draw state
        if not possible(board):
            print("Tie")
            return jsonify({'cell_values': board, "oppo":False, "play": False , "tie": True})

    return jsonify({'cell_values': board, "oppo":False, "play": False , "tie": False})


#Ai making its move using monte carlo
@app.route("/aiMove")
def aiMove():
    global board,mcboard,mcts
    #best move fro the monte carlo
    best = mcts.search(mcboard)

    #mmaking the best move on the board
    mcboard = best.board

    board=mcboard.get_board_format()

    winner=mcboard.winner()
    #check whether ai won with its move
    if winner==player: #player -> AI
            return jsonify({'cell_values': board, "oppo":False, "play": True , "tie": False}) #play -> ai
    
    #check the Draw state
    if not possible(board):
        print("Tie")
        return jsonify({'cell_values': board, "oppo":False, "play": False , "tie": True})

    return jsonify({'cell_values': board, "oppo":False, "play": False , "tie": False})


if __name__ == "__main__":
    app.run()