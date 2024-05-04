import random
import math



#TreeNode  -> considered as a state in the game
class TreeNode:
    def __init__(self,board,parent):
        self.board=board

        if self.board.winner() or self.board.isdraw():
            self.isTerminal=True
        else:
            self.isTerminal=False
        self.isExpanded=self.isTerminal #all the actions are explored at the current state
        self.parent=parent
        self.children={}
        self.visits=0 #how many times the current state been visited
        self.score=0  #state-action value 


class Mcts:
    #searching for the best move at current state
    def search(self,current_state,iteration):
        self.root = TreeNode(current_state,None)
        #Iterations
        for iterations in range(iteration):
            #select an action
            node=self.select(self.root)
            #simulation phase - score estimation
            score = self.rollout(node.board)
            #Backpropagating 
            self.backpropagate(node=node,score=score)
        try:
            return self.get_best_move(self.root,0)
        except:
            pass

    #selecting node/action in current state   
    def select(self,node):
        while not node.isTerminal:
            if  node.isExpanded:
                node=self.get_best_move(node,2)
            else:
                return self.expand(node) #all the new state from the current states are expanded as the children
        return node
    
    def expand(self,node):
        #generateing legal states for the given node

        states=node.board.generate_states()

        #loop over these states
        for state in states:
            if str(state.position) not in node.children:
                new_node = TreeNode(state,node) #new_node -> child  :  node -> parent
                node.children[str(state.position)]=new_node
                if len(states)==len(node.children):
                    node.isExpanded=True
                return new_node
            
    def rollout(self,board):
        #make moves on both sides until the end

        while not board.winner() and not board.isdraw():
            #try to make a move
            try:
                board=random.choice(board.generate_states())
            #check draw state and return draw score
            except:
                return 0

        if board.player_1=='x':
            return 1
        elif board.player_1=='o':
            return -1
        
    def backpropagate(self,node,score):
        #update the visits and score from the current node to the root node
        while node is not None:
            node.visits+=1
            node.score+=score
            node=node.parent   

    #core function of Mnte carlo .. it choses best node/action from available actions.
    # This function also includes exploration constant - epsilon
    def get_best_move(self,node, epsilon):
        best_score=-float('inf')
        best_move=[]
    
        for child in node.children.values():
            if child.board.player_1 =='x':
               current_player=1
            else:
               current_player=-1

            #UCT formula for move score
            move_score= current_player *child.score / child.visits + epsilon * math.sqrt(math.log(node.visits / child.visits))
            if move_score >  best_score:
                best_score=move_score
                best_move=[child]
            elif move_score==best_score:
                best_move.append(child)
        return random.choice(best_move) #if more than one best actions are found .. some random choices are made
