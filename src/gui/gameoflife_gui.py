import re
import sys
import argparse
from tkinter import Tk, Canvas
from tkinter import BOTH
from src.game.gameoflife import next_generation, get_bounds


class Colors:
    DARK       = "#111a1e"
    LESS_DARK  = "#142229"
    WHITE      = "#ffffff"
    GREEN      = "#6cd777"
    ORANGE     = "#D66825"
    DARKORANGE = "#723612"


class Dimensions:
    CANVAS = (700, 500)
    CELL_SIZE = 12
    ROWS, COLUMNS = CANVAS[1] // CELL_SIZE, CANVAS[0] // CELL_SIZE
    XY_START_POS = 4


class State:
    options    = ['fill', 'activefill', 'outline']
    vals_dead  = [Colors.LESS_DARK, Colors.DARKORANGE, Colors.ORANGE]
    vals_alive = [Colors.ORANGE, Colors.ORANGE, Colors.WHITE]

    DEAD  = dict( zip(options, vals_dead) )
    ALIVE = dict( zip(options, vals_alive) )


def create_cells(master):
    xy1 = lambda row, col: (Dimensions.XY_START_POS + pos * Dimensions.CELL_SIZE for pos in [row, col] )
    xy2 = lambda row, col:  (pos + Dimensions.CELL_SIZE for pos in xy1(row, col))

    return { (y_axis, x_axis): master.create_rectangle( *xy1(x_axis, y_axis), *xy2(x_axis, y_axis), State.DEAD ) \
        for y_axis in range(Dimensions.ROWS) \
            for x_axis in range(Dimensions.COLUMNS) }

def set_cells(live_cells, all_cells, master):
    live_cells = [ str(cell) for cell in live_cells ]
    for cell in all_cells: master.itemconfig(all_cells[cell], **State.ALIVE) \
        if str(cell) in live_cells else master.itemconfig(all_cells[cell], **State.DEAD)

def filter_seed(raw_seed):
    return [ (int(val.split(',')[0]), int(val.split(',')[1])) for val in [ item for item in re.findall(r'\((.*?)\)', raw_seed) ] ]

def loop(seed, grid, board):
    seed = next_generation(seed)
    set_cells(seed, grid, board)
    board.after(500, lambda: loop(seed, grid, board))


def main():
    print("Input format example (can copy and paste this below): (12, 10) (12, 11) (12, 12) (12, 13) (12, 14)")
    user_input = input("Enter starting seed (use above format): ")
    seed = filter_seed(user_input) if len(user_input) > 1 else ''
    root = Tk()
    root.title("Conway's Game of Life")
    board = Canvas(root, width=Dimensions.CANVAS[0],
                         height=Dimensions.CANVAS[1],
                         bg=Colors.DARK)
    grid = create_cells(board)
    board.pack(fill=BOTH)

    set_cells(seed, grid, board)

    root.update()
    root.bind("<Control-c>", lambda e: root.quit())
    root.resizable(False, False)
    root.geometry(f"{Dimensions.CANVAS[0] + 5}x{Dimensions.CANVAS[1] + 1}")
    root.after(0, lambda: loop(seed, grid, board))
    root.mainloop()

if __name__ == '__main__':
    main()