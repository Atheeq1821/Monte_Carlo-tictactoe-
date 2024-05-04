from copy import deepcopy # to copy the instance of the board
from mcarlo import *


# board class

class Board:
    def __init__(self,board=None):
        self.player_1='x'
        self.player_2='o'
        self.empty="" # EMPTY CELL VALUE 
        self.position={} # cell values
        self.reset_board()
        # creating a copy of previous state board if available
        if board is not None:
            self.__dict__=deepcopy(board.__dict__)

    #Board reset 
    def reset_board(self):
        for row in range(3):
            for col in range(3):
                self.position[row,col]=self.empty  
    # this function runs when print(board) is called (made for user purpose)
    def __str__(self):
        current_b=""
        for row in range(3):
            for col in range(3):
                current_b+=f"{self.position[row,col]} "
            current_b+='\n'
        if self.player_1=='x':
            print("______________its x move_________")
        else:
            print("______________its o move ___________")
        return current_b   

    #Coverts the dictionary board to 2 dimentional board
    def get_board_format(self):
        b=[]
        for row in range(3):
            temp=[]
            for col in range(3):
                temp.append(self.position[row,col])
            b.append(temp)
        return b
    
    # implements the move in the board at row,col position
    def make_move(self,row,col):
        # self - current board state 
        
        board=Board(board=self)
        # create new board with the new move made based on the current state board
        board.position[row,col]=board.player_1
        # this swapping is essential so that ai can make both the moves
        (board.player_1,board.player_2) = (board.player_2,board.player_1)
        return board
    
    # function to check for draw
    def isdraw(self):
        for row,col in self.position:
            if self.position[row,col]==self.empty:
                return False
        return True
    
    # function to find winner
    def winner(self):
        
        #column winning sequence
        for col in range(3):
            if self.position[0,col]==self.position[1,col]==self.position[2,col]!=self.empty:
                return self.position[0,col]
        #row winning sequence
        for row in range(3):
            if self.position[row,0]==self.position[row,1]==self.position[row,2]!=self.empty:
                return self.position[row,0]
        #diagonal winning sequence
        if self.position[0,0]==self.position[1,1]==self.position[2,2]!=self.empty:
            return self.position[0,0]
        # reverse diagonal winning sequence
        elif self.position[0,2]==self.position[1,1]==self.position[2,0]!=self.empty:
            return self.position[0,2]
        return False

    # generating available move states for particular state    
    def generate_states(self):
        actions=[] # this will have all the possible actions can be made on the current state
            
        for row in range(3):
            for col in range(3):
                if self.position[row,col]==self.empty:
                    actions.append(self.make_move(row,col))
        return actions   
    
     