# Dots and Boxes

## How to play

Dots and Boxes is a simple pencil-and-paper game for two players. The game is played on a
grid of dots, with each player taking turns adding a single horizontal or vertical line
between two adjacent dots. When a player completes the fourth side of a 1x1 box, they
complete the box and place their initial inside of it. The goal of the game is to complete
more boxes than your opponent.

## Running the game

Run the main.py with your python editor.

When you are prompted, type the move you wish to make, in the following fashion: i, j, dir.
Here (i, j) are coordinates of the dot from which your edge is 
going (starting from 0), and dir is character 'h' or 'v'. If dir is 'h' your edge will go
from the dot (i, j) to the right and if dir is 'v' your edge will go downwards from (i, j).

Here's an example:

. . . .  
        
. . . .  
        
. . . .  
        
. . . .  
Scores: X=0, O=0  
Player X, enter your edge: 0 0 v
   
.-. . .  
       
. . . .  
        
. . . .  
        
. . . .  
Scores: X=0, O=0  
Player O, enter your edge: ...


## Setting up the game

You can change the size of the field, number of players or play against AI by setting
the variables at the top of the main.py accordingly.

Enjoy playing! :)

