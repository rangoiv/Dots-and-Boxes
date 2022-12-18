# Dots and Boxes

## How to play

Dots and Boxes is a simple pencil-and-paper game for two players. The game is played on a
grid of dots, with each player taking turns adding a single horizontal or vertical line
between two adjacent dots. When a player completes the fourth side of a 1x1 box, they
complete the box and place their initial inside of it. The goal of the game is to complete
more boxes than your opponent.

## Running the game

Run the main.py with your python editor.

When you are prompted, type the move you wish to make, in the following fashion: x, y, dir.
Here (x, y) are coordinates of the dot from which your edge is 
going (starting from 1), and dir is character 'h' or 'v'. If dir is 'h' your edge will go
from the dot (x, y) to the right and if dir is 'v' your edge will go downwards from (x, y).

Here's an example:

.-. . .  
         
. . . .  
         
. . . .  
          
. . . .  
Rangoiv turn  
Enter your move: 1 1 v  
.-. . .  
         
. . . .  
  |      
. . . .  
         
. . . .  
Sparkles turn  
.-. . .  
         
.-. . .  
  |       
. . . .  
          
. . . .  
Rangoiv turn  
Enter your move: 1 2 h  
.-. . .  
          
.-. . .  
  |       
. .-. .  
          
. . . .


## Setting up the game

You can start the game by running `main.py`. There you can
also adjust the players who are playing and their parameters,
by editing the `players` list.

Enjoy playing!

