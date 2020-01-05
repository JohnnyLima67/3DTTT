# 3DTTT
An implementation of a single player 3D Tic Tac Toe game using  the pygame library

<h1>Introduction:</h1>
In this project , we made an AI for the 3D Implementation of Tic-Tac-
Toe (4x4x4) using the minimax algorithm. Due to the high
computation required to calculate all possible outcomes 
we limit the lookahead to 2 moves.
This effectively breaks down the minimax implementation to a directwin
achiever or blocker. To improve the performance of the AI , we
added a if-else if sequence to choose moves which are more likely to
lead to a win condition , this effectively simulates a heuristic in which
the more preferred moves would return a higher score.
It is good to note that on implementing the same AI without the
heuristic but with a lookahead of 3 or 4 we have about the same or
deteriorated performance in terms of speed and deteriorated or about
the same performance in terms of outperforming the player
respectively when compared with the implementation mentioned in
the previous paragraphs

<h1>Project Files:</h1>
<h2>1. main.py</h2>
The main file , contains UI implemented in pygame. It calls the Movebest()
function when it ts the AI's turn to play
<h2>2. minimax.py</h2>
Contains the implementation of Movebest() and minimax() functions ,
where the Movebest function uses the minimax function and the if-else if
sequence to change the board state according to the optimal move for the
AI
<h2>3. checkComplete.py</h2>
Contains the isComplete() function used to check for win condition and
the hasSpace() function to check for draw condition(Board is full)
<h2>4. init.py</h2>
Contains the init_board() function used to initialize the 4x4x4 board with
all states set to empty
<h2>5. progressbar.py</h2>
Contains ProgressBar class used while debugging and testing
<h2>6. view.py</h2>
Contains functions for debugging to check board state from different views

<h1>Dependencies:</h1>
⦁ Python 3
⦁ Pygame
⦁ Pip

<h1>Execution And GUI:</h1>
To run and play against the AI , move all the files into one directory
and after opening a command terminal in that directory , use the
command:
<i>python main.py</i>
It is important to note that the execution requires python and pygame
installed on the system in the current environment
The game will play out like a regular tic tac toe game , alternating
between player(X) and AI(O) , the Player can click on the square
they wish to play their move on.
