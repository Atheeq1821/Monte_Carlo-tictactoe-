
# MONTE CARLO AI BASED TIC TAC TOE GAME

## You can play this game on  - [link](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
Monte Carlo Tic-Tac-Toe is a Python-based implementation of the classic Tic-Tac-Toe game with added artificial intelligence using the Monte Carlo search method. This project offers players the opportunity to play against an AI opponent at three different difficulty levels, each corresponding to a different number of iterations in the Monte Carlo search algorithm.




## MCTS Space Tree for Tictactoe

![App Screenshot](https://nestedsoftware.com/assets/images/2019-08-07-tic-tac-toe-with-mcts-2h5k.152104/6dpz3fabybointn48xte.png)



# Workflow : - 

### 1.Initialization :
At the start of the game, the AI randomly chooses whether to play as "X" or "O". This decision is made to ensure fairness and variability in gameplay.

### 2.Player Interaction:
If the AI is assigned as "X", it makes the first move. Otherwise, it waits for the player to make their first move.

### 3.Player Move Processing:
After the player makes a move, JavaScript captures the player's move (row, col) and sends it to the Python backend (Flask).
Python then updates the game board with the player's move and evaluates the current state of the game, checking for winning or draw conditions.

### 4.Updating the Board:
Python returns the current state of the board to JavaScript, along with the information about winning or draw states.
JavaScript updates the game board on the frontend based on the received state.

### 5. AI Move Search :

The AI move search method employs the Monte Carlo search algorithm with the UCT (Upper Confidence Bound for Trees) formula.

#### move_score= current_player *child.score / child.visits + epsilon * math.sqrt(math.log(node.visits / child.visits))
It iteratively explores possible moves by expanding the current state of the board and simulating games until completion.
The algorithm calculates scores for each move based on the UCT formula, considering factors like the current player, the score of the child node, and the number of visits.
After selecting the best move, the AI makes its move on the current state of the board
### 6. Game Continuation :
The game continues until a winning or draw state is reached.


## Installation




### Use Command prompt
```bash
  git clone https://github.com/Atheeq1821/Monte_Carlo-tictactoe-.git
  
  cd Monte_Carlo-tictactoe-
  
  pip install -r requirements.txt
  
  python app.py
```

# ENJOY YOUR PLAY
    
