This project implements Conway's Game of Life https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life  

The user will input the initial state of the game through (x,y) coordinates as command line arguments, then the game will commence automatically.   
  
The evolution of the cells follow these four rules:  
  1) Any live cell with fewer than two live neighbours dies, as if by underpopulation.  
  2) Any live cell with two or three live neighbours lives on to the next generation.  
  3) Any live cell with more than three live neighbours dies, as if by overpopulation.  
  4) Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.  

To run the code start in the main directory and use the following command/format:  
python -m src.gui.gameoflife_gui '(12, 10) (12, 11) (12, 12) (12, 13) (12, 14)'
