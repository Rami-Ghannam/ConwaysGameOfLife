import re
import sys
import numpy as np
from random import randint
from tkinter import BOTH
from tkinter import Tk, Canvas
from src.game.gameoflife import next_generation, get_bounds

maxRC = lambda: (CANVAS[1] // CELL_SIZE, CANVAS[0] // CELL_SIZE)

CANVAS        = (1000, 1000)
XY_START_POS  = 4
CELL_SIZE     = 17
BUFFER        = 2
ROWS, COLUMNS = maxRC()
ROW_START     = 0
COL_START     = 0
ROW_STOP      = ROW_START + ROWS
COL_STOP      = COL_START + COLUMNS
SPEED         = 300


class Colors:
    FILL    = "#beba46"
    OUTLINE = HIDE = "#771414"
    ALIVE = "#8bd3fb"


class State:
    ALIVE = { 'fill': Colors.ALIVE, 'outline': Colors.OUTLINE }
    DEAD  = { 'fill': Colors.FILL,  'outline': Colors.OUTLINE }
    HIDE  = dict( zip( ['fill', 'outline'], [ Colors.HIDE ] * 2 ))


def filter_seed(raw_seed):
    return [ (int(val.split(',')[0]), int(val.split(',')[1])) for val in [ item for item in re.findall(r'\((.*?)\)', raw_seed) ] ]

def set_bounds(bounds):
    global ROWS, COLUMNS, ROW_START, ROW_STOP, COL_START, COL_STOP
    top_left, bottom_right = bounds if bounds else [(0, 0), (0, 0)]

    ROWS, COLUMNS = np.add( [bottom_right[0] - top_left[0], bottom_right[1] - top_left[1] ], [5, 5] )
    ROW_START, COL_START = (n - BUFFER for n in top_left)
    ROW_STOP, COL_STOP = np.add([ROW_START, COL_START], [ROWS, COLUMNS])
    
def create_cells(master):
    master.delete("all")
    xy1 = lambda row, col: (XY_START_POS + pos * CELL_SIZE for pos in [row, col] )
    xy2 = lambda row, col:  (pos + CELL_SIZE for pos in xy1(row, col))

    return { (y_axis, x_axis): master.create_rectangle( *xy1(x, y), *xy2(x, y), State.DEAD ) \
        for y, y_axis in enumerate(range(ROW_START, ROW_STOP)) \
            for x, x_axis in enumerate(range(COL_START, COL_STOP)) }

def set_cells(live_cells, all_cells, master):
    live_cells = [ str(cell) for cell in live_cells ]
    
    for cell in all_cells:
        if str(cell) in live_cells:
            master.itemconfig(all_cells[cell], **State.ALIVE)
        elif cell[0] in range(ROW_START, ROW_STOP) and cell[1] in range(COL_START, COL_STOP):
            master.itemconfig(all_cells[cell], **State.DEAD)
        else:
            master.itemconfig(all_cells[cell], **State.HIDE)

def loop(seed, grid, board):
    global CELL_SIZE, ROWS, COLUMNS, CANVAS

    set_bounds(get_bounds(seed))
    grid = create_cells(board)
    set_cells(seed, grid, board)
    seed = next_generation(seed)
    board.after(SPEED, lambda: loop(seed, grid, board))


def main():
    seed = filter_seed(sys.argv[1]) if len(sys.argv) > 1 else ''
    root = Tk()
    root.title("Conway's Game of Life")

    board = Canvas(root, width=CANVAS[0],
                         height=CANVAS[1],
                         bg=Colors.FILL)
    grid = create_cells(board)
    board.pack(fill=BOTH)

    root.update() 
    root.bind("<Control-c>", lambda e: root.quit())
    root.resizable(True, True)
    root.geometry(f"{CANVAS[0]}x{CANVAS[1]}")
    root.after(0, lambda: loop(seed, grid, board))
    root.mainloop()

if __name__ == '__main__':
    main()